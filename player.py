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
        elif self.down:
            self._car.brake()
        else:
            self._car.decelarate()

   
    def _position_update(self):
        """
        Updates player position proportional to speed
        """ 
        self._car.update()
            
    def draw(self, window):
        """
        Draws all sprites in group and renders player info
        """
        super().draw(window)

        # print player info
        myfont = font.SysFont('Comic Sans MS', 15)
        infos = []
        infos.append(myfont.render(f"traction: {self._car.traction}", False, (255, 255, 255)))
        infos.append(myfont.render(f"speed: {self._car.speed:.4f}", False, (255, 255, 255)))
        infos.append(myfont.render(f"velocity: {self._car.velocity}", False, (255, 255, 255)))
        infos.append(myfont.render(f"forward: {self._car.forward}", False, (255, 255, 255)))
        infos.append(myfont.render(f"w-front: {self._car.weight_front:.4f}", False, (255, 255, 255)))
        infos.append(myfont.render(f"w-rear: {self._car.weight_rear:.4f}", False, (255, 255, 255)))

        for i, info in enumerate(infos):
            window.blit(info, (0,20 * i))

        

    
