import pygame
import sys
from .state import State


class GameLoop(object):

    def __init__(self, screen=None):

        # self.state = State()
        self.state_dict = None
        self.state_name = None
        self.state = None
        self.done = False
        self.exit = False
        self.screen = screen
        self.keys = None
        self.clock = pygame.time.Clock()
        self.current_time = 0.0
        self.fps = 60
        self.time_passed_seconds = 0
        self.key_events = []
        self.pressed_keys = []
        self.event_conditions = {}
        self.event_actions = {}
        self.event_persist = {}

    def setup_states(self, state_dict, start_state):
        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]

    def main_loop(self):
        print('in main loop')
        time_delta = self.clock.tick(self.fps)/1000.0
        self.time_passed_seconds = time_delta
        background = pygame.Surface(self.screen.get_size())
        background = background.convert()
        background.fill(pygame.Color("white"))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                # Exit the game if you press ESC
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()

                # TODO: process events based on keys/mouse updates
                pass

            self.screen.blit(background, (0, 0))
            pygame.display.flip()

            # TODO: update all objects in the game state
            # snake.move()
            # check_eat(snake, apple)
            # snake.draw(surface)
            # apple.draw(surface)

            # TODO: draw objects to screen
            font = pygame.font.Font(None, 36)
            # text = font.render(str(snake.length), 1, (10, 10, 10))
            # textpos = text.get_rect()
            # textpos.centerx = 20
            # background.blit(text, textpos)
            # self.screen.blit(background, (0, 0))

            # TODO: flip/update the display with the new info
            pygame.display.flip()
            pygame.display.update()

    def event_loop(self):
        self.key_events = []
        self.pressed_keys = list(pygame.key.get_pressed())
        for event in pygame.event.get():
            self.key_events.append(event)
            if event.type == pygame.QUIT:
                self.done = True
                self.exit = True
            self.state.get_event(event)

    def update(self, dt):

        self.current_time = pygame.time.get_ticks()
        # if self.state.quit:
        #     self.done = True
        #     self.exit = True
        # elif self.state.done:
        #     self.flip_state()
        self.state.update(self.screen, self.keys, self.current_time, dt)
        # if self.config.controller_overlay == "1":
        #     self.controller.draw(self)
