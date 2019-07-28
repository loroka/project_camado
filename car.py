import pygame

class Car(pygame.sprite.Sprite):
    def __init__(self, max_health, max_speed, min_speed):
        super().__init__()
        # health
        self._max_health = max_health
        self._health = max_health

        # velocity
        self._max_speed = max_speed
        self._min_speed = min_speed
        self.speed = 0
        self._acceleration = 0.5
        self._deacceleration = 3.0

        # steering
        self.rotation = 0
        self.steering_strenght = 3
        self.last_rot_update = 0

        # asset
        self.original_image = pygame.image.load("assets/Car.png")
        self.original_image = pygame.transform.scale(self.original_image, (48, 48))
        self.original_image.set_colorkey((0,0,0))
        self.image = self.original_image
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        
    def rotate(self, angle):
        """
        Rotate car by angle

        :param angle: int
        """

        self.rotation = (self.rotation + angle) % 360
        new_image = pygame.transform.rotate(self.original_image, self.rotation)
        old_center = self.rect.center
        self.image = new_image
        self.rect = self.image.get_rect()
        self.rect.center = old_center
    
    def move_by(self, position):
        """
        Move car by position
        
        :param position: pygame.Vector2
        """
        self.rect.x += position.x
        self.rect.y += position.y

