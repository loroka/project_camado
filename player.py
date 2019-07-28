import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, max_health, max_speed, min_speed, position, color):
        super().__init__()
        self._max_health = max_health
        self._health = max_health
        self._max_speed = max_speed
        self._min_speed = min_speed
        self._speed = 0
        self._position = position
        self._acceleration = 0.5
        self._deacceleration = 3.0
        self.rotation = 0
        self.rotation_speed = 1
        self.direction = pygame.Vector2((0, 1))

        x, y, z = position

        self.original_image = pygame.image.load("assets/Car.png")
        self.original_image = pygame.transform.scale(self.original_image, (48, 48))
        self.original_image.set_colorkey((0,0,0))
        self.image = self.original_image
        self.image.set_colorkey((0,0,0))

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.left = False
        self.right = False
        self.up = False
        self.down = False

        self.last_speed_update = 0
        self.last_rot_update = 0

    def update(self):
        """
        Updates player every tick
        """
        super().update()
        self._position_update()

    def key_update(self,key_state):
        """
        Update current keystate
        :param key_state: dict containing key states
        """ 
        self.up = key_state.get('up')
        self.down = key_state.get('down')
        self.left = key_state.get('left')
        self.right = key_state.get('right')
    
    def _position_update(self):
        """
        Updates player position proportional to speed
        """ 
        now = pygame.time.get_ticks()
        if now - self.last_speed_update > self._max_speed - self._speed:
        
            if self.down: # backward
                self._speed += self._acceleration
                if self._speed > self._max_speed:
                    self._speed = self._max_speed
            elif self.up: # forward
                self._speed -= self._acceleration 
                if self._speed < self._min_speed:
                    self._speed = self._min_speed
            else: # breaking with no button pushed
                if self._speed < 0:
                    self._speed += self._deacceleration
                    if self._speed > 0:
                        self._speed = 0
                elif self._speed > 0:
                    self._speed -= self._deacceleration
                    if self._speed < 0:
                        self._speed = 0
                
            self.last_speed_update = now

        if self.left:
            self.rotate(True)

            pass
        if self.right:
            self.rotate(False)
            pass
                    
        self.rect.x += self._speed * self.direction.x
        self.rect.y += self._speed * self.direction.y
            
    def rotate(self, direction):
        """
        Rotates player by angle
        :param angle: int
        """
        now = pygame.time.get_ticks()
        if now - self.last_rot_update > self.rotation_speed:
            self.last_rot_update = now

            if direction: # left
                angle = 3
            else: # right
                angle = -3

            self.rotation = (self.rotation + angle) % 360
            self.direction = self.direction.rotate(-angle)
            new_image = pygame.transform.rotate(self.original_image, self.rotation)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center




        

    
