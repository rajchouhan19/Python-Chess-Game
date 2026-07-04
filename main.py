import pygame

from src.constants import *
from src.game import Game

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Python Chess")

clock = pygame.time.Clock()

game = Game()

running = True

while running:

    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        game.handle_event(event)

    if game.in_menu:

        game.draw_menu(screen)

    else:

        game.update()

        game.draw(screen)

    pygame.display.flip()

pygame.quit()