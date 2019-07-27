import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, max_health, max_speed, position, color):
        super().__init__()
        self._max_health = max_health
        self._health = max_health
        self._max_speed = max_speed
        self._speed = max_speed
        self._position = position

        x, y, z = position
        self.image = pygame.Surface([40, 20])
        self.image.fill(color)
        pygame.draw.rect(self.image, color, [0, 0, 40, 20])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


