import random
import sys
import pygame as pg

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

pg.init()
size=[800,480]
windowSurface = pg.display.set_mode(size)
pg.display.set_caption('Sample')
mainClock = pg.time.Clock()

foodCounter = 0
NEWFOOD = 40
FOODSIZE = 20

player = pg.Rect(random.randint(0,size[0]//10), random.randint(0,size[1]//10), 50, 50)

foods = []
for i in range(0, 20):
    foods.append(pg.Rect(random.randint(0, size[0] - FOODSIZE),
                             random.randint(0, size[1] - FOODSIZE),
                             FOODSIZE, FOODSIZE))

moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 5

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                moveRight = False
                moveLeft = True
            if event.key == pg.K_RIGHT:
                moveRight = True
                moveLeft = False
            if event.key == pg.K_UP:
                moveUp = True
                moveDown = False
            if event.key == pg.K_DOWN:
                moveUp = False
                moveDown = True

        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT:
                moveLeft = False
            if event.key == pg.K_RIGHT:
                moveRight = False
            if event.key == pg.K_UP:
                moveUp = False
            if event.key == pg.K_DOWN:
                moveDown = False

    foodCounter += 1
    if foodCounter >= NEWFOOD:
        foodCounter = 0
        foods.append(pg.Rect(random.randint(0, size[0] - FOODSIZE)
                                 , random.randint(0, size[1] - FOODSIZE)
                                 , FOODSIZE, FOODSIZE))

    windowSurface.fill(BLACK)

    if moveDown and player.bottom < size[1]:
        player.top += MOVESPEED
    elif moveUp and player.top > 0:
        player.top -= MOVESPEED
    elif moveLeft and player.left > 0:
        player.left -= MOVESPEED
    elif moveRight and player.right < size[0]:
        player.left += MOVESPEED

    pg.draw.rect(windowSurface, WHITE, player)

    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)

    for i in range(len(foods)):
        pg.draw.rect(windowSurface, GREEN, foods[i])

    pg.display.update()
    mainClock.tick(60)
