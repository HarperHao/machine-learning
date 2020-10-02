import pygame
import sys
from Game import *


# 游戏结束
def gameEnd(screen,score,running2):
    font = pygame.font.Font(None,24)
    font_red = (255,0,0)
    # font_black = (113, 197, 207)
    font_black = (255, 255, 255)
    font_green = (0,255,0)
    gameover_img = pygame.image.load("./resources/images/gameover.png")
    gamewin_img = pygame.image.load('./resources/images/youwin.png')
    if not running2:
        text =font.render(f'Score:{score}',True,font_red)
    else:
        text =font.render(f'Score:{score}',True,font_green)
    text_rect = text.get_rect()
    text_rect.centerx = screen.get_rect().centerx
    text_rect.centery = screen.get_rect().centery + 24
    text_restart_b = font.render('Restart',True,font_black)
    text_restart_g = font.render('Restart',True,font_green)
    text_restart_r = font.render('Restart',True,font_red)
    text_quit_b = font.render('Quit',True,font_black)
    text_quit_g = font.render('Quit',True,font_green)
    text_quit_r = font.render('Quit',True,font_red)
    restart_rect = text_restart_g.get_rect()
    restart_rect.centerx = screen.get_rect().centerx
    restart_rect.centery = screen.get_rect().centery + 40
    quit_rect = text_quit_b.get_rect()
    quit_rect.centerx = screen.get_rect().centerx
    quit_rect.centery = screen.get_rect().centery + 55
    is_quit_game = False
    while True:
        screen.fill(0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return is_quit_game
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s:
                    is_quit_game = not is_quit_game
        screen.blit(text,text_rect)
        if running2:
            screen.blit(gamewin_img, (0, 0))
            if not is_quit_game:
                screen.blit(text_restart_g, restart_rect)
                screen.blit(text_quit_b, quit_rect)
            else:
                screen.blit(text_restart_b, restart_rect)
                screen.blit(text_quit_g, quit_rect)
        else:
            screen.blit(gameover_img, (0, 0))
            if not is_quit_game:
                screen.blit(text_restart_r, restart_rect)
                screen.blit(text_quit_b, quit_rect)
            else:
                screen.blit(text_restart_b, restart_rect)
                screen.blit(text_quit_r, quit_rect)
        pygame.display.flip()
        pygame.display.update()
