import pygame
from player import Player
from keyboard_controller import *

def main():
    pygame.init()

    window = pygame.display.set_mode((800,600))

 
    clock=pygame.time.Clock()

    player = Player(max_health=100, max_speed=10, min_speed=-10, 
                    position=(300, 500, 0), color=(255, 255, 255))

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
                player.key_update(key_state)
            if event.type == pygame.KEYDOWN:
                process_keys_down(key_state, event)
                player.key_update(key_state)
              

        all_sprites_list.draw(window)


        all_sprites_list.update()
        pygame.display.update()
        window.fill((0,0,0))
        clock.tick(60)
        
    pygame.quit()
        



if __name__ == "__main__":
    main()