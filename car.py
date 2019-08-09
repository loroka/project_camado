import pygame
import pygame.sprite as sprite

from math import tan, radians, degrees

from pygame import Vector2

class Car(sprite.Sprite):
    def __init__(self):
        super().__init__()

        # movement
        self.velocity = Vector2((0.0, 0.0))
        self.acceleration = 0.0
        self.acceleration_speed = 0.3
        self.deceleration = 0.1
        self.braking_force = 0.5

        # steering
        self.angle = 0
        self.length = 3 # distance between front and back wheels
        self.steering = 0.0
        self.steering_sensitivity = 0.15
        
        # max
        self.max_acceleration = 3.0
        self.max_steering = 1.75
        self.velocity = Vector2((0,0))
        
        self.position = Vector2((200, 500))

        # asset
        self.original_image = pygame.image.load("assets/Car.png").convert()
        self.original_image = pygame.transform.scale(self.original_image, (48, 48))
        self.image = self.original_image
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

    def accelerate(self):
        """
        Increase car engine force, if reversing brakes
        """
        if self.velocity.y > 0: # braking
            self.acceleration = self.braking_force
        else:
            self.acceleration += self.acceleration_speed
        self.acceleration = max(-self.max_acceleration, min(self.acceleration, self.max_acceleration))

    
    def decelarate(self):
        """
        Decelarate engine force
        """
        if self.acceleration > self.deceleration:
            self.acceleration -= self.deceleration
        elif self.acceleration < -self.deceleration:
            self.acceleration += self.deceleration
        else:
            self.acceleration = 0
            

    def brake(self):
        """
        Brakes car or accelerate backwards
        """
        if self.velocity.y < 0: # braking
           self.acceleration = -self.braking_force
        else:
            self.acceleration -= self.acceleration_speed
        self.acceleration = max(-self.max_acceleration, min(self.acceleration, self.max_acceleration))
        
    
    def turn_left(self):
        self.steering -= self.steering_sensitivity
        self.steering = max(-self.max_steering, min(self.steering, self.max_steering))
        
    
    def turn_right(self):
        self.steering += self.steering_sensitivity
        self.steering = max(-self.max_steering, min(self.steering, self.max_steering))


    def counter_steer(self):
        self.steering = 0


    def update(self):
        """
        Updates vehicle
        """

        self._update_physics()
        self._update_sprite()

        # update posiiton
        self.rect.x = self.position.x
        self.rect.y = self.position.y

    def _update_physics(self):
        self.velocity.y = -self.acceleration 

        if self.steering != 0:
            turning_radius = self.length / tan(radians(self.steering ))
            angular_velocity = self.velocity.y / turning_radius
        else:
            angular_velocity = 0

        angle_offset = self.angle % 90 
        if angle_offset > -1 and angle_offset < 1:
            self.angle -= angle_offset
        self.position += self.velocity.rotate(-self.angle)
        self.angle += degrees(angular_velocity)

   
    def _update_sprite(self):
        rotated_image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = rotated_image.get_rect()
        self.image = rotated_image