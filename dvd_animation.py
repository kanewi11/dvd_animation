import sys
import random
from itertools import cycle
from collections import deque

import pygame


class DVDAnimation:
    WIDTH, HEIGHT = 800, 600
    SCREEN_SIZE = (WIDTH, HEIGHT)
    BACKGROUND = (0, 0, 0)

    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Create the window
        self.screen = pygame.display.set_mode(self.SCREEN_SIZE)
        pygame.display.set_caption('DVD Animation')

        # Load the DVD logo image (load only once)
        self.dvd_logo = pygame.image.load('logo.png').convert_alpha()

        self.clock = pygame.time.Clock()

        # Generate a deque of random colors for the logo
        self.colors = [(random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)) for _ in range(100)]
        random.shuffle(self.colors)
        self.color_cycle = cycle(deque(self.colors))

        # Initial position and speed of the logo
        self.x, self.y = self.WIDTH // 2, self.HEIGHT // 2
        self.speed_x, self.speed_y = 0.5, 0.5
        self.logo = self.dvd_logo

        # Calculate maximum x and y bounds for the logo movement
        self.max_x = self.WIDTH - self.dvd_logo.get_width()
        self.max_y = self.HEIGHT - self.dvd_logo.get_height()

    def fill_logo(self, color):
        dvd_logo_copy = self.dvd_logo.copy()
        dvd_logo_copy.fill(color, special_flags=pygame.BLEND_RGBA_MIN)
        return dvd_logo_copy

    def update_logo_position(self):
        # Move horizontally
        self.x += self.speed_x
        if not 0 <= self.x <= self.max_x:
            self.logo = self.fill_logo(next(self.color_cycle))
            self.speed_x = -self.speed_x

        # Move vertically
        self.y += self.speed_y
        if not 0 <= self.y <= self.max_y:
            self.logo = self.fill_logo(next(self.color_cycle))
            self.speed_y = -self.speed_y

    def run(self):
        while True:
            self._handle_events()
            self.update_logo_position()

            # Fill the background with white
            self.screen.fill(self.BACKGROUND)

            # Render the DVD logo on the screen
            self.screen.blit(self.logo, (self.x, self.y))

            # Update the display
            pygame.display.flip()

            # Limit the FPS (frames per second)
            self.clock.tick(120)

    @staticmethod
    def _handle_events():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


if __name__ == '__main__':
    dvd_animation = DVDAnimation()
    dvd_animation.run()
