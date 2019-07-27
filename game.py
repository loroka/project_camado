import pygame
from player import Player


def main():
    pygame.init()

    window = pygame.display.set_mode((800,600))

 
    clock=pygame.time.Clock()

    player = Player(100, 10, (100, 100, 0), (255, 255, 255))

    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(player)

    quit_flag = False
    while not quit_flag:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quit_flag = True
        

        all_sprites_list.draw(window)

        all_sprites_list.update()
        pygame.display.flip()
        clock.tick(60)
        
    pygame.quit()
        



if __name__ == "__main__":
    main()