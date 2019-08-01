import pygame

def check_keys(keys, event, isPressed):
    """
    Update keys states depending on pressed keys
    :param keys: dict with key states
    :param event: pygame.event, containing pressed keys
    :param state: bool True - pressed 
    """
    if event.key == pygame.K_w or event.key == pygame.K_UP:
        keys.update({'up': isPressed})
    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
        keys.update({'left': isPressed})
    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
        keys.update({'down': isPressed})
    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
        keys.update({'right': isPressed})