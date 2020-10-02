"""
新增功能：
实现水果的斜抛
"""

import pygame
import random
import time
import math


class MainGame():
    def __init__(self):
        self.screen_width = 640
        self.screen_height = 480
        self.surface = None
        self.text_surface = None
        self.score = 0
        # 存储水果
        self.fruits_list = []
        self.fruitsCount = 3
        # 创建时钟对象
        self.clock = pygame.time.Clock()

    def startGame(self):
        # 初始化窗口
        pygame.display.init()
        # 设置窗口，并显示
        self.surface = pygame.display.set_mode([self.screen_width, self.screen_height])
        pygame.display.set_caption("水果忍者1.1")
        # 游戏背景图片
        self.background = pygame.image.load(r'.\source\images\background.jpg')
        # 设置得分surface
        text = '总得分：{}'.format(self.score)
        self.text_surface = self.drawText(text)
        self.score_image = pygame.image.load(r'.\source\images\score.png')
        # 初始化水果，并将水果添加到列表里
        self.creatFruits()
        while True:
            # 游戏背景
            self.surface.blit(self.background, (0, 0))
            # 游戏得分
            self.surface.blit(self.score_image, (10, 10))
            self.surface.blit(self.text_surface, (50, 20))
            # 水果显示
            self.blitFruits()
            # 获取事件
            self.getEvent()
            # 不断刷新
            pygame.display.update()
            self.clock.tick(200)

    def endGame(self):
        exit()

    def getEvent(self):
        # 获取所有事件
        eventList = pygame.event.get()
        for event in eventList:
            if event.type == pygame.QUIT:
                self.endGame()

    # 绘制左上方字体
    def drawText(self, text):
        pygame.font.init()
        # 获取字体对象
        font = pygame.font.SysFont('Kaiti', 18)
        # 绘制文字信息
        textSurface = font.render(text, True, (255, 0, 0))
        return textSurface

    # 创建水果对象并将水果添加到列表里
    def creatFruits(self):
        for i in range(self.fruitsCount):
            # 实例化水果并初始化水果的坐标
            fruit = Fruits(random.randint(120, 560), 470)
            self.fruits_list.append(fruit)

    # 显示水果
    def blitFruits(self):
        for fruit in self.fruits_list:
            fruit.display()


class Fruits():

    def __init__(self, left, top):
        # 加载图片集
        self.images = {'apple': pygame.image.load(r'.\source\images\fruit\apple.png'),
                       'banana': pygame.image.load(r'.\source\images\fruit\banana.png'),
                       'basaha': pygame.image.load(r'.\source\images\fruit\basaha.png'),
                       'peach': pygame.image.load(r'.\source\images\fruit\peach.png'),
                       'sandia': pygame.image.load(r'.\source\images\fruit\sandia.png')}
        # 随机获取图片surface
        self.random_num = self.randImage()
        self.image = self.images[self.random_num]
        # 获取图片的Rect区域
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        # self.init_left = left
        # self.init_top = top
        # 设置初始速度,
        self.speed_x = random.uniform(-3, 3)
        self.speed_y = random.uniform(-5, -3)
        # 设置速度
        self.vx = 0
        self.vy = 0
        # self.speed = random.randint(10, 50)
        # 设置平抛角度
        # self.alpha = random.uniform(0, math.pi)
        # 设置G
        self.G = 0.5

        self.t = 0.5

    # 展示水果
    def display(self):
        # x = MainGame()
        game.surface.blit(self.image, self.rect)
        self.set_pos(self.t)

    # 获取并更新斜抛运动时的坐标
    def set_pos(self, t):

        # x = self.speed * t * math.cos(self.alpha)
        # y = self.speed * t * math.sin(self.alpha) - 1 / 2 * self.G * t * t
        self.vy = self.speed_y + self.G * t  # 先负后正
        self.vx = self.speed_x
        self.rect.left = self.rect.left - self.vx * self.t
        self.rect.top = self.rect.top + self.vy * t
        self.t = self.t + 1/200

    # def move(self):
    #
    #     # 上次运行时间
    #     # time_seconds = (self.clock.tick()) / 1000
    #     self.set_pos(self.t)

    def randImage(self):
        num = random.randint(1, 5)
        if num == 1:
            return 'apple'
        elif num == 2:
            return 'banana'
        elif num == 3:
            return 'basaha'
        elif num == 4:
            return 'peach'
        elif num == 5:
            return 'sandia'


class Music():
    pass


if __name__ == "__main__":
    game = MainGame()
    game.startGame()
    # MainGame().startGame()
