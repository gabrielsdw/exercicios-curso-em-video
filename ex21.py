import pygame as pg
from time import sleep
pg.init()
pg.mixer.init()
som = pg.mixer.Sound("salamisound-4638139-sfx-power-up-29-games.mp3")
som.play()
sleep(20)