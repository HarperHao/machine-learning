"""
新增功能：
显示游戏界面
显示水果
"""

import pygame
import random


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

    def startGame(self):
        # 初始化窗口
        pygame.display.init()
        # 设置窗口，并显示
        self.surface = pygame.display.set_mode([self.screen_width, self.screen_height])
        pygame.display.set_caption("水果忍者1.0")
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
            self.getEvent()
            pygame.display.update()

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
            fruit = Fruits(100 + i * 20, 200)
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
        # 设置速度
        self.speed = 5

    # #  展示水果
    def display(self):
        # x = MainGame()
        game.surface.blit(self.image, self.rect)

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
