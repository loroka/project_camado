import pygame
from player import Player
from keyboard_controller import *
from weapon import Weapon

def main():
    pygame.init()

    window = pygame.display.set_mode((800,600))

    clock = pygame.time.Clock()

    player = Player(position=(300, 500, 0))

    quit_flag = False
    key_state = {'up': False, 'left': False, 'right': False, 'down': False}
    while not quit_flag:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quit_flag = True
            if event.type == pygame.KEYUP:
                process_keys_up(key_state, event)
                player.key_update(key_state)
            if event.type == pygame.KEYDOWN:
                process_keys_down(key_state, event)
                player.key_update(key_state)
              
        player.draw(window)
        player.update()

        pygame.display.update()
        window.fill((0,0,0))
        clock.tick(60)
        
    pygame.quit()
        

if __name__ == "__main__":
    main()