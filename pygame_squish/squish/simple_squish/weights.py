#!coding:utf-8
import sys,pygame
from pygame.locals import *
from random import randrange

class Weight(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Weight_image
        self.rect = self.image.get_rect()
        self.reset()
    def reset(self):
        self.rect.top = -self.rect.height
        self.rect.centerx = randrange(screen_size[0])

    def update(self):
        self.rect.top += 1
        if self.rect.top > screen_size[1]:
            self.reset()

pygame.init()
screen_size = 800,600
pygame.display.set_mode(screen_size, RESIZABLE)#FULLSCREEN
pygame.mouse.set_visible(0)

Weight_image = pygame.image.load('weight.png')
Weight_image = Weight_image.convert()

sprites = pygame.sprite.RenderUpdates()
sprites.add(Weight())

screen = pygame.display.get_surface()
bg = (255,255,255)#white
screen.fill(bg)
pygame.display.flip()


def clear_callback(surf, rect):
    surf.fill(bg, rect)

while True:
#检查退出事件
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()

    sprites.clear(screen, clear_callback)
    sprites.update()

    updates = sprites.draw(screen)
    pygame.display.update(updates)