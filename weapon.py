import pygame

class Weapon(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()

        self.load_image = pygame.image.load("assets/weapons/turret_01_mk1.png")
        self.original_image = pygame.Surface([128, 128])
        self.original_image.blit(self.load_image, [0,0], [0, 0, 128, 128])
        self.original_image = pygame.transform.scale(self.original_image, [32,32])
        self.original_image.set_colorkey((0,0,0))
        self.image = self.original_image
        self.image.set_colorkey((0,0,0))

        self.rect = self.image.get_rect()
        self.rect.center = position

    def shoot():
        pass