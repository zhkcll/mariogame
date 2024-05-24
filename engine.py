import pygame
import components as Com


def check_overlap(new_sprite, group):
    for sprite in group:
        if pygame.sprite.collide_rect(new_sprite, sprite):
            return True
    return False


def display_score(start_time):
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    Com.text_score_surface = Com.test_font.render(
        "Scores: " + f'{current_time}', False, "Green")
    Com.text_score_rect = Com.text_score_surface. \
        get_rect(center=(Com.FONT_POS_X, Com.FONT_SIZE))
    return current_time


def evils_collision_sprite():
    if pygame.sprite.spritecollide(Com.player.sprite, Com.evil_group, False):
        Com.evil_group.empty()
        return True
    else:
        return False


def coin_collision_sprite():
    coin_hit_list = pygame.sprite.spritecollide( Com.player.sprite, Com.coins_group, True)
    return len(coin_hit_list)


def render_life(life):
    if life==2:
        Com.life_surface_2
    if life ==1:
        Com.life_surface_1



def add_coin_score(start_time, hit_score):
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    current_time += hit_score * 10
    Com.text_score_surface = Com.test_font.render(
        "Scores: " + f'{current_time}', False, "White")

    Com.text_score_rect = Com.text_score_surface.get_rect(
        center=(Com.FONT_POS_X, Com.FONT_SIZE))
    return current_time