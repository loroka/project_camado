import pygame
import pygame.sprite as sprite
import pygame.font as font

from pygame import Vector2

from weapon import Weapon
from car import Car

class Player(sprite.Group):
    def __init__(self, position):
        super().__init__()
        
        self._position = position

        self.direction = Vector2((0, 1))

        x, y, z = position

        self._car = Car()
        self.add(self._car)

        #self._weapon = Weapon(self._car.rect.center)
        #self.add(self._weapon)

        #self.move_by(pygame.Vector2(x,y))

        self.left = False
        self.right = False
        self.up = False
        self.down = False


    def update(self, key_state):
        """
        Updates player states every tick
        """
        super().update()
        self._position_update()
        #self._rotation_update()

        self.up = key_state.get('up')
        self.down = key_state.get('down')
        self.left = key_state.get('left')
        self.right = key_state.get('right')

        if self.up:
            self._car.accelerate()
        if self.down:
            self._car.brake()
        if self.left:
            self._car.turn_left()
        if self.right:
            self._car.turn_right()
        
        if not self.left and not self.right:
            self._car.counter_steer()

        if not self.up and not self.down:
            self._car.decelarate()

   
    def _position_update(self):
        """
        Updates player position proportional to speed
        """ 
        self._car.update()
    
    def draw(self, window):
        super().draw(window)
        
        myfont = font.SysFont('Comic Sans MS', 15) 
        infos = [] 
        infos.append(myfont.render(f"velocity: {self._car.velocity}", False, (255, 255, 255))) 
        infos.append(myfont.render(f"acceleration: {self._car.acceleration}", False, (255, 255, 255))) 

        for i, info in enumerate(infos): 
            window.blit(info, (0,20 * i)) 