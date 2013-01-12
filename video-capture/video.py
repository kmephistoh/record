#!/usr/bin/env python2
# -*- coding:utf-8 -*-
import sys
import pygame
import Image
from  pygame.locals import *
import cv
import PIL

camera = cv.CreateCameraCapture(0)


def get_image():
    im = cv.QueryFrame(camera)
    return cv.ShowImage("ipl2pil", im)
fps = 30.0
pygame.init()
window = pygame.display.set_mode((640, 480))
pygame.display.set_caption("WebCam Demo")
screen = pygame.display.get_surface()
while 1:
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT or event.type == KEYDOWN:
            sys.exit(0)
    im = get_image()
    pg_img = pygame.image.frombuffer(im.tostring(), im.size, im.mode)
    screen.blit(pg_img, (0, 0))
    pygame.display.flip()
    pygame.time.delay(int(1000 * 1.0 / fps))
