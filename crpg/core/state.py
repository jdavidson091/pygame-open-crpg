import logging
import pygame

logger = logging.getLogger(__name__)


# TODO: work in progress


class State(object):

    def __init__(self, game_loop):
        self.state = None
        self.start_time = 0.0
        self.current_time = 0.0
        self.done = False
        self.quit = False
        self.next = None
        self.previous = None
        self.persist = {}
        self.state_name = None
        self.state_dict = {}
        self.game_loop = game_loop
        self.screen = game_loop.screen
        self.time_passed_seconds = 0.0
        self.events = []
        self.pressed = []

    def get_event(self, event):
        pass

    def startup(self, current_time, persistant):
        self.persist = persistant
        self.start_time = current_time

    def shutdown(self):
        pass

    def cleanup(self):
        self.done = False
        self.shutdown()
        return self.persist

    def update(self, surface, keys, current_time, time_delta):
        # Tick our clock and limit the framerate to the fps specified in the
        # config
        self.time_passed_seconds = self.game_loop.time_passed_seconds

        # Fill the screen background with black
        self.screen.fill(pygame.Color("White"))

        # Get all the pygame events
        self.events = keys

        # Get all the keys pressed
        self.pressed = pygame.key.get_pressed()
        self.pressed = list(self.pressed)

        # # Get the player's tile position based on the global_x/y variables. Since the player's sprite is 1 x 2
        # # tiles in size, we add 1 to the 'y' position so the player's actual position will be on the bottom
        # # portion of the sprite.
        # self.player1.tile_pos = (float((self.player1.position[0] - self.global_x)) / float(
        #     self.tile_size[0]), (float((self.player1.position[1] - self.global_y)) / float(self.tile_size[1])) + 1)

        # # Handle world events
        # self.map_drawing()
        # self.player_movement()
        # self.high_map_drawing()
        # self.midscreen_animations()
        # self.draw_menus()
        # self.fullscreen_animations()
        pass

    def flip_state(self):
        """When a State changes to "done" necessary startup and cleanup functions
        are called and the current State is changed. In addition, the state
        specified in self.state.next is loaded.
        """
        previous, self.state_name = self.state_name, self.state.next
        persist = self.state.cleanup()
        self.state = self.state_dict[self.state_name]
        self.state.startup(self.current_time, persist)
        self.state.previous = previous
