import pygame
from weapon import Weapon
from car import Car

class Player(pygame.sprite.Group):
    def __init__(self, position):
        super().__init__()
        
        self._position = position

        self.direction = pygame.Vector2((0, 1))

        x, y, z = position

        self._car = Car(max_health=100, max_speed=10, min_speed=-10)
        self.add(self._car)

        self._weapon = Weapon(self._car.rect.center)
        self.add(self._weapon)

        self.move_by(pygame.Vector2(x,y))

        self.left = False
        self.right = False
        self.up = False
        self.down = False

        self.last_speed_update = 0


    def update(self, key_state):
        """
        Updates player states every tick
        """
        super().update()
        self._position_update()
        self._rotation_update()

        self.up = key_state.get('up')
        self.down = key_state.get('down')
        self.left = key_state.get('left')
        self.right = key_state.get('right')

   
    def _position_update(self):
        """
        Updates player position proportional to speed
        """ 
        now = pygame.time.get_ticks()
        if now - self.last_speed_update > self._car._max_speed - self._car.speed:
        
            if self.down: # backward
                self._car.speed += self._car._acceleration
                if self._car.speed > self._car._max_speed:
                    self._car.speed = self._car._max_speed
            elif self.up: # forward
                self._car.speed -= self._car._acceleration 
                if self._car.speed < self._car._min_speed:
                    self._car.speed = self._car._min_speed
            else: # breaking with no button pushed
                if self._car.speed < 0:
                    self._car.speed += self._car._deacceleration
                    if self._car.speed > 0:
                        self._car.speed = 0
                elif self._car.speed > 0:
                    self._car.speed -= self._car._deacceleration
                    if self._car.speed < 0:
                        self._car.speed = 0
                
            self.last_speed_update = now
  
        if self._car.speed != 0:
            self.move_by(self.direction * self._car.speed)
           
            
    def _rotation_update(self):
        """
        Checks if key is pressed, if so rotates all sprites
        """
        if self.left:
            angle = self._car.steering_strenght
        elif self.right:
            angle = -self._car.steering_strenght
        else:
            return

        self.direction = self.direction.rotate(-angle)

        for sprite in self.sprites():
            sprite.rotate(angle)


    def move_by(self, position):
        """
        Moves all sprites by given position
        """
        for sprite in self.sprites():
            sprite.move_by(position)
        
        # fix gun in middle of car, weapon is shifted a bit
        # during rotation
        self._weapon.rect.center = self._car.rect.center 


        

    
