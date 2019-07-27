import pygame
from player import Player
from keyboard_controller import *

def main():
    pygame.init()

    window = pygame.display.set_mode((800,600))

 
    clock=pygame.time.Clock()

    player = Player(100, 10, (100, 100, 0), (255, 255, 255))

    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(player)

    quit_flag = False
    key_state = {'up': False, 'left': False, 'right': False, 'down': False}
    while not quit_flag:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quit_flag = True
            if event.type == pygame.KEYUP:
                process_keys_up(key_state, event)
            if event.type == pygame.KEYDOWN:
                process_keys_down(key_state, event)
              


        all_sprites_list.draw(window)


        all_sprites_list.update()
        pygame.display.flip()
        clock.tick(60)
        
    pygame.quit()
        



if __name__ == "__main__":
    main()