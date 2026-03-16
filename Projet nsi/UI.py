import pygame
import parametres
import bouton
import fonction
import entities
import math
from parametres import xbouton, ybouton, largeur_bouton, hauteur_bouton, taille_cell

screen = parametres.ecran


def _draw_stat_card(
    screen, x, y, w, h, label, current, maximum, bar_color, font_small, font_label
):
    PANEL_CARD = (24, 28, 38)
    PANEL_BORDER = (40, 46, 60)
    TEXT_MAIN = (230, 235, 245)
    TEXT_MUTED = (110, 120, 145)

    card_rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, PANEL_CARD, card_rect, border_radius=6)
    pygame.draw.rect(screen, PANEL_BORDER, card_rect, width=1, border_radius=6)

    lbl_surf = font_label.render(label, True, TEXT_MUTED)
    screen.blit(lbl_surf, (x + 10, y + 8))

    val_surf = font_small.render(f"{current}/{maximum}", True, TEXT_MAIN)
    screen.blit(val_surf, (x + w - val_surf.get_width() - 10, y + 8))

    bar_x, bar_y = x + 10, y + 36
    bar_w, bar_h = w - 20, 7
    pygame.draw.rect(
        screen, PANEL_BORDER, (bar_x, bar_y, bar_w, bar_h), border_radius=3
    )

    fill = max(0, min(1, current / maximum)) if maximum > 0 else 0
    if fill > 0:
        pygame.draw.rect(
            screen, bar_color, (bar_x, bar_y, int(bar_w * fill), bar_h), border_radius=3
        )


