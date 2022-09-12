#Faça um programa em Python que abra e reproduza um áudio de um arquivo .mp3

import pygame

pygame.init()
pygame.mixer.music.load('dbz.mp3')
pygame.mixer.music.play()
pygame.event.wait()