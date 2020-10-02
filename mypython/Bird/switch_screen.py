import sys
import pygame
from Game import *
from Game import WIDTH


def switch_start(screen,choice_logo):
    screen.fill(0)
    background_img = pygame.image.load('./resources/images/background.png')
    color_white = (255, 255, 255)
    color_gray = (192, 192, 192)
    font = pygame.font.Font('./resources/fonts/font.TTF',30)
    logo_img = pygame.image.load('./resources/images/logo.png')
    logo_img = pygame.transform.scale(logo_img, (450, 100))
    bird_img = pygame.image.load('./resources/images/bird.png')
    bird_rect = bird_img.get_rect()
    logo_rect = logo_img.get_rect()
    logo_rect.centerx,logo_rect.centery = 350,150
    jindu_img = pygame.image.load('./resources/images/gamebar.png')
    # 游戏加载提示
    font_render = font.render('Londing game data,You will enter Level_%s' %choice_logo,True,color_white)
    font_rect = font_render.get_rect()
    font_rect.centerx, font_rect.centery = 330,220
    # 游戏加载进度条进度
    # jindu_img.rect = jindu_img.get_rect()
    jindu_rect = jindu_img.get_rect()
    jindu_rect.centerx, jindu_rect.centery = 330,340
    bird_rect.left = jindu_rect.left
    bird_rect.centery = jindu_rect.centery
    # 加载所需时间
    load_time_left = jindu_rect.right - bird_rect.right + 8
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if load_time_left <= 0:
            return
        for x in range(WIDTH // background_img.get_width() + 1):
            for y in range(HEIGHT // background_img.get_height() + 1):
                screen.blit(background_img, (x * 100, y * 100))
        screen.blit(logo_img,logo_rect)
        screen.blit(font_render,font_rect)
        screen.blit(jindu_img, jindu_rect)
        screen.blit(bird_img,bird_rect)
        pygame.draw.rect(screen,color_gray,(jindu_rect.left+6,jindu_rect.top+5,bird_rect.left-jindu_rect.left-8,bird_rect.bottom-jindu_rect.top-13))
        bird_rect.left += 1
        load_time_left -= 1
        pygame.display.update()
        clock.tick(60)