# ── MENU ─────────────────────────────────────────────────────────────────────
def menu(screen):
    BG_COLOR = (13, 16, 23)
    PANEL_BORDER = (40, 46, 60)
    CARD_BG = (24, 28, 38)
    TEXT_MAIN = (230, 235, 245)
    TEXT_MUTED = (110, 120, 145)
    ACCENT = (99, 179, 237)

    sw, sh = screen.get_width(), screen.get_height()
    screen.fill(BG_COLOR)

    font_title = pygame.font.SysFont("Courier New", 48, bold=True)
    font_sub = pygame.font.SysFont("Courier New", 16)
    font_btn = pygame.font.SysFont("Courier New", 18, bold=True)
    font_label = pygame.font.SysFont("Courier New", 15)

    title_surf = font_title.render("Wave puncher", True, TEXT_MAIN)
    sub_surf = font_sub.render(
        "v0.1  —  un jeu de rôle au tour par tour", True, TEXT_MUTED
    )
    screen.blit(title_surf, (sw // 2 - title_surf.get_width() // 2, sh // 2 - 220))
    screen.blit(sub_surf, (sw // 2 - sub_surf.get_width() // 2, sh // 2 - 158))

    line_w = 120
    pygame.draw.line(
        screen,
        ACCENT,
        (sw // 2 - line_w // 2, sh // 2 - 132),
        (sw // 2 + line_w // 2, sh // 2 - 132),
        1,
    )

    btn_w, btn_h = 240, 50
    btn_x = sw // 2 - btn_w // 2
    buttons = [
        (bouton.Jouer_bt, bouton.Jouer_txt, ACCENT, True),
        (bouton.parametre_bt, bouton.parametre_txt, CARD_BG, False),
        (bouton.rules_bt, bouton.rules_txt, CARD_BG, False),
    ]

    for i, (rect, txt, bg, is_primary) in enumerate(buttons):
        by = sh // 2 - 90 + i * 66
        rect.x, rect.y = btn_x, by
        rect.width, rect.height = btn_w, btn_h
        btn_rect = pygame.Rect(btn_x, by, btn_w, btn_h)

        if is_primary:
            pygame.draw.rect(screen, ACCENT, btn_rect, border_radius=6)
            lbl = font_btn.render(txt, True, BG_COLOR)
        else:
            pygame.draw.rect(screen, bg, btn_rect, border_radius=6)
            pygame.draw.rect(screen, PANEL_BORDER, btn_rect, width=1, border_radius=6)
            lbl = font_btn.render(txt, True, TEXT_MAIN)

        screen.blit(
            lbl,
            (
                btn_x + (btn_w - lbl.get_width()) // 2,
                by + (btn_h - lbl.get_height()) // 2,
            ),
        )

    exit_rect = pygame.Rect(12, 12, 70, 32)
    bouton.exit_bt.x, bouton.exit_bt.y = 12, 12
    bouton.exit_bt.width, bouton.exit_bt.height = 70, 32
    pygame.draw.rect(screen, CARD_BG, exit_rect, border_radius=4)
    pygame.draw.rect(screen, PANEL_BORDER, exit_rect, width=1, border_radius=4)
    exit_lbl = font_label.render("EXIT", True, TEXT_MUTED)
    screen.blit(
        exit_lbl,
        (12 + (70 - exit_lbl.get_width()) // 2, 12 + (32 - exit_lbl.get_height()) // 2),
    )


# ── PLAY ─────────────────────────────────────────────────────────────────────
def play(screen, grille_jeu, joueur):
    BG_COLOR = (13, 16, 23)
    PANEL_BG = (15, 17, 23)
    PANEL_BORDER = (40, 46, 60)
    CARD_BG = (24, 28, 38)
    TEXT_MAIN = (230, 235, 245)
    TEXT_MUTED = (110, 120, 145)
    ACCENT = (99, 179, 237)
    HP_COLOR = (72, 199, 142)
    ARMOR_COLOR = (99, 179, 237)
    XP_COLOR = (250, 204, 21)
    GRID_BG = (22, 28, 42)
    GRID_LINE = (38, 48, 68)
    TURN_JOUEUR = (99, 179, 237)
    TURN_MOB = (252, 129, 74)

    sw, sh = screen.get_width(), screen.get_height()
    screen.fill(BG_COLOR)

    panel_w = 230
    panel_x = sw - panel_w - 16
    panel_rect = pygame.Rect(panel_x - 8, 0, panel_w + 24, sh)
    pygame.draw.rect(screen, PANEL_BG, panel_rect)
    pygame.draw.line(screen, PANEL_BORDER, (panel_x - 8, 0), (panel_x - 8, sh), 1)

    font_title = pygame.font.SysFont("Courier New", 18, bold=True)
    font_label = pygame.font.SysFont("Courier New", 15)
    font_small = pygame.font.SysFont("Courier New", 16, bold=True)
    font_value = pygame.font.SysFont("Courier New", 26, bold=True)

    title_surf = font_title.render("JOUEUR", True, TEXT_MUTED)
    screen.blit(title_surf, (panel_x + (panel_w - title_surf.get_width()) // 2, 20))
    pygame.draw.line(screen, PANEL_BORDER, (panel_x, 44), (panel_x + panel_w, 44), 1)

    cy = 58

    niv_label = font_label.render("NIVEAU", True, TEXT_MUTED)
    screen.blit(niv_label, (panel_x + 10, cy))
    niv_val = font_value.render(str(entities.j1.niveau), True, ACCENT)
    screen.blit(niv_val, (panel_x + panel_w - niv_val.get_width() - 10, cy - 4))
    cy += 36

    _draw_stat_card(
        screen,
        panel_x,
        cy,
        panel_w,
        52,
        "XP",
        entities.j1.xp,
        10,
        XP_COLOR,
        font_small,
        font_label,
    )
    cy += 64

    _draw_stat_card(
        screen,
        panel_x,
        cy,
        panel_w,
        52,
        "VIE",
        entities.j1.life,
        entities.j1.max_life,
        HP_COLOR,
        font_small,
        font_label,
    )
    cy += 64

    _draw_stat_card(
        screen,
        panel_x,
        cy,
        panel_w,
        52,
        "ARMURE",
        entities.j1.armor,
        entities.j1.max_armor,
        ARMOR_COLOR,
        font_small,
        font_label,
    )
    cy += 74

    pygame.draw.line(
        screen, PANEL_BORDER, (panel_x, cy - 8), (panel_x + panel_w, cy - 8), 1
    )
    dep_label = font_label.render("DÉPLACEMENTS", True, TEXT_MUTED)
    screen.blit(dep_label, (panel_x + 10, cy))
    cy += 22
    deps = getattr(
        parametres, "deplacement_joueur_restants", parametres.deplacement_joueur_max
    )
    dep_val = font_value.render(str(deps), True, TEXT_MAIN)
    screen.blit(dep_val, (panel_x + (panel_w - dep_val.get_width()) // 2, cy))
    cy += 50

    pygame.draw.line(screen, PANEL_BORDER, (panel_x, cy), (panel_x + panel_w, cy), 1)
    cy += 14
    is_joueur = parametres.tour_deplacement == "joueur"
    badge_color = TURN_JOUEUR if is_joueur else TURN_MOB
    badge_txt = "TON TOUR" if is_joueur else "TOUR ENNEMI"
    badge_rect = pygame.Rect(panel_x + 10, cy, panel_w - 20, 32)
    pygame.draw.rect(screen, CARD_BG, badge_rect, border_radius=5)
    pygame.draw.rect(screen, badge_color, badge_rect, width=1, border_radius=5)
    badge_surf = font_label.render(badge_txt, True, badge_color)
    screen.blit(
        badge_surf,
        (
            panel_x + (panel_w - badge_surf.get_width()) // 2,
            cy + (32 - badge_surf.get_height()) // 2,
        ),
    )

    grille_size = parametres.taille_grille * taille_cell
    grid_x = (sw - panel_w - 24 - grille_size) // 2
    grid_y = (sh - grille_size) // 2

    pygame.draw.rect(
        screen,
        GRID_BG,
        (grid_x - 2, grid_y - 2, grille_size + 4, grille_size + 4),
        border_radius=4,
    )

    for (cx_g, cy_g), cell in grille_jeu.items():
        rx = grid_x + cx_g * taille_cell
        ry = grid_y + cy_g * taille_cell
        pygame.draw.rect(screen, GRID_BG, (rx, ry, taille_cell, taille_cell))
        pygame.draw.rect(screen, GRID_LINE, (rx, ry, taille_cell, taille_cell), 1)

    # ── Joueur ───────────────────────────────────────────────────
    jx = grid_x + joueur.x * taille_cell
    jy = grid_y + joueur.y * taille_cell
    cx_j = jx + taille_cell // 2
    cy_j = jy + taille_cell // 2
    r = taille_cell // 2 - 2

    # Halo joueur
    halo = pygame.Surface((taille_cell * 3, taille_cell * 3), pygame.SRCALPHA)
    pygame.draw.circle(halo, (99, 179, 237, 35), (taille_cell + taille_cell // 2, taille_cell + taille_cell // 2), taille_cell)
    screen.blit(halo, (cx_j - taille_cell - taille_cell // 2, cy_j - taille_cell - taille_cell // 2))

    # Losange joueur (bleu accent)
    points = [
        (cx_j,     cy_j - r),
        (cx_j + r, cy_j),
        (cx_j,     cy_j + r),
        (cx_j - r, cy_j),
    ]
    pygame.draw.polygon(screen, (99, 179, 237), points)
    pygame.draw.polygon(screen, (180, 220, 255), points, 1)

    # ── Entités ───────────────────────────────────────────────────
    for cell in grille_jeu.values():
        if cell.contenu is None:
            continue

        ex = grid_x + cell.x * taille_cell + taille_cell // 2
        ey = grid_y + cell.y * taille_cell + taille_cell // 2
        r  = taille_cell // 2 - 2
        col = cell.contenu.couleur

        # Détecte le type par couleur
        is_mob   = (col[0] > 150 and col[1] < 100)                    # rouge  → mob
        is_heal  = (col[1] > 150 and col[0] < 100)                    # vert   → soin
        is_shield= (col[2] > 150 and col[0] < 100 and col[1] < 100)  # bleu   → shield

        if is_mob:
            # Triangle pointé vers le bas (menaçant)
            pts = [
                (ex,     ey - r),
                (ex + r, ey + r),
                (ex - r, ey + r),
            ]
            pygame.draw.polygon(screen, (220, 60, 60), pts)
            pygame.draw.polygon(screen, (255, 120, 120), pts, 1)

        elif is_heal:
            # Croix (soin)
            t = max(2, taille_cell // 6)
            pygame.draw.rect(screen, (72, 199, 142), (ex - t, ey - r, t * 2, r * 2))
            pygame.draw.rect(screen, (72, 199, 142), (ex - r, ey - t, r * 2, t * 2))
            # Contour léger
            pygame.draw.rect(screen, (140, 230, 180), (ex - t, ey - r, t * 2, r * 2), 1)
            pygame.draw.rect(screen, (140, 230, 180), (ex - r, ey - t, r * 2, t * 2), 1)

        elif is_shield:
            # Hexagone (bouclier)
            pts = [
                (int(ex + r * math.cos(math.radians(a))),
                 int(ey + r * math.sin(math.radians(a))))
                for a in range(0, 360, 60)
            ]
            pygame.draw.polygon(screen, (56, 130, 200), pts)
            pygame.draw.polygon(screen, (99, 179, 237), pts, 1)

        else:
            # Fallback cercle
            pygame.draw.circle(screen, col, (ex, ey), r)
            pygame.draw.circle(screen, (200, 200, 200), (ex, ey), r, 1)
            
    exit_rect = pygame.Rect(12, 12, 70, 32)
    bouton.exit_bt.x, bouton.exit_bt.y = 12, 12
    bouton.exit_bt.width, bouton.exit_bt.height = 70, 32
    pygame.draw.rect(screen, PANEL_BG, exit_rect, border_radius=4)
    pygame.draw.rect(screen, PANEL_BORDER, exit_rect, width=1, border_radius=4)
    font_exit = pygame.font.SysFont("Courier New", 15)
    exit_surf = font_exit.render("EXIT", True, TEXT_MUTED)
    screen.blit(
        exit_surf,
        (
            12 + (70 - exit_surf.get_width()) // 2,
            12 + (32 - exit_surf.get_height()) // 2,
        ),
    )


# ── PARAMETRE ─────────────────────────────────────────────────────────────────
def parametre(screen):
    BG_COLOR = (13, 16, 23)
    PANEL_BORDER = (40, 46, 60)
    CARD_BG = (24, 28, 38)
    TEXT_MAIN = (230, 235, 245)
    TEXT_MUTED = (110, 120, 145)
    ACCENT = (99, 179, 237)

    sw, sh = screen.get_width(), screen.get_height()
    screen.fill(BG_COLOR)

    font_head = pygame.font.SysFont("Courier New", 30, bold=True)
    font_sub = pygame.font.SysFont("Courier New", 16)
    font_btn = pygame.font.SysFont("Courier New", 18, bold=True)
    font_label = pygame.font.SysFont("Courier New", 15)

    title_surf = font_head.render("PARAMÈTRES", True, TEXT_MAIN)
    screen.blit(title_surf, (sw // 2 - title_surf.get_width() // 2, 80))
    sub_surf = font_sub.render("Choisir la difficulté", True, TEXT_MUTED)
    screen.blit(sub_surf, (sw // 2 - sub_surf.get_width() // 2, 122))
    pygame.draw.line(screen, PANEL_BORDER, (sw // 2 - 60, 148), (sw // 2 + 60, 148), 1)

    difficulties = [
        (
            bouton.facile_bt,
            bouton.facile_txt,
            parametres.facile_clicked,
            (72, 199, 142),
        ),
        (bouton.moyen_bt, bouton.moyen_txt, parametres.moyen_clicked, (250, 204, 21)),
        (
            bouton.difficile_bt,
            bouton.difficile_txt,
            parametres.difficile_clicked,
            (252, 129, 74),
        ),
    ]

    btn_w, btn_h = 240, 50
    btn_x = sw // 2 - btn_w // 2

    for i, (rect, txt, clicked, color) in enumerate(difficulties):
        by = 175 + i * 70
        rect.x, rect.y = btn_x, by
        rect.width, rect.height = btn_w, btn_h
        btn_rect = pygame.Rect(btn_x, by, btn_w, btn_h)

        if clicked:
            pygame.draw.rect(screen, color, btn_rect, border_radius=6)
            lbl = font_btn.render(txt, True, BG_COLOR)
        else:
            pygame.draw.rect(screen, CARD_BG, btn_rect, border_radius=6)
            pygame.draw.rect(screen, color, btn_rect, width=1, border_radius=6)
            lbl = font_btn.render(txt, True, color)

        screen.blit(
            lbl,
            (
                btn_x + (btn_w - lbl.get_width()) // 2,
                by + (btn_h - lbl.get_height()) // 2,
            ),
        )

    exit_rect = pygame.Rect(12, 12, 70, 32)
    bouton.exit_bt.x, bouton.exit_bt.y = 12, 12
    bouton.exit_bt.width, bouton.exit_bt.height = 70, 32
    pygame.draw.rect(screen, CARD_BG, exit_rect, border_radius=4)
    pygame.draw.rect(screen, PANEL_BORDER, exit_rect, width=1, border_radius=4)
    exit_lbl = font_label.render("EXIT", True, TEXT_MUTED)
    screen.blit(
        exit_lbl,
        (12 + (70 - exit_lbl.get_width()) // 2, 12 + (32 - exit_lbl.get_height()) // 2),
    )


# ── RULES ─────────────────────────────────────────────────────────────────────
def rules(screen):
    BG_COLOR = (13, 16, 23)
    PANEL_BORDER = (40, 46, 60)
    CARD_BG = (24, 28, 38)
    TEXT_MAIN = (230, 235, 245)
    TEXT_MUTED = (110, 120, 145)
    ACCENT = (99, 179, 237)

    sw, sh = screen.get_width(), screen.get_height()
    screen.fill(BG_COLOR)

    font_head = pygame.font.SysFont("Courier New", 30, bold=True)
    font_body = pygame.font.SysFont("Courier New", 16)
    font_label = pygame.font.SysFont("Courier New", 15)

    title_surf = font_head.render("RÈGLES", True, TEXT_MAIN)
    screen.blit(title_surf, (sw // 2 - title_surf.get_width() // 2, 80))
    pygame.draw.line(screen, ACCENT, (sw // 2 - 40, 122), (sw // 2 + 40, 122), 1)

    rules_lines = [
        (
            "DÉPLACEMENT",
            ACCENT,
            "Utilise les touches fléchées pour te déplacer sur la grille.",
        ),
        (
            "COMBAT",
            ACCENT,
            "Approche un ennemi pour déclencher un combat au tour par tour.",
        ),
        ("ATTAQUE", ACCENT, "Choisis d'attaquer ou de te soigner à chaque tour."),
        (
            "NIVEAU",
            ACCENT,
            "Battre des ennemis donne de l'XP pour évoluer.",
        ),
        ("MORT", (252, 129, 74), "Si ta vie tombe à 0, la partie est terminée."),
    ]

    card_w = min(580, sw - 120)
    card_x = sw // 2 - card_w // 2
    cy = 144

    for heading, h_color, body in rules_lines:
        card_h = 70
        card_rect = pygame.Rect(card_x, cy, card_w, card_h)
        pygame.draw.rect(screen, CARD_BG, card_rect, border_radius=6)
        pygame.draw.rect(screen, PANEL_BORDER, card_rect, width=1, border_radius=6)
        pygame.draw.rect(
            screen, h_color, (card_x, cy + 8, 3, card_h - 16), border_radius=2
        )

        h_surf = font_body.render(heading, True, h_color)
        screen.blit(h_surf, (card_x + 18, cy + 10))

        b_surf = font_label.render(body, True, TEXT_MUTED)
        screen.blit(b_surf, (card_x + 18, cy + 36))
        cy += 82

    exit_rect = pygame.Rect(12, 12, 70, 32)
    bouton.exit_bt.x, bouton.exit_bt.y = 12, 12
    bouton.exit_bt.width, bouton.exit_bt.height = 70, 32
    pygame.draw.rect(screen, CARD_BG, exit_rect, border_radius=4)
    pygame.draw.rect(screen, PANEL_BORDER, exit_rect, width=1, border_radius=4)
    exit_lbl = font_label.render("EXIT", True, TEXT_MUTED)
    screen.blit(
        exit_lbl,
        (12 + (70 - exit_lbl.get_width()) // 2, 12 + (32 - exit_lbl.get_height()) // 2),
    )


# ── COMBAT ────────────────────────────────────────────────────────────────────
def combat(screen):
    BG_COLOR = (13, 16, 23)
    PANEL_BORDER = (40, 46, 60)
    CARD_BG = (24, 28, 38)
    TEXT_MAIN = (230, 235, 245)
    TEXT_MUTED = (110, 120, 145)
    ACCENT = (99, 179, 237)
    HP_COLOR = (72, 199, 142)
    ARMOR_COLOR = (99, 179, 237)
    DANGER = (252, 129, 74)
    BTN_ATTACK = (220, 60, 60)
    BTN_HEAL = (72, 199, 142)

    sw, sh = screen.get_width(), screen.get_height()
    screen.fill(BG_COLOR)

    font_label = pygame.font.SysFont("Courier New", 15)
    font_small = pygame.font.SysFont("Courier New", 16, bold=True)
    font_name = pygame.font.SysFont("Courier New", 24, bold=True)
    font_btn = pygame.font.SysFont("Courier New", 18, bold=True)
    font_turn = pygame.font.SysFont("Courier New", 15)

    cx = sw // 2
    cy_center = sh // 2

    # Badge de tour
    is_joueur = parametres.tour_de == "joueur"
    tour_txt = "▶  TON TOUR" if is_joueur else "▶  TOUR ENNEMI"
    tour_col = ACCENT if is_joueur else DANGER
    badge_w, badge_h = 220, 34
    badge_rect = pygame.Rect(cx - badge_w // 2, 18, badge_w, badge_h)
    pygame.draw.rect(screen, CARD_BG, badge_rect, border_radius=17)
    pygame.draw.rect(screen, tour_col, badge_rect, width=1, border_radius=17)
    tour_surf = font_turn.render(tour_txt, True, tour_col)
    screen.blit(
        tour_surf,
        (cx - tour_surf.get_width() // 2, 18 + (badge_h - tour_surf.get_height()) // 2),
    )

    # Ligne VS centrale
    pygame.draw.line(screen, PANEL_BORDER, (cx, 80), (cx, sh - 80), 1)
    vs_surf = font_small.render("VS", True, TEXT_MUTED)
    vs_bg = pygame.Rect(cx - 20, cy_center - 16, 40, 32)
    pygame.draw.rect(screen, BG_COLOR, vs_bg)
    screen.blit(
        vs_surf, (cx - vs_surf.get_width() // 2, cy_center - vs_surf.get_height() // 2)
    )

    def draw_fighter(label, life, max_life, armor, max_armor, side):
        card_w = sw // 2 - 80
        card_x = 40 if side == -1 else cx + 40
        card_y = cy_center - 150

        name_surf = font_name.render(label, True, TEXT_MAIN)
        screen.blit(name_surf, (card_x, card_y))
        card_y += 44

        _draw_stat_card(
            screen,
            card_x,
            card_y,
            card_w,
            52,
            "VIE",
            life,
            max_life,
            HP_COLOR,
            font_small,
            font_label,
        )
        card_y += 64

        if side == -1:
            _draw_stat_card(
                screen,
                card_x,
                card_y,
                card_w,
                52,
                "ARMURE",
                armor,
                max_armor,
                ARMOR_COLOR,
                font_small,
                font_label,
            )

    draw_fighter(
        "JOUEUR",
        entities.j1.life,
        entities.j1.max_life,
        entities.j1.armor,
        entities.j1.max_armor,
        side=-1,
    )
    draw_fighter(
        "ENNEMI",
        entities.ennemi_en_combat.life,
        entities.ennemi_en_combat.max_life,
        0,
        1,
        side=1,
    )

    # Boutons d'action
    btn_w, btn_h = 180, 50
    spacing = 20
    total_w = btn_w * 2 + spacing
    b1_x = cx - total_w // 2
    b2_x = b1_x + btn_w + spacing
    by = sh - 160

    bouton.attaquer_bt.x, bouton.attaquer_bt.y = b1_x, by
    bouton.attaquer_bt.width, bouton.attaquer_bt.height = btn_w, btn_h
    atk_rect = pygame.Rect(b1_x, by, btn_w, btn_h)
    pygame.draw.rect(screen, BTN_ATTACK, atk_rect, border_radius=6)
    atk_surf = font_btn.render(bouton.attaquer_txt, True, TEXT_MAIN)
    screen.blit(
        atk_surf,
        (
            b1_x + (btn_w - atk_surf.get_width()) // 2,
            by + (btn_h - atk_surf.get_height()) // 2,
        ),
    )

    bouton.soin_bt.x, bouton.soin_bt.y = b2_x, by
    bouton.soin_bt.width, bouton.soin_bt.height = btn_w, btn_h
    heal_rect = pygame.Rect(b2_x, by, btn_w, btn_h)
    pygame.draw.rect(screen, CARD_BG, heal_rect, border_radius=6)
    pygame.draw.rect(screen, BTN_HEAL, heal_rect, width=1, border_radius=6)
    heal_surf = font_btn.render(bouton.soin_txt, True, BTN_HEAL)
    screen.blit(
        heal_surf,
        (
            b2_x + (btn_w - heal_surf.get_width()) // 2,
            by + (btn_h - heal_surf.get_height()) // 2,
        ),
    )

    # Inventaire
    inv_surf = font_label.render(
        f"Inventaire : {str(entities.j1.inventaire)}", True, TEXT_MUTED
    )
    screen.blit(inv_surf, (cx - inv_surf.get_width() // 2, sh - 50))

    # Exit
    exit_rect = pygame.Rect(12, 12, 70, 32)
    bouton.exit_bt.x, bouton.exit_bt.y = 12, 12
    bouton.exit_bt.width, bouton.exit_bt.height = 70, 32
    pygame.draw.rect(screen, CARD_BG, exit_rect, border_radius=4)
    pygame.draw.rect(screen, PANEL_BORDER, exit_rect, width=1, border_radius=4)
    exit_lbl = font_label.render("EXIT", True, TEXT_MUTED)
    screen.blit(
        exit_lbl,
        (12 + (70 - exit_lbl.get_width()) // 2, 12 + (32 - exit_lbl.get_height()) // 2),
    )


# ── MORT ──────────────────────────────────────────────────────────────────────
def mort(screen):
    BG_COLOR = (13, 16, 23)
    PANEL_BORDER = (40, 46, 60)
    CARD_BG = (24, 28, 38)
    TEXT_MUTED = (110, 120, 145)
    DANGER = (220, 60, 60)

    sw, sh = screen.get_width(), screen.get_height()
    screen.fill(BG_COLOR)

    font_big = pygame.font.SysFont("Courier New", 64, bold=True)
    font_sub = pygame.font.SysFont("Courier New", 16)
    font_label = pygame.font.SysFont("Courier New", 15)

    dead_surf = font_big.render("VOUS ÊTES MORT", True, DANGER)
    screen.blit(dead_surf, (sw // 2 - dead_surf.get_width() // 2, sh // 2 - 80))

    pygame.draw.line(
        screen, DANGER, (sw // 2 - 100, sh // 2 + 16), (sw // 2 + 100, sh // 2 + 16), 1
    )

    sub_surf = font_sub.render("ta partie est terminée", True, TEXT_MUTED)
    screen.blit(sub_surf, (sw // 2 - sub_surf.get_width() // 2, sh // 2 + 32))

    exit_rect = pygame.Rect(12, 12, 70, 32)
    bouton.exit_bt.x, bouton.exit_bt.y = 12, 12
    bouton.exit_bt.width, bouton.exit_bt.height = 70, 32
    pygame.draw.rect(screen, CARD_BG, exit_rect, border_radius=4)
    pygame.draw.rect(screen, PANEL_BORDER, exit_rect, width=1, border_radius=4)
    exit_lbl = font_label.render("EXIT", True, TEXT_MUTED)
    screen.blit(
        exit_lbl,
        (12 + (70 - exit_lbl.get_width()) // 2, 12 + (32 - exit_lbl.get_height()) // 2),
    )


# ── NIVEAU ────────────────────────────────────────────────────────────────────
def niveau(screen):
    BG_COLOR = (13, 16, 23)
    PANEL_BORDER = (40, 46, 60)
    CARD_BG = (24, 28, 38)
    TEXT_MAIN = (230, 235, 245)
    TEXT_MUTED = (110, 120, 145)
    ACCENT = (99, 179, 237)
    XP_COLOR = (250, 204, 21)

    sw, sh = screen.get_width(), screen.get_height()
    screen.fill(BG_COLOR)

    font_head = pygame.font.SysFont("Courier New", 30, bold=True)
    font_sub = pygame.font.SysFont("Courier New", 16)
    font_btn = pygame.font.SysFont("Courier New", 16, bold=True)
    font_desc = pygame.font.SysFont("Courier New", 14)
    font_label = pygame.font.SysFont("Courier New", 15)

    title_surf = font_head.render("NIVEAU SUPÉRIEUR !", True, XP_COLOR)
    screen.blit(title_surf, (sw // 2 - title_surf.get_width() // 2, 70))
    sub_surf = font_sub.render("Choisis une récompense", True, TEXT_MUTED)
    screen.blit(sub_surf, (sw // 2 - sub_surf.get_width() // 2, 112))
    pygame.draw.line(screen, XP_COLOR, (sw // 2 - 60, 138), (sw // 2 + 60, 138), 1)

    rewards = [
        (
            bouton.more_force_bt,
            bouton.more_force_txt,
            "Augmente ton attaque",
            (252, 129, 74),
        ),
        (
            bouton.more_deplacement_bt,
            bouton.more_deplacement_txt,
            "+1 déplacement par tour",
            ACCENT,
        ),
        (
            bouton.more_life_bt,
            bouton.more_life_txt,
            "Augmente ta vie maximale",
            (72, 199, 142),
        ),
    ]

    card_w = 200
    spacing = 30
    total_w = len(rewards) * card_w + (len(rewards) - 1) * spacing
    start_x = sw // 2 - total_w // 2
    card_h = 160
    card_y = sh // 2 - card_h // 2 + 20

    for i, (rect, txt, desc, color) in enumerate(rewards):
        cx_card = start_x + i * (card_w + spacing)

        rect.x, rect.y = cx_card, card_y
        rect.width, rect.height = card_w, card_h

        card_rect = pygame.Rect(cx_card, card_y, card_w, card_h)
        pygame.draw.rect(screen, CARD_BG, card_rect, border_radius=8)
        pygame.draw.rect(screen, color, card_rect, width=1, border_radius=8)
        pygame.draw.rect(screen, color, (cx_card, card_y, card_w, 4), border_radius=8)

        btn_surf = font_btn.render(txt, True, color)
        screen.blit(
            btn_surf, (cx_card + card_w // 2 - btn_surf.get_width() // 2, card_y + 22)
        )

        desc_surf = font_desc.render(desc, True, TEXT_MUTED)
        screen.blit(
            desc_surf, (cx_card + card_w // 2 - desc_surf.get_width() // 2, card_y + 52)
        )

        pygame.draw.line(
            screen,
            PANEL_BORDER,
            (cx_card + 16, card_y + 80),
            (cx_card + card_w - 16, card_y + 80),
            1,
        )

        pick_surf = font_label.render("[ CHOISIR ]", True, color)
        screen.blit(
            pick_surf, (cx_card + card_w // 2 - pick_surf.get_width() // 2, card_y + 96)
        )

    exit_rect = pygame.Rect(12, 12, 70, 32)
    bouton.exit_bt.x, bouton.exit_bt.y = 12, 12
    bouton.exit_bt.width, bouton.exit_bt.height = 70, 32
    pygame.draw.rect(screen, CARD_BG, exit_rect, border_radius=4)
    pygame.draw.rect(screen, PANEL_BORDER, exit_rect, width=1, border_radius=4)
    exit_lbl = font_label.render("EXIT", True, TEXT_MUTED)
    screen.blit(
        exit_lbl,
        (12 + (70 - exit_lbl.get_width()) // 2, 12 + (32 - exit_lbl.get_height()) // 2),
    )
