import pygame
import components as Com
import engine
from sys import exit
from random import choice, randint

pygame.init()
screen = pygame.display.set_mode((Com.WIDTH, Com.HEIGHT))
pygame.display.set_caption("Mario Runner")
clock = pygame.time.Clock()

game_over = False
push_obstacle = False
start_time = 0
score = 0
hit_score = 0
life = 2

evil_timer = pygame.USEREVENT + 1
pygame.time.set_timer(evil_timer, 800)


def game_over_render(life=0):
    screen.blit(Com.background_surface, (0, 0))
    screen.blit(Com.game_over_surface, Com.game_over_rect)
    screen.blit(Com.player_dead_surface, Com.player_dead_rect)
    screen.blit(Com.restart_surface, Com.restart_rect)

    engine.render_life(life)
    screen.blit(Com.text_score_surface, Com.text_score_rect)
    return 0, 0


def game(start_time, life, hit_score):
    screen.blit(Com.background_surface, (0, 0))

    # Player
    Com.player.draw(screen)
    Com.player.update()

    # obstacles
    Com.evil_group.draw(screen)
    Com.evil_group.update()

    # Coins
    Com.coins_group.draw(screen)
    Com.coins_group.update()

    collision = engine.evils_collision_sprite()

    hit_score += engine.coin_collision_sprite()

    score = engine.add_coin_score(start_time, hit_score)
    engine.render_life(life)
    screen.blit(Com.text_score_surface, Com.text_score_rect)

    if life==2:
        screen.blit(Com.life_surface_2, Com.life_rect_2)
    if life ==1:
        screen.blit(Com.life_surface_1, Com.life_rect_1 )

    is_game_over = False
    if collision:
        life -= 1
        if life == 0:
            is_game_over = True
        else:
            pygame.time.delay(1000)

    return is_game_over, score, life, hit_score


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_over == True:
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                start_time = pygame.time.get_ticks() // 1000
                game_over, life, hit_score = False, 2, 0
        else:
            if event.type == evil_timer:
                if push_obstacle:
                    new_evil = Com.Evils(choice([1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]))
                    if not engine.check_overlap(new_evil, Com.evil_group) and not engine.check_overlap(new_evil, Com.coins_group):
                        Com.evil_group.add(new_evil)
                    push_obstacle = False
                else:
                    type = choice([1, 2])
                    new_coins = []
                    for i in range(randint(1, 2)):
                        new_coin = Com.Coin(type, i)
                        if not engine.check_overlap(new_coin, Com.evil_group) and not engine.check_overlap(new_coin, Com.coins_group):
                            new_coins.append(new_coin)
                    Com.coins_group.add(*new_coins)
                    push_obstacle = True

    if game_over == True:
        score = game_over_render()
    else:
        game_over, score, life, hit_score = game(start_time, life, hit_score)

    pygame.display.update()
    clock.tick(90)