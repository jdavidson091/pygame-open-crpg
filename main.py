import sys
import pygame

from crpg.core import (
    prepare,
    state,
)
from crpg.core.game_loop import GameLoop

if __name__ == '__main__':

    # set up pygame
    pygame.init()

    # read the configuration file
    # config = config.Config()

    # The game resolution
    resolution = (1280, 720)

    # set up the window with epic name
    # fullscreen = pygame.FULLSCREEN
    fullscreen = 0
    screen = pygame.display.set_mode(resolution, fullscreen, 32)
    pygame.display.set_caption('Game')

    # # # Native resolution is similar to the old gameboy resolution. This is used for scaling.
    # # native_resolution = [240, 160]
    # #
    # # # If scaling is enabled, scale the tiles based on the resolution
    # # if config.scaling == "1":
    # #     scale = int((resolution[0] / native_resolution[0]))
    #
    # # Fill background
    # background = pygame.Surface(screen.get_size())
    # background = background.convert()
    # background.fill(pygame.Color("white"))
    #
    # # Blit everything to the screen
    # screen.blit(background, (0, 0))
    # pygame.display.flip()

    # print("Loading map")
    # tile_size = [80, 80]  # 1 tile = 16 pixels
    # testmap = Map()
    # # testmap.loadfile("resources/maps/test.map", tile_size)
    # testmap.loadfile("resources/maps/test_pathfinding.map", tile_size)

    # # Event loop THIS IS WHAT SHIT IS DOING RIGHT NOW BRAH
    # while True:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             sys.exit()
    #
    #         # Exit the game if you press ESC
    #         if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
    #             pygame.quit()
    #
    #     screen.blit(background, (0, 0))
    #     pygame.display.flip()

    # prepare.init()
    game_loop = GameLoop(screen=screen)
    # game.player1 = prepare.player1
    state_dict = {"WORLD": state.State(game_loop)}
    game_loop.setup_states(state_dict, "WORLD")
    game_loop.main_loop()
