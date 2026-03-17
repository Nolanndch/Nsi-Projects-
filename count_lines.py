#!/usr/bin/env python3
"""
count_lines.py — Compte les lignes de code des fichiers Python de votre workspace.

Usage:
    python count_lines.py                  # Dossier courant
    python count_lines.py /chemin/dossier  # Dossier spécifié
    python count_lines.py --no-blank       # Exclure les lignes vides
    python count_lines.py --no-comments    # Exclure les commentaires
"""

import os
import sys
import argparse
from pathlib import Path


def count_lines_in_file(
    filepath: Path, count_blank: bool, count_comments: bool
) -> dict:
    """Compte les lignes d'un fichier Python."""
    total = 0
    blank = 0
    comments = 0
    code = 0

    try:
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            lines = f.readlines()

        total = len(lines)
        for line in lines:
            stripped = line.strip()
            if stripped == "":
                blank += 1
            elif stripped.startswith("#"):
                comments += 1
            else:
                code += 1

    except (OSError, PermissionError) as e:
        print(f"  ⚠️  Impossible de lire {filepath}: {e}")
        return None

    effective = 0
    if count_blank:
        effective += blank
    if count_comments:
        effective += comments
    effective += code

    return {
        "total": total,
        "code": code,
        "comments": comments,
        "blank": blank,
        "effective": effective,
    }


def find_python_files(root: Path) -> list[Path]:
    """Trouve récursivement tous les fichiers .py."""
    return sorted(root.rglob("*.py"))


def format_number(n: int) -> str:
    return f"{n:,}".replace(",", " ")


def print_separator(width: int = 80):
    print("─" * width)


def main():
    parser = argparse.ArgumentParser(
        description="Compte les lignes de code des fichiers Python."
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Chemin du dossier à analyser (défaut: dossier courant)",
    )
    parser.add_argument(
        "--no-blank",
        action="store_true",
        help="Ne pas compter les lignes vides",
    )
    parser.add_argument(
        "--no-comments",
        action="store_true",
        help="Ne pas compter les lignes de commentaires",
    )
    parser.add_argument(
        "--top",
        type=int,
        default=None,
        metavar="N",
        help="Afficher uniquement les N fichiers les plus grands",
    )
    parser.add_argument(
        "--min-lines",
        type=int,
        default=0,
        metavar="N",
        help="Ignorer les fichiers avec moins de N lignes",
    )

    args = parser.parse_args()

    root = Path(args.path).resolve()
    if not root.exists():
        print(f"❌ Erreur : le chemin '{root}' n'existe pas.")
        sys.exit(1)
    if not root.is_dir():
        print(f"❌ Erreur : '{root}' n'est pas un dossier.")
        sys.exit(1)

    count_blank = not args.no_blank
    count_comments = not args.no_comments

    print()
    print("🐍  Python Line Counter")
    print_separator()
    print(f"📁  Dossier  : {root}")
    print(f"📊  Comptage : code", end="")
    if count_comments:
        print(" + commentaires", end="")
    if count_blank:
        print(" + lignes vides", end="")
    print()
    print_separator()

    files = [
        f for f in find_python_files(root) if f.resolve() != Path(__file__).resolve()
    ]

    if not files:
        print("Aucun fichier .py trouvé.")
        sys.exit(0)

    results = []
    for f in files:
        stats = count_lines_in_file(f, count_blank, count_comments)
        if stats and stats["total"] >= args.min_lines:
            results.append((f, stats))

    # Trier par lignes effectives décroissant
    results.sort(key=lambda x: x[1]["effective"], reverse=True)

    if args.top:
        results = results[: args.top]

    # Affichage tableau
    col_file = 50
    col_code = 8
    col_cmt = 10
    col_blank = 8
    col_total = 8

    header = (
        f"{'Fichier':<{col_file}} {'Code':>{col_code}} {'Commentaires':>{col_cmt}} "
        f"{'Vides':>{col_blank}} {'Total':>{col_total}}"
    )
    print(header)
    print_separator()

    total_code = total_comments = total_blank = total_total = 0

    for filepath, stats in results:
        try:
            rel = filepath.relative_to(root)
        except ValueError:
            rel = filepath

        rel_str = str(rel)
        if len(rel_str) > col_file:
            rel_str = "…" + rel_str[-(col_file - 1) :]

        print(
            f"{rel_str:<{col_file}} "
            f"{format_number(stats['code']):>{col_code}} "
            f"{format_number(stats['comments']):>{col_cmt}} "
            f"{format_number(stats['blank']):>{col_blank}} "
            f"{format_number(stats['total']):>{col_total}}"
        )

        total_code += stats["code"]
        total_comments += stats["comments"]
        total_blank += stats["blank"]
        total_total += stats["total"]

    print_separator()

    total_effective = total_code
    if count_comments:
        total_effective += total_comments
    if count_blank:
        total_effective += total_blank

    print(
        f"{'TOTAL  (' + str(len(results)) + ' fichiers)':<{col_file}} "
        f"{format_number(total_code):>{col_code}} "
        f"{format_number(total_comments):>{col_cmt}} "
        f"{format_number(total_blank):>{col_blank}} "
        f"{format_number(total_total):>{col_total}}"
    )
    print_separator()
    print(f"\n✅  Lignes effectives comptabilisées : {format_number(total_effective)}")
    print(f"    dont code pur                    : {format_number(total_code)}")
    print(f"    dont commentaires                : {format_number(total_comments)}")
    print(f"    dont lignes vides                : {format_number(total_blank)}")
    print()


if __name__ == "__main__":
    main()
