import pygame
import random
from .board import Board
from .ui.panel import Panel
from .constants import *


class Game:

    def __init__(self):

        self.board = Board()
        self.panel = Panel()

        self.turn = "white"

        self.selected = None
        self.valid_moves = []
        # --------------------------
        # Menu Settings
        # --------------------------

        self.in_menu = True

        self.game_mode = "pvp"

        self.theme_name = "classic"

    def update(self):
        # AI only plays in Player vs Computer mode
        if self.game_mode != "ai":
            return

        if self.turn != "black":
            return

        all_moves = self.board.get_all_moves("black")

        if len(all_moves) == 0:
            return

        legal_moves = [

            (start, move)

            for start, move in all_moves

            if 0 <= move.row < 8
            and 0 <= move.col < 8

        ]

        if not legal_moves:
            return

        start, move = random.choice(legal_moves)

        self.board.move_piece(
            start,
            (move.row, move.col)
        )

        self.turn = "white"

    def draw(self, screen):

        self.board.draw(screen, self.selected, self.valid_moves)

        self.panel.draw(screen, self.turn,self.board.move_history)

    def handle_event(self, event):

        # ------------------------
        # MENU EVENTS
        # ------------------------

        if self.in_menu:

            if event.type != pygame.MOUSEBUTTONDOWN:
                return

            x, y = event.pos

            # -------------------------
            # Player vs Player
            # -------------------------

            if (
                90 <= x <= 350 and
                225 <= y <= 283
            ):

                self.game_mode = "pvp"

            # -------------------------
            # Player vs Computer
            # -------------------------

            elif (
                90 <= x <= 350 and
                305 <= y <= 363
            ):

                self.game_mode = "ai"

            # -------------------------
            # Classic Theme
            # -------------------------

            elif (
                WIDTH - 330 <= x <= WIDTH - 110 and
                225 <= y <= 283
            ):

                self.theme_name = "classic"

            # -------------------------
            # Dark Theme
            # -------------------------

            elif (
                WIDTH - 330 <= x <= WIDTH - 110 and
                305 <= y <= 363
            ):

                self.theme_name = "dark"

            # -------------------------
            # Start Game
            # -------------------------

            elif (
                WIDTH//2 - 170 <= x <= WIDTH//2 + 170 and
                500 <= y <= 572
            ):

                self.board.set_theme(self.theme_name)

                self.turn = "white"
                self.selected = None
                self.valid_moves = []

                self.in_menu = False

            return

        if event.type != pygame.MOUSEBUTTONDOWN:
            return

        x, y = event.pos

        if x >= BOARD_SIZE:
            return

        row = y // SQUARE_SIZE
        col = x // SQUARE_SIZE

        # ----------------------------
        # Move selected piece
        # ----------------------------

        if self.selected:

            clicked_move = None

            for move in self.valid_moves:

                if move.row == row and move.col == col:
                    clicked_move = move
                    break

            if clicked_move:

                self.board.move_piece(
                    self.selected,
                    (row, col),
                )

                self.turn = (
                    "black"
                    if self.turn == "white"
                    else "white"
                )

                self.selected = None
                self.valid_moves = []

                return

        # ----------------------------
        # Select another piece
        # ----------------------------

        piece = self.board.get_piece(row, col)

        if piece is None:

            self.selected = None
            self.valid_moves = []

            return

        if piece.color != self.turn:
            return

        self.selected = (row, col)

        self.valid_moves = piece.get_valid_moves(
            self.board,
            row,
            col,
        )
    def draw_menu(self, screen):

        screen.fill((28, 28, 32))

        # Fonts
        title_font = pygame.font.SysFont("Segoe UI", 46, bold=True)
        subtitle_font = pygame.font.SysFont("Segoe UI", 18)
        heading_font = pygame.font.SysFont("Segoe UI", 30, bold=True)
        button_font = pygame.font.SysFont("Segoe UI", 22)
        footer_font = pygame.font.SysFont("Segoe UI", 16)

        # ==========================
        # Title
        # ==========================

        title = title_font.render(
            "Python Chess",
            True,
            (245, 245, 245)
        )

        screen.blit(
            title,
            (
                WIDTH // 2 - title.get_width() // 2,
                35
            )
        )

        subtitle = subtitle_font.render(
            "Play Chess • Player vs Player • Easy AI",
            True,
            (170, 170, 170)
        )

        screen.blit(
            subtitle,
            (
                WIDTH // 2 - subtitle.get_width() // 2,
                88
            )
        )

        # ==========================
        # Layout
        # ==========================

        LEFT_X = 90
        RIGHT_X = WIDTH - 330

        TOP_Y = 170

        BUTTON_W = 260
        BUTTON_H = 58
        GAP = 22

        # ==========================
        # Left Panel
        # ==========================

        txt = heading_font.render(
            "Game Mode",
            True,
            (235, 235, 235)
        )

        screen.blit(txt, (LEFT_X, TOP_Y))

        pvp_color = (
            (46, 170, 80)
            if self.game_mode == "pvp"
            else
            (75, 75, 90)
        )

        pygame.draw.rect(
            screen,
            pvp_color,
            (
                LEFT_X,
                TOP_Y + 55,
                BUTTON_W,
                BUTTON_H
            ),
            border_radius=14
        )

        txt = button_font.render(
            "Player vs Player",
            True,
            (255, 255, 255)
        )

        screen.blit(
            txt,
            (
                LEFT_X + BUTTON_W // 2 - txt.get_width() // 2,
                TOP_Y + 72
            )
        )

        pvc_color = (
            (46, 170, 80)
            if self.game_mode == "ai"
            else
            (75, 75, 90)
        )

        pygame.draw.rect(
            screen,
            pvc_color,
            (
                LEFT_X,
                TOP_Y + 55 + BUTTON_H + GAP,
                BUTTON_W,
                BUTTON_H
            ),
            border_radius=14
        )

        txt = button_font.render(
            "Player vs Computer",
            True,
            (255, 255, 255)
        )

        screen.blit(
            txt,
            (
                LEFT_X + BUTTON_W // 2 - txt.get_width() // 2,
                TOP_Y + 72 + BUTTON_H + GAP
            )
        )

        # ==========================
        # Right Panel
        # ==========================

        txt = heading_font.render(
            "Board Theme",
            True,
            (235, 235, 235)
        )

        screen.blit(txt, (RIGHT_X, TOP_Y))

        classic_color = (
            (46, 170, 80)
            if self.theme_name == "classic"
            else
            (75, 75, 90)
        )

        pygame.draw.rect(
            screen,
            classic_color,
            (
                RIGHT_X,
                TOP_Y + 55,
                220,
                BUTTON_H
            ),
            border_radius=14
        )

        txt = button_font.render(
            "Classic",
            True,
            (255, 255, 255)
        )

        screen.blit(
            txt,
            (
                RIGHT_X + 110 - txt.get_width() // 2,
                TOP_Y + 72
            )
        )

        dark_color = (
            (46, 170, 80)
            if self.theme_name == "dark"
            else
            (75, 75, 90)
        )

        pygame.draw.rect(
            screen,
            dark_color,
            (
                RIGHT_X,
                TOP_Y + 55 + BUTTON_H + GAP,
                220,
                BUTTON_H
            ),
            border_radius=14
        )

        txt = button_font.render(
            "Dark",
            True,
            (255, 255, 255)
        )

        screen.blit(
            txt,
            (
                RIGHT_X + 110 - txt.get_width() // 2,
                TOP_Y + 72 + BUTTON_H + GAP
            )
        )

        # ==========================
        # Start Button
        # ==========================

        START_W = 340
        START_H = 72

        pygame.draw.rect(
            screen,
            (50, 180, 90),
            (
                WIDTH // 2 - START_W // 2,
                500,
                START_W,
                START_H
            ),
            border_radius=18
        )

        txt = heading_font.render(
            "START GAME",
            True,
            (255, 255, 255)
        )

        screen.blit(
            txt,
            (
                WIDTH // 2 - txt.get_width() // 2,
                522
            )
        )

        # ==========================
        # Footer
        # ==========================

        footer = footer_font.render(
            "Developed by Raj Chouhan",
            True,
            (110, 110, 110)
        )

        screen.blit(
            footer,
            (
                WIDTH // 2 - footer.get_width() // 2,
                HEIGHT - 28
            )
        )