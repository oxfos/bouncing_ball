import sys
import pygame
from settings import Settings
from bar import Bar

class BouncingBall:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Bouncing Ball")
        self.bar = Bar(self)

    def run_game(self):
        """Main game loop."""
        while True:
            self._check_events()
            self.bar.update() # implements movement depending on movement flag
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # Pressing arrow keys for movement:
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            # Releasing arrow keys:
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Checks keydown events."""
        if event.key == pygame.K_RIGHT:
            self.bar.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.bar.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Checks keyup events."""
        if event.key == pygame.K_RIGHT:
            self.bar.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.bar.moving_left = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.bar.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    # Make game instance + run game.
    bb = BouncingBall()
    bb.run_game()