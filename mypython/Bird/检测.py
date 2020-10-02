# # import pygame
# # WIDTH,HEIGHT = 640,460
# # from pygame.locals import *
# #
# # def main():
# #     pygame.init()
# #     screen = pygame.display.set_mode((WIDTH,HEIGHT),0,32)
# #     pygame.display.set_caption('小鸟快飞')
# #     # 载入图片
# #     background_img = pygame.image.load("./resources/images/bird.png")
# #     print(background_img.get_rect())
# #     gameover_img = pygame.image.load("./resources/images/gameover.png")
# #     # 载入音乐
# #     jump_sound = pygame.mixer.Sound("./resources/audios/jump.wav")
# #     jump_sound.set_volume(6)
# #     #载入字体
# #     font = pygame.font.Font('./resources/fonts/simkai.ttf',24)
# #     #时钟
# #     clock = pygame.time.Clock()
# #
# #     #小鸟
# #     #管道
# #     #时间
# #     time = 0
# #     time_interval = 0
# #     #分数
# #     score = 0
# #     running = True
# #     while running:
# #         screen.fill(0)
# #         screen.blit(background_img, (0, 0))
# #         rotated_bird = pygame.transform.rotate(background_img,40)
# #         print(rotated_bird.get_rect())
# #         screen.blit(rotated_bird, (32, 0))
# #         # for x in range(WIDTH//background_img.get_width()+1):
# #         #     for y in range(HEIGHT//background_img.get_height()+1):
# #         #         screen.blit(background_img,(x*100,y*100))
# #         time_passed = clock.tick() / 1000
# #         for event in pygame.event.get():
# #             if event.type == pygame.QUIT:
# #                 pygame.quit()
# #                 exit(0)
# #             if event.type == pygame.KEYDOWN:
# #                 if event.key == K_SPACE:
# #                     jump_sound.play()
# #         pygame.display.flip()
# #         pygame.display.update()
# #     pygame.display.flip()
# #     pygame.display.update()
# # if __name__ == '__main__':
# #     main()
# #
# # import pygame, sys, random
# # from pygame.locals import *
# #
# #
# # # 定义精灵类，从Sprite继承，并重写update()函数
# # # 这里必须在初始化函数中执行父类构造函数Sprite.__init__(self)
# # class Player(pygame.sprite.Sprite):
# #     def __init__(self, color, topleft):
# #         pygame.sprite.Sprite.__init__(self)
# #         self.image = pygame.Surface((20, 20))  # 这个就是每个精灵的图片Surface
# #         self.image.fill(color)
# #         self.rect = self.image.get_rect()  # 每个精灵Surface显示的Rectangle
# #         self.rect.topleft = topleft  # 设定矩阵左上角的位置
# #
# #
# #     def update(self):
# #         # 向右移动，如果到达最右边则从左边开始
# #         speed = random.randint(0, 10)
# #         self.rect.left += speed
# #         if self.rect.left > 630:
# #             self.rect.left = -10
# #
# #
# # pygame.init()
# # FSPClock = pygame.time.Clock()
# # screen = pygame.display.set_mode((640, 480))
# #
# # playerGroup = pygame.sprite.Group()
# #
# # # 定义四个Player，并添加到精灵的Group中
# # for pos in ((0, 0), (100, 100), (200, 200), (300, 300)):
# #     playerGroup.add(Player((0, 0, 0), pos))
# #
# # while True:
# #     screen.fill((255, 255, 255))
# #
# #     for event in pygame.event.get():
# #         if event.type == QUIT:
# #             pygame.quit()
# #             sys.exit()
# #
# #     # 将每个精灵更新后显示在Screen上
# #     for player in playerGroup:
# #         player.update()
# #         screen.blit(player.image, player.rect)
# #
# #     pygame.display.update()
# #     FSPClock.tick(10)
# import pygame
# clock = pygame.time.Clock()
# while 1:
#     time_passed = clock.tick() / 1000
#     print(time_passed)
#     # time_passed = clock.tick(30)
#     sum = 0
#     for i in range(20000000):
#         sum += i
#     print(time_passed)
# a = '2'
# b = '2'
# if a == b:
#     print('yes')
import  time
for second in range(120,-1,-1):
    print("%02d:%02d"%(second // 60,second % 60))
    time.sleep(1)

