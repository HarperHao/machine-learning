import pygame
import sys
from Game import *


# 设计开始画面的图片，直接利用蓝色的背景图片，另外再加上一个start game 按enter开始游戏的提示
def Start(screen):
    screen.fill(0)
    color_white = (255, 255, 255)
    color_red = (255, 0, 0)
    background_img = pygame.image.load('./resources/images/background.png')
    font = pygame.font.Font('./resources/fonts/font.TTF',50)
    logo_img = pygame.image.load('./resources/images/logo.png')
    logo_img = pygame.transform.scale(logo_img, (450, 100))
    bird_img = pygame.image.load('./resources/images/bird.png')
    bird_rect = bird_img.get_rect()
    logo_rect = logo_img.get_rect()
    logo_rect.centerx,logo_rect.centery = 320,150

    # 游戏难度选择
    play_difficult_white = font.render('Difficult',True,color_white)
    play_difficult_red = font.render('Difficult',True,color_red)
    play_difficult_rect = play_difficult_red.get_rect()
    play_difficult_rect.left,play_difficult_rect.top = 260,200
    play_easy_white = font.render('Easy',True,color_white)
    play_easy_red = font.render('Easy',True,color_red)
    play_easy_rect = play_easy_red.get_rect()
    play_easy_rect.left,play_easy_rect.top = 260,270

    # 游戏提示
    game_tip = font.render('Are You Ready',True,color_white)
    game_tip_rect = game_tip.get_rect()
    game_tip_rect.centerx, game_tip_rect.top = 300,350
    game_tip_flash_time = 25
    game_tip_flash_count = 0
    game_tip_show_flag = True
    clock = pygame.time.Clock()
    is_dual_mode = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return is_dual_mode
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s:
                    is_dual_mode = not is_dual_mode
        for x in range(WIDTH // background_img.get_width() + 1):
            for y in range(HEIGHT // background_img.get_height() + 1):
                screen.blit(background_img, (x * 100, y * 100))
        screen.blit(background_img,(0,0))
        screen.blit(logo_img,logo_rect)
        game_tip_flash_count += 1
        if game_tip_flash_count > game_tip_flash_time:
            game_tip_show_flag = not game_tip_show_flag
            game_tip_flash_count = 0
        if game_tip_show_flag:
            screen.blit(game_tip, game_tip_rect)
        # is dual_mode == False 选择的是Difficult
        if not is_dual_mode:
            bird_rect.right,bird_rect.top = play_difficult_rect.left-10,play_difficult_rect.top
            screen.blit(bird_img,bird_rect)
            screen.blit(play_difficult_red,play_difficult_rect)
            screen.blit(play_easy_white, play_easy_rect)
        # is dual_mode == True,即选择的是easy
        else:
            bird_rect.right, bird_rect.top = play_easy_rect.left - 10, play_easy_rect.top
            screen.blit(bird_img, bird_rect)
            screen.blit(play_easy_red, play_easy_rect)
            screen.blit(play_difficult_white,play_difficult_rect)
        pygame.display.update()
        clock.tick(100)