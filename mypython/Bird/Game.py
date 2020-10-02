import random
"""
    1.开始画面的加载画面可以再美化一些
    2.开始针对俩个不同的结局，写不同的画面，一个是You failed的图片
    一个是 除了图片，还得有分数    此外，还得判断是否需要重新进入游戏

"""
import pygame
import Bird
import Pipe
import arrow
from start_screen import *
WIDTH,HEIGHT = 640,460
from pygame.locals import *
from switch_screen import *
from end_screen import *

def main():
    # 时钟
    clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT),0,32)
    start = Start(screen)
    if start:
        choice_logo = 'Easy'
    else:
        choice_logo = 'Difficult'
    switch_start(screen,choice_logo)
    pygame.display.set_caption('小鸟快飞')

    # 载入图片
    background_img = pygame.image.load("./resources/images/background.png")
    gameover_img = pygame.image.load("./resources/images/gameover.png")
    gamewin_img = pygame.image.load('./resources/images/youwin.png')
    # 箭
    arrow_img = pygame.image.load('./resources/images/bullet.png')
    # 生命条
    life_red_img = pygame.image.load('./resources/images/health_red.png')
    life_green_img = pygame.image.load('./resources/images/health_green.png')
    # 载入音乐
    jump_sound = pygame.mixer.Sound("./resources/audios/jump.wav")
    jump_sound.set_volume(6)
    sheji_sound = pygame.mixer.Sound('./resources/audios/explode.wav')
    sheji_sound.set_volume(7)
    #载入字体
    font = pygame.font.Font('./resources/fonts/simkai.ttf',24)
    # #时钟
    # clock = pygame.time.Clock()
    #小鸟
    bird = Bird.Bird(HEIGHT,WIDTH)
    #管道
    pipes = []
    #弓箭
    arrow_sprites_group = pygame.sprite.Group()
    arrow1 = arrow.Arrow(arrow_img,position=(640,300))
    arrow_sprites_group.add(arrow1)
    # 定义一个计时器，使得游戏过一段时间久新建弓箭
    t1 = 100
    t2 = 0
    #时间
    time0 = 0
    #几秒显示一次管道
    time_interval = 10
    #分数
    SCORE = 0
    shijian = 0
    # 生命值
    healthvalue = 194
    running = True
    running2 = True
    count = 0
    while running:
        screen.fill(0)
        for x in range(WIDTH//background_img.get_width()+1):
            for y in range(HEIGHT//background_img.get_height()+1):
                screen.blit(background_img,(x*100,y*100))
        time_passed = clock.tick() / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    jump_sound.play()
                    bird.is_jump = True
                    bird.cur_jump_height = 0
        bird.update(time_passed)
        screen.blit(bird.rotated_bird,bird.rect)
        if bird.is_dead():
            running = False
            running2 = False
        if not start:
            # 画管道
            time1 = pygame.time.get_ticks() / 1000
            if time1 - time0 > time_interval:
                time0 = time1
                pipes.append(Pipe.Pipe(HEIGHT,WIDTH))
            for i,pipe in enumerate(pipes):
                pipe.update(time_passed)
                for p in pipe.pipe:
                    screen.blit(p.img,p.rect)
                if bird.rect.left > pipe.x + Pipe.pipeHead().width and not pipe.add_score:
                    SCORE += 1
                    pipe.add_score = True
                if pipe.x + Pipe.pipeHead().width < 0:
                    pipes.pop(i)
                # 小鸟与管道碰撞检测
                if pygame.sprite.spritecollide(bird,pipe.pipe,False,None):
                    running = False
                    running2 = False
            # 小鸟与弓箭碰撞检测
        for arr in arrow_sprites_group:
            if pygame.sprite.collide_mask(bird,arr):
                sheji_sound.play()
                healthvalue -= random.randint(4, 10)
                arrow_sprites_group.remove(arr)
        if healthvalue <= 0:
            running = False
            running2 = False
        if t1 == 0:
            arrow1 = arrow.Arrow(arrow_img,position=(640,random.randint(0,HEIGHT)))
            arrow_sprites_group.add(arrow1)
            t1 = 100 - (t2 * 2)
            t2 = 20 if t1 >= 20 else t2 + 2
        t1 -= 1
        for arr in arrow_sprites_group:
            if arr.update():
                arrow_sprites_group.remove(arr)
        arrow_sprites_group.draw(screen)
        #显示分数
        scoreText = font.render('Score:' + str(SCORE),True,(0,0,0))
        scoreRect = scoreText.get_rect()
        scoreRect.topleft = [10,10]
        screen.blit(scoreText,scoreRect)
        # --倒计时信息
        # 改变一下倒计时的方式
        # count += 1
        # print(count)
        ticks = pygame.time.get_ticks()
        # if count == 1:
        #     ticks = 8641
        #     print(ticks)
        start_m = (80000 - ticks) // 60000
        print('start_m',start_m)
        start_s =(80000 - ticks) // 1000 % 60
        shijian = str(start_m) + ":" + str(start_s).zfill(2)
        countdown_text = font.render(shijian, True, (0, 0, 0))
        countdown_rect = countdown_text.get_rect()
        countdown_rect.topleft = [10, 30]
        screen.blit(countdown_text, countdown_rect)
        if shijian =='0:00' and healthvalue >0:
            running = False
        # 显示血条
        # 首先画出一个全红色的生命值条，然后在此上面画绿色条
        screen.blit(life_red_img,(440,10))
        for i in range(healthvalue):
            screen.blit(life_green_img,(i+443,13))
        pygame.display.flip()
        pygame.display.update()
    game_end = gameEnd(screen,SCORE,running2)
    # end = pygame.time.get_ticks()
    # kongyu = end - ticks
    # kongyu_m = kongyu // 60000
    # kongyu_s = (kongyu - kongyu_m * 60000) // 1000 % 60
    #
    # pygame.time.delay(2)
    return game_end

if __name__ == '__main__':
    while True:
        a = main()
        if a:
            break

