import pygame

def process_keys_up(keys, event):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_w or event.key == pygame.K_UP:
            keys.update({'up': False})
        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            keys.update({'left': False})
        if event.key == pygame.K_s or event.key == pygame.K_DOWN:
            keys.update({'down': False})
        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            keys.update({'right': False})

def process_keys_down(keys, event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w or event.key == pygame.K_UP:
            keys.update({'up': True})
        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            keys.update({'left': True})
        if event.key == pygame.K_s or event.key == pygame.K_DOWN:
            keys.update({'down': True})
        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            keys.update({'right': True})