import pygame

from src.constants import *


class Panel:
    def __init__(self):

        self.title_font = pygame.font.SysFont("Segoe UI", 34, bold=True)
        self.heading_font = pygame.font.SysFont("Segoe UI", 22, bold=True)
        self.text_font = pygame.font.SysFont("Segoe UI", 18)

        self.padding = 20
        self.card_width = SIDE_PANEL - (self.padding * 1.5)
        self.card_radius = 12

    def draw_card(self, screen, y, height, title):

        x = BOARD_SIZE + self.padding

        pygame.draw.rect(
            screen,
            (48, 48, 48),
            (x, y, self.card_width, height),
            border_radius=self.card_radius,
        )

        pygame.draw.rect(
            screen,
            (75, 75, 75),
            (x, y, self.card_width, height),
            width=2,
            border_radius=self.card_radius,
        )

        text = self.heading_font.render(title, True, (240, 240, 240))
        screen.blit(text, (x + 15, y + 12))

    def draw(self, screen, turn, move_history):

        # Background
        pygame.draw.rect(
            screen,
            (32, 32, 32),
            (BOARD_SIZE, 0, SIDE_PANEL, HEIGHT),
        )

        # Title
        title = self.title_font.render("Python Chess", True, (255, 255, 255))
        screen.blit(title, (BOARD_SIZE + 20, 20))

        # Turn Card
        self.draw_card(screen, 90, 70, "Current Turn")

        turn_color = (120, 255, 120) if turn == "white" else (255, 180, 120)

        turn_text = self.text_font.render(
            turn.capitalize(),
            True,
            turn_color,
        )

        screen.blit(
            turn_text,
            (BOARD_SIZE + 35, 130),
        )

        # Move History Card
        self.draw_card(screen, 190, 220, "Move History")
        y = 235

        if len(move_history) == 0:

            text = self.text_font.render(
                "No moves yet",
                True,
                (180,180,180)
            )

            screen.blit(
                text,
                (BOARD_SIZE + 35, y)
            )

        else:

            # Show only the last 8 moves
            recent_moves = move_history[-6:]

            for index, move in enumerate(recent_moves):

                start = (
                    chr(ord("a") + move.start_col)
                    + str(8 - move.start_row)
                )

                end = (
                    chr(ord("a") + move.end_col)
                    + str(8 - move.end_row)
                )

                text = self.text_font.render(

                    f"{start} - {end}",

                    True,

                    (235,235,235)

                )

                screen.blit(
                    text,
                    (
                        BOARD_SIZE + 35,
                        y
                    )
                )

                y += 24

        # Buttons
        button_y = 620

        for text in ["Undo", "Restart"]:

            rect = pygame.Rect(
                BOARD_SIZE + 20,
                button_y,
                self.card_width,
                45,
            )

            pygame.draw.rect(
                screen,
                (70, 70, 70),
                rect,
                border_radius=10,
            )

            pygame.draw.rect(
                screen,
                (120, 120, 120),
                rect,
                width=2,
                border_radius=10,
            )

            label = self.text_font.render(text, True, (255, 255, 255))

            screen.blit(
                label,
                (
                    rect.centerx - label.get_width() // 2,
                    rect.centery - label.get_height() // 2,
                ),
            )

            button_y += 60