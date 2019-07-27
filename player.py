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

        x, y, z = position
        self.image = pygame.Surface([40, 20])
        self.image.fill(color)
        pygame.draw.rect(self.image, color, [0, 0, 40, 20])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.left = False
        self.right = False
        self.up = False
        self.down = False

        self.last_update = 0

    def update(self):
        super().update()
        self._position_update()

    
    
    def key_update(self,key_state):
       self.up = key_state.get('up')
       self.down = key_state.get('down')
       self.left = key_state.get('left')
       self.right = key_state.get('right')
    
    
    def _position_update(self):
        
        now = pygame.time.get_ticks()
        if now - self.last_update > self._max_speed - self._speed:
        
            if self.right:
                self._speed += self._acceleration
                if self._speed > self._max_speed:
                    self._speed = self._max_speed
            elif self.left:
                self._speed -= self._acceleration 
                if self._speed < self._min_speed:
                    self._speed = self._min_speed
            else:
                if self._speed < 0:
                    self._speed += self._deacceleration
                    if self._speed > 0:
                        self._speed = 0
                elif self._speed > 0:
                    self._speed -= self._deacceleration
                    if self._speed < 0:
                        self._speed = 0
                else:
                    pass
            self.last_update = now
        self.rect.x += self._speed
            
        

        

    
