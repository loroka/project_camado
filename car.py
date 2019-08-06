import pygame
import pygame.sprite as sprite

from pygame import Vector2

class Car(sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.mass = 1000
        self.total_weight = self.mass * 10  # take gravity to count
        self.gravity_center = 0
        self.grav_magic = 1.5
        self.weight_front = self.mass / 2
        self.weight_rear = self.mass / 2

        self.engine_f = 0
        self.max_engine_f = 100
        self.acceleration_speed = 5
        self.brake_f = 50
        self.velocity = Vector2((0.0,0.0))
        self.speed = 0.0

        self.traction = Vector2((0,0))
        self.wheel_friction = 1.0

        self.air_resistance = 1
        self.roll_resistance = 30 # aprox 30 times air resistance
        self.f_drag = Vector2((0,0))
        self.f_res = Vector2((0,0))

        self.direction = Vector2((0, -1))
        self.forward = True
        
        # asset
        self.original_image = pygame.image.load("assets/Car.png").convert()
        self.original_image = pygame.transform.scale(self.original_image, (48, 48))
        self.image = self.original_image
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect = (200, 500) 

    def accelerate(self):
        """
        Increase car engine force, if reversing brakes
        """
        if self.speed > 0.1 and not self.forward: # brake
            self.engine_f += self.brake_f
            if self.engine_f > 0:
                self.engine_f = 0
        else: # go front
            self.engine_f += self.acceleration_speed
            if self.engine_f > self.max_engine_f:
                self.engine_f = self.max_engine_f
            self.forward = True
    
    def decelarate(self):
        """
        Decelarate engine force
        """
        if self.speed > 0.1 and self.forward:
            self.engine_f -= self.acceleration_speed * 2
            if self.engine_f < 0:
                self.engine_f = 0
        elif self.speed > 0.1 and not self.forward:
            self.engine_f += self.acceleration_speed * 2
            if self.engine_f > 0:
                self.engine_f = 0
            
    def brake(self):
        """
        Brakes car or accelerate backwards
        """
        if self.speed > 0.1 and self.forward: # brake
            self.engine_f -= self.brake_f
            if self.engine_f < 0:
                self.engine_f = 0
        else: # go reverse
            self.engine_f -= self.acceleration_speed / 2
            self.forward = False

    def update(self):
        """
        Updates vehicle forces
        """
        self.traction = self.engine_f * self.direction
        max_force = self.wheel_friction * self.total_weight

        # limit engine force prop. to traction
        if self.traction.length() > max_force:
            self.traction.scale_to_length(max_force)

        self.speed = self.velocity.dot(self.velocity)

        # resistance
        self.f_drag = -self.air_resistance * self.velocity * self.speed
        self.f_res = -self.roll_resistance * self.velocity

        # real force
        longtitudinal_f = self.traction + self.f_drag + self.f_res
        acceleration = longtitudinal_f / self.mass

        if self.forward:
            self.weight_front = (self.total_weight / 2) - (self.mass / self.grav_magic) * acceleration.length()
            self.weight_rear = (self.total_weight / 2) + (self.mass / self.grav_magic) * acceleration.length()
        else:
            self.weight_front = (self.total_weight / 2) + (self.mass / self.grav_magic) * acceleration.length()
            self.weight_rear = (self.total_weight / 2) - (self.mass / self.grav_magic) * acceleration.length()

        self.gravity_center = 1.0 - self.weight_front
        
        self.velocity += acceleration 

        # change position
        self.rect += self.velocity
        