import pygame
import time
pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play(loops=0)
while pygame.mixer.music.get_busy()
    time.sleep(1)