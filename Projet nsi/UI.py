import pygame
import parametres
import bouton
import fonction
import entities
from parametres import xbouton, ybouton, largeur_bouton, hauteur_bouton, taille_cell

screen = parametres.ecran


# UI Menu
def menu(screen):
    # ── Palette ──────────────────────────────────────────────────
    BG_COLOR = (13, 16, 23)
    PANEL_BG = (15, 17, 23)
    PANEL_BORDER = (40, 46, 60)
    CARD_BG = (24, 28, 38)
    TEXT_MAIN = (230, 235, 245)
    TEXT_MUTED = (110, 120, 145)
    ACCENT = (99, 179, 237)

    sw, sh = screen.get_width(), screen.get_height()
    screen.fill(BG_COLOR)

    font_title = pygame.font.SysFont("Courier New", 42, bold=True)
    font_sub = pygame.font.SysFont("Courier New", 13)
    font_btn = pygame.font.SysFont("Courier New", 15, bold=True)

    # ── Titre ────────────────────────────────────────────────────
    title_surf = font_title.render("DUNGEON", True, TEXT_MAIN)
    sub_surf = font_sub.render(
        "v0.1  —  un jeu de rôle au tour par tour", True, TEXT_MUTED
    )
    screen.blit(title_surf, (sw // 2 - title_surf.get_width() // 2, sh // 2 - 200))
    screen.blit(sub_surf, (sw // 2 - sub_surf.get_width() // 2, sh // 2 - 148))

    # Ligne décorative sous le titre
    line_w = 120
    pygame.draw.line(
        screen,
        ACCENT,
        (sw // 2 - line_w // 2, sh // 2 - 128),
        (sw // 2 + line_w // 2, sh // 2 - 128),
        1,
    )

    # ── Boutons ──────────────────────────────────────────────────
    btn_w, btn_h = 220, 44
    btn_x = sw // 2 - btn_w // 2
    buttons = [
        (bouton.Jouer_bt, bouton.Jouer_txt, ACCENT, True),  # bouton principal accentué
        (bouton.parametre_bt, bouton.parametre_txt, CARD_BG, False),
        (bouton.rules_bt, bouton.rules_txt, CARD_BG, False),
    ]

    for i, (rect, txt, bg, is_primary) in enumerate(buttons):
        by = sh // 2 - 80 + i * 58
        btn_rect = pygame.Rect(btn_x, by, btn_w, btn_h)

        # Remplace le rect du bouton original pour que les clics fonctionnent
        rect.x, rect.y = btn_x, by
        rect.width, rect.height = btn_w, btn_h

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

    # ── Exit coin haut gauche ─────────────────────────────────────
    exit_rect = pygame.Rect(12, 12, 60, 28)
    bouton.exit_bt.x, bouton.exit_bt.y = 12, 12
    bouton.exit_bt.width, bouton.exit_bt.height = 60, 28
    pygame.draw.rect(screen, CARD_BG, exit_rect, border_radius=4)
    pygame.draw.rect(screen, PANEL_BORDER, exit_rect, width=1, border_radius=4)
    exit_lbl = font_sub.render("EXIT", True, TEXT_MUTED)
    screen.blit(
        exit_lbl,
        (12 + (60 - exit_lbl.get_width()) // 2, 12 + (28 - exit_lbl.get_height()) // 2),
    )


# UI PLay
def play(screen, grille_jeu, joueur):
    # ── Palette ──────────────────────────────────────────────────
    BG_COLOR = (13, 16, 23)
    PANEL_BG = (15, 17, 23)
    PANEL_BORDER = (40, 46, 60)
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

    # ── Fond ─────────────────────────────────────────────────────
    screen.fill(BG_COLOR)

    # ── Panneau latéral droit ────────────────────────────────────
    panel_w = 210
    panel_x = sw - panel_w - 16
    panel_rect = pygame.Rect(panel_x - 8, 0, panel_w + 24, sh)
    pygame.draw.rect(screen, PANEL_BG, panel_rect)
    pygame.draw.line(screen, PANEL_BORDER, (panel_x - 8, 0), (panel_x - 8, sh), 1)

    font_title = pygame.font.SysFont("Courier New", 13, bold=True)
    font_label = pygame.font.SysFont("Courier New", 11)
    font_small = pygame.font.SysFont("Courier New", 12, bold=True)
    font_value = pygame.font.SysFont("Courier New", 22, bold=True)

    # — Titre panneau —
    title_surf = font_title.render("JOUEUR", True, TEXT_MUTED)
    screen.blit(title_surf, (panel_x + (panel_w - title_surf.get_width()) // 2, 18))
    pygame.draw.line(screen, PANEL_BORDER, (panel_x, 36), (panel_x + panel_w, 36), 1)

    cy = 50  # curseur vertical

    # — Niveau (grand) —
    niv_label = font_label.render("NIVEAU", True, TEXT_MUTED)
    screen.blit(niv_label, (panel_x + 10, cy))
    niv_val = font_value.render(str(entities.j1.niveau), True, ACCENT)
    screen.blit(niv_val, (panel_x + panel_w - niv_val.get_width() - 10, cy - 4))
    cy += 28

    # — XP —
    fonction._draw_stat_card(
        screen,
        panel_x,
        cy,
        panel_w,
        48,
        "XP",
        entities.j1.xp,
        10,
        XP_COLOR,
        font_small,
        font_label,
    )
    cy += 58

    # — Vie —
    fonction._draw_stat_card(
        screen,
        panel_x,
        cy,
        panel_w,
        48,
        "VIE",
        entities.j1.life,
        entities.j1.max_life,
        HP_COLOR,
        font_small,
        font_label,
    )
    cy += 58

    # — Armure —
    fonction._draw_stat_card(
        screen,
        panel_x,
        cy,
        panel_w,
        48,
        "ARMURE",
        entities.j1.armor,
        entities.j1.max_armor,
        ARMOR_COLOR,
        font_small,
        font_label,
    )
    cy += 68

    # — Déplacements restants —
    pygame.draw.line(
        screen, PANEL_BORDER, (panel_x, cy - 6), (panel_x + panel_w, cy - 6), 1
    )
    dep_label = font_label.render("DÉPLACEMENTS", True, TEXT_MUTED)
    screen.blit(dep_label, (panel_x + 10, cy))
    cy += 18
    deps = getattr(
        parametres, "deplacement_joueur_restants", parametres.deplacement_joueur_max
    )
    dep_val = font_value.render(str(deps), True, TEXT_MAIN)
    screen.blit(dep_val, (panel_x + (panel_w - dep_val.get_width()) // 2, cy))
    cy += 40

    # — Tour actuel (badge coloré) —
    pygame.draw.line(screen, PANEL_BORDER, (panel_x, cy), (panel_x + panel_w, cy), 1)
    cy += 12
    is_joueur = parametres.tour_deplacement == "joueur"
    badge_color = TURN_JOUEUR if is_joueur else TURN_MOB
    badge_txt = "TON TOUR" if is_joueur else "TOUR ENNEMI"
    badge_rect = pygame.Rect(panel_x + 10, cy, panel_w - 20, 28)
    pygame.draw.rect(
        screen, (*badge_color, 40), badge_rect, border_radius=5
    )  # semi-transparent simulé
    pygame.draw.rect(screen, badge_color, badge_rect, width=1, border_radius=5)
    badge_surf = font_label.render(badge_txt, True, badge_color)
    screen.blit(
        badge_surf,
        (
            panel_x + (panel_w - badge_surf.get_width()) // 2,
            cy + (28 - badge_surf.get_height()) // 2,
        ),
    )

    # ── Grille ───────────────────────────────────────────────────
    grille_size = parametres.taille_grille * taille_cell
    grid_x = (sw - panel_w - 24 - grille_size) // 2
    grid_y = (sh - grille_size) // 2

    # Fond grille
    pygame.draw.rect(
        screen,
        GRID_BG,
        (grid_x - 2, grid_y - 2, grille_size + 4, grille_size + 4),
        border_radius=4,
    )

    # Re-dessiner la grille avec les nouvelles couleurs
    for (cx_g, cy_g), cell in grille_jeu.items():
        rx = grid_x + cx_g * taille_cell
        ry = grid_y + cy_g * taille_cell
        pygame.draw.rect(screen, GRID_BG, (rx, ry, taille_cell, taille_cell))
        pygame.draw.rect(screen, GRID_LINE, (rx, ry, taille_cell, taille_cell), 1)

    # Joueur (carré avec contour accent)
    jx = grid_x + joueur.x * taille_cell + 2
    jy = grid_y + joueur.y * taille_cell + 2
    s = taille_cell - 4
    pygame.draw.rect(screen, ACCENT, (jx, jy, s, s), border_radius=2)
    pygame.draw.rect(screen, TEXT_MAIN, (jx, jy, s, s), width=1, border_radius=2)

    # Entités (cercles)
    for cell in grille_jeu.values():
        if cell.contenu is not None:
            ex = grid_x + cell.x * taille_cell + taille_cell // 2
            ey = grid_y + cell.y * taille_cell + taille_cell // 2
            r = taille_cell // 2 - 2
            pygame.draw.circle(screen, cell.contenu.couleur, (ex, ey), r)
            pygame.draw.circle(screen, (0, 0, 0), (ex, ey), r, 1)

    # ── Bouton exit (en haut à gauche, style sobre) ──────────────
    exit_rect = pygame.Rect(12, 12, 60, 28)
    pygame.draw.rect(screen, PANEL_BG, exit_rect, border_radius=4)
    pygame.draw.rect(screen, PANEL_BORDER, exit_rect, width=1, border_radius=4)
    exit_surf = font_label.render("EXIT", True, TEXT_MUTED)
    screen.blit(
        exit_surf,
        (
            12 + (60 - exit_surf.get_width()) // 2,
            12 + (28 - exit_surf.get_height()) // 2,
        ),
    )


# UI Parametre
def parametre(screen):
    BG_COLOR = (13, 16, 23)
    PANEL_BORDER = (40, 46, 60)
    CARD_BG = (24, 28, 38)
    TEXT_MAIN = (230, 235, 245)
    TEXT_MUTED = (110, 120, 145)
    ACCENT = (99, 179, 237)

    sw, sh = screen.get_width(), screen.get_height()
    screen.fill(BG_COLOR)

    font_title = pygame.font.SysFont("Courier New", 13, bold=True)
    font_label = pygame.font.SysFont("Courier New", 11)
    font_btn = pygame.font.SysFont("Courier New", 14, bold=True)
    font_head = pygame.font.SysFont("Courier New", 22, bold=True)

    # ── Titre ────────────────────────────────────────────────────
    title_surf = font_head.render("PARAMÈTRES", True, TEXT_MAIN)
    screen.blit(title_surf, (sw // 2 - title_surf.get_width() // 2, 80))
    sub_surf = font_label.render("Choisir la difficulté", True, TEXT_MUTED)
    screen.blit(sub_surf, (sw // 2 - sub_surf.get_width() // 2, 116))
    pygame.draw.line(screen, PANEL_BORDER, (sw // 2 - 60, 136), (sw // 2 + 60, 136), 1)

    # ── Boutons difficulté ───────────────────────────────────────
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

    btn_w, btn_h = 220, 44
    btn_x = sw // 2 - btn_w // 2

    for i, (rect, txt, clicked, color) in enumerate(difficulties):
        by = 170 + i * 62
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

    # ── Exit ─────────────────────────────────────────────────────
    exit_rect = pygame.Rect(12, 12, 60, 28)
    bouton.exit_bt.x, bouton.exit_bt.y = 12, 12
    bouton.exit_bt.width, bouton.exit_bt.height = 60, 28
    pygame.draw.rect(screen, CARD_BG, exit_rect, border_radius=4)
    pygame.draw.rect(screen, PANEL_BORDER, exit_rect, width=1, border_radius=4)
    exit_lbl = font_label.render("EXIT", True, TEXT_MUTED)
    screen.blit(
        exit_lbl,
        (12 + (60 - exit_lbl.get_width()) // 2, 12 + (28 - exit_lbl.get_height()) // 2),
    )


# UI Rules
def rules(screen):
    BG_COLOR = (13, 16, 23)
    PANEL_BORDER = (40, 46, 60)
    CARD_BG = (24, 28, 38)
    TEXT_MAIN = (230, 235, 245)
    TEXT_MUTED = (110, 120, 145)
    ACCENT = (99, 179, 237)

    sw, sh = screen.get_width(), screen.get_height()
    screen.fill(BG_COLOR)

    font_label = pygame.font.SysFont("Courier New", 11)
    font_head = pygame.font.SysFont("Courier New", 22, bold=True)
    font_body = pygame.font.SysFont("Courier New", 13)

    # ── Titre ────────────────────────────────────────────────────
    title_surf = font_head.render("RÈGLES", True, TEXT_MAIN)
    screen.blit(title_surf, (sw // 2 - title_surf.get_width() // 2, 80))
    pygame.draw.line(screen, ACCENT, (sw // 2 - 40, 114), (sw // 2 + 40, 114), 1)

    # ── Contenu ──────────────────────────────────────────────────
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
            "Battre des ennemis donne de l'XP. Monte de niveau pour progresser.",
        ),
        ("MORT", (252, 129, 74), "Si ta vie tombe à 0, la partie est terminée."),
    ]

    card_w = min(560, sw - 120)
    card_x = sw // 2 - card_w // 2
    cy = 140

    for heading, h_color, body in rules_lines:
        # Carte
        card_h = 62
        card_rect = pygame.Rect(card_x, cy, card_w, card_h)
        pygame.draw.rect(screen, CARD_BG, card_rect, border_radius=6)
        pygame.draw.rect(screen, PANEL_BORDER, card_rect, width=1, border_radius=6)
        # Barre gauche colorée
        pygame.draw.rect(
            screen, h_color, (card_x, cy + 8, 3, card_h - 16), border_radius=2
        )
        # Heading
        h_surf = font_body.render(heading, True, h_color)
        screen.blit(h_surf, (card_x + 16, cy + 10))
        # Body
        b_surf = font_label.render(body, True, TEXT_MUTED)
        screen.blit(b_surf, (card_x + 16, cy + 32))
        cy += 72

    # ── Exit ─────────────────────────────────────────────────────
    exit_rect = pygame.Rect(12, 12, 60, 28)
    bouton.exit_bt.x, bouton.exit_bt.y = 12, 12
    bouton.exit_bt.width, bouton.exit_bt.height = 60, 28
    pygame.draw.rect(screen, CARD_BG, exit_rect, border_radius=4)
    pygame.draw.rect(screen, PANEL_BORDER, exit_rect, width=1, border_radius=4)
    exit_lbl = font_label.render("EXIT", True, TEXT_MUTED)
    screen.blit(
        exit_lbl,
        (12 + (60 - exit_lbl.get_width()) // 2, 12 + (28 - exit_lbl.get_height()) // 2),
    )


def combat(screen):
    # ── Palette ──────────────────────────────────────────────────
    BG_COLOR = (13, 16, 23)
    PANEL_BG = (15, 17, 23)
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

    font_title = pygame.font.SysFont("Courier New", 13, bold=True)
    font_label = pygame.font.SysFont("Courier New", 11)
    font_small = pygame.font.SysFont("Courier New", 12, bold=True)
    font_name = pygame.font.SysFont("Courier New", 18, bold=True)
    font_btn = pygame.font.SysFont("Courier New", 14, bold=True)
    font_turn = pygame.font.SysFont("Courier New", 12)

    cx = sw // 2
    cy_center = sh // 2

    # ── Indicateur de tour en haut au centre ─────────────────────
    is_joueur = parametres.tour_de == "joueur"
    tour_txt = "▶  TON TOUR" if is_joueur else "▶  TOUR ENNEMI"
    tour_col = ACCENT if is_joueur else DANGER
    badge_w, badge_h = 200, 30
    badge_rect = pygame.Rect(cx - badge_w // 2, 16, badge_w, badge_h)
    pygame.draw.rect(screen, CARD_BG, badge_rect, border_radius=15)
    pygame.draw.rect(screen, tour_col, badge_rect, width=1, border_radius=15)
    tour_surf = font_turn.render(tour_txt, True, tour_col)
    screen.blit(
        tour_surf,
        (cx - tour_surf.get_width() // 2, 16 + (badge_h - tour_surf.get_height()) // 2),
    )

    # ── Ligne séparatrice centrale (VS) ──────────────────────────
    pygame.draw.line(screen, PANEL_BORDER, (cx, 80), (cx, sh - 80), 1)
    vs_surf = font_small.render("VS", True, TEXT_MUTED)
    vs_bg = pygame.Rect(cx - 18, cy_center - 14, 36, 28)
    pygame.draw.rect(screen, BG_COLOR, vs_bg)
    screen.blit(
        vs_surf, (cx - vs_surf.get_width() // 2, cy_center - vs_surf.get_height() // 2)
    )

    # ─── Fonction locale pour dessiner une fiche personnage ──────
    def draw_fighter(label, life, max_life, armor, max_armor, side):
        """side = -1 pour gauche (joueur), +1 pour droite (ennemi)"""
        card_w = sw // 2 - 80
        card_x = 40 if side == -1 else cx + 40
        card_y = cy_center - 130

        # Nom / label
        name_surf = font_name.render(label, True, TEXT_MAIN)
        screen.blit(name_surf, (card_x, card_y))
        card_y += 36

        # Barre Vie
        fonction._draw_stat_card(
            screen,
            card_x,
            card_y,
            card_w,
            48,
            "VIE",
            life,
            max_life,
            HP_COLOR,
            font_small,
            font_label,
        )
        card_y += 58

        # Barre Armure (joueur uniquement)
        if side == -1:
            fonction._draw_stat_card(
                screen,
                card_x,
                card_y,
                card_w,
                48,
                "ARMURE",
                armor,
                max_armor,
                ARMOR_COLOR,
                font_small,
                font_label,
            )

    # Joueur (gauche)
    draw_fighter(
        "JOUEUR",
        entities.j1.life,
        entities.j1.max_life,
        entities.j1.armor,
        entities.j1.max_armor,
        side=-1,
    )

    # Ennemi (droite)
    draw_fighter(
        "ENNEMI",
        entities.ennemi_en_combat.life,
        entities.ennemi_en_combat.max_life,
        0,
        1,
        side=1,
    )

    # ── Boutons d'action centrés en bas ──────────────────────────
    btn_w, btn_h = 160, 44
    spacing = 20
    total_w = btn_w * 2 + spacing
    b1_x = cx - total_w // 2
    b2_x = b1_x + btn_w + spacing
    by = sh - 200

    # Attaquer
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

    # Soin
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

    # Inventaire (petit texte discret)
    inv_surf = font_label.render(
        f"Inventaire : {str(entities.j1.inventaire)}", True, TEXT_MUTED
    )
    screen.blit(inv_surf, (cx - inv_surf.get_width() // 2, sh - 46))

    # ── Exit ─────────────────────────────────────────────────────
    exit_rect = pygame.Rect(12, 12, 60, 28)
    bouton.exit_bt.x, bouton.exit_bt.y = 12, 12
    bouton.exit_bt.width, bouton.exit_bt.height = 60, 28
    pygame.draw.rect(screen, CARD_BG, exit_rect, border_radius=4)
    pygame.draw.rect(screen, PANEL_BORDER, exit_rect, width=1, border_radius=4)
    exit_lbl = font_label.render("EXIT", True, TEXT_MUTED)
    screen.blit(
        exit_lbl,
        (12 + (60 - exit_lbl.get_width()) // 2, 12 + (28 - exit_lbl.get_height()) // 2),
    )


# UI Mort
def mort(screen):
    BG_COLOR = (13, 16, 23)
    TEXT_MAIN = (230, 235, 245)
    TEXT_MUTED = (110, 120, 145)
    DANGER = (220, 60, 60)
    CARD_BG = (24, 28, 38)
    PANEL_BORDER = (40, 46, 60)

    sw, sh = screen.get_width(), screen.get_height()
    screen.fill(BG_COLOR)

    font_label = pygame.font.SysFont("Courier New", 11)
    font_big = pygame.font.SysFont("Courier New", 52, bold=True)
    font_sub = pygame.font.SysFont("Courier New", 14)

    # ── Message principal ─────────────────────────────────────────
    dead_surf = font_big.render("VOUS ÊTES MORT", True, DANGER)
    screen.blit(dead_surf, (sw // 2 - dead_surf.get_width() // 2, sh // 2 - 80))

    # Ligne décorative
    pygame.draw.line(
        screen, DANGER, (sw // 2 - 100, sh // 2 + 10), (sw // 2 + 100, sh // 2 + 10), 1
    )

    sub_surf = font_sub.render("ta partie est terminée", True, TEXT_MUTED)
    screen.blit(sub_surf, (sw // 2 - sub_surf.get_width() // 2, sh // 2 + 26))

    # ── Exit ─────────────────────────────────────────────────────
    exit_rect = pygame.Rect(12, 12, 60, 28)
    bouton.exit_bt.x, bouton.exit_bt.y = 12, 12
    bouton.exit_bt.width, bouton.exit_bt.height = 60, 28
    pygame.draw.rect(screen, CARD_BG, exit_rect, border_radius=4)
    pygame.draw.rect(screen, PANEL_BORDER, exit_rect, width=1, border_radius=4)
    exit_lbl = font_label.render("EXIT", True, TEXT_MUTED)
    screen.blit(
        exit_lbl,
        (12 + (60 - exit_lbl.get_width()) // 2, 12 + (28 - exit_lbl.get_height()) // 2),
    )


# UI Niveau
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

    font_label = pygame.font.SysFont("Courier New", 11)
    font_head = pygame.font.SysFont("Courier New", 26, bold=True)
    font_sub = pygame.font.SysFont("Courier New", 13)
    font_btn = pygame.font.SysFont("Courier New", 13, bold=True)
    font_desc = pygame.font.SysFont("Courier New", 11)

    # ── Titre ────────────────────────────────────────────────────
    title_surf = font_head.render("NIVEAU SUPÉRIEUR !", True, XP_COLOR)
    screen.blit(title_surf, (sw // 2 - title_surf.get_width() // 2, 70))
    sub_surf = font_sub.render("Choisis une récompense", True, TEXT_MUTED)
    screen.blit(sub_surf, (sw // 2 - sub_surf.get_width() // 2, 108))
    pygame.draw.line(screen, XP_COLOR, (sw // 2 - 60, 130), (sw // 2 + 60, 130), 1)

    # ── Cartes de récompense ──────────────────────────────────────
    rewards = [
        (
            bouton.more_force_bt,
            bouton.more_force_txt,
            "⚔",
            "Augmente ton attaque",
            (252, 129, 74),
        ),
        (
            bouton.more_deplacement_bt,
            bouton.more_deplacement_txt,
            "👟",
            "+1 déplacement par tour",
            ACCENT,
        ),
        (
            bouton.more_life_bt,
            bouton.more_life_txt,
            "❤",
            "Augmente ta vie maximale",
            (72, 199, 142),
        ),
    ]

    card_w = 180
    spacing = 30
    total_w = len(rewards) * card_w + (len(rewards) - 1) * spacing
    start_x = sw // 2 - total_w // 2
    card_h = 140
    card_y = sh // 2 - card_h // 2 + 20

    for i, (rect, txt, icon, desc, color) in enumerate(rewards):
        cx_card = start_x + i * (card_w + spacing)

        rect.x, rect.y = cx_card, card_y
        rect.width, rect.height = card_w, card_h

        card_rect = pygame.Rect(cx_card, card_y, card_w, card_h)
        pygame.draw.rect(screen, CARD_BG, card_rect, border_radius=8)
        pygame.draw.rect(screen, color, card_rect, width=1, border_radius=8)

        # Barre colorée en haut de la carte
        pygame.draw.rect(screen, color, (cx_card, card_y, card_w, 4), border_radius=8)

        # Titre bouton
        btn_surf = font_btn.render(txt, True, color)
        screen.blit(
            btn_surf, (cx_card + card_w // 2 - btn_surf.get_width() // 2, card_y + 20)
        )

        # Description
        desc_surf = font_desc.render(desc, True, TEXT_MUTED)
        screen.blit(
            desc_surf, (cx_card + card_w // 2 - desc_surf.get_width() // 2, card_y + 46)
        )

        # Ligne séparatrice
        pygame.draw.line(
            screen,
            PANEL_BORDER,
            (cx_card + 16, card_y + 68),
            (cx_card + card_w - 16, card_y + 68),
            1,
        )

        # Texte "Choisir"
        pick_surf = font_label.render("[ CHOISIR ]", True, color)
        screen.blit(
            pick_surf, (cx_card + card_w // 2 - pick_surf.get_width() // 2, card_y + 82)
        )

    # ── Exit ─────────────────────────────────────────────────────
    exit_rect = pygame.Rect(12, 12, 60, 28)
    bouton.exit_bt.x, bouton.exit_bt.y = 12, 12
    bouton.exit_bt.width, bouton.exit_bt.height = 60, 28
    pygame.draw.rect(screen, CARD_BG, exit_rect, border_radius=4)
    pygame.draw.rect(screen, PANEL_BORDER, exit_rect, width=1, border_radius=4)
    exit_lbl = font_label.render("EXIT", True, TEXT_MUTED)
    screen.blit(
        exit_lbl,
        (12 + (60 - exit_lbl.get_width()) // 2, 12 + (28 - exit_lbl.get_height()) // 2),
    )
