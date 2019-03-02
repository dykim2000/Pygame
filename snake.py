import pygame as pg
import sys
import random
import time

red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
brown = (165, 42, 42)

pg.init()
gameSize = [800,480]
playSurface = pg.display.set_mode(gameSize)
pg.display.set_caption("Snake Game")
fps = pg.time.Clock()

snakeHead = [random.randrange(1,gameSize[0]-10),random.randrange(1,gameSize[1]-10)]
snakeBody = [snakeHead]

food = [random.randrange(1,gameSize[0]-10),random.randrange(1,gameSize[1]-10)]
foodSpawn = True

state = ''
change = ''
score = 0
speed=5
Size=10
level=10

def gameOver():
    playSurface.fill(black)
    myFont = pg.font.SysFont('times new roman', 72)

    GOsurf = myFont.render("Game Over", True, red)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (gameSize[0]/2, gameSize[1]/2)
    playSurface.blit(GOsurf, GOrect)

    Ssurf = myFont.render("Score  :  {0}".format(score), True, red)
    Srect = Ssurf.get_rect()
    Srect.midtop = ((gameSize[0] / 2), (gameSize[1] / 2) + 100)
    playSurface.blit(Ssurf, Srect)
    pg.display.flip()
    time.sleep(5)
    pg.quit()
    sys.exit()

def showScore():
    SFont = pg.font.SysFont('monaco', 32)
    Ssurf = SFont.render("Score  :  {0}".format(score), True, black)
    Srect = Ssurf.get_rect()
    Srect.midtop = (80, 10)
    playSurface.blit(Ssurf, Srect)


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                change = 'RIGHT'
            if event.key == pg.K_LEFT:
                change = 'LEFT'
            if event.key == pg.K_UP:
                change = 'UP'
            if event.key == pg.K_DOWN:
                change = 'DOWN'

    if change == 'RIGHT' and state != 'LEFT':
        state='RIGHT'
    elif change == 'LEFT' and state != 'RIGHT':
        state='LEFT'
    elif change == 'UP' and state != 'DOWN':
        state='UP'
    elif change == 'DOWN' and state != 'UP':
        state = 'DOWN'

    if state == 'RIGHT':
        snakeHead[0] += speed
    elif state == 'LEFT':
        snakeHead[0] -= speed
    elif state == 'DOWN':
        snakeHead[1] += speed
    elif state == 'UP':
        snakeHead[1] -= speed

    drawHead = pg.Rect(snakeHead[0], snakeHead[1], Size, Size)
    drawFood = pg.Rect(food[0], food[1], Size, Size)

    snakeBody.insert(0, list(snakeHead))

    if drawHead.colliderect(drawFood):
        print('먹는다!')
        foodSpawn = False
        score += 1
    else:
        snakeBody.pop()

    if score==level:
        level+=10
        speed+=1
        print('레벨 업! ' + str(speed))

    if foodSpawn == False:
        food = [random.randrange(1,gameSize[0]-10),random.randrange(1,gameSize[1]-10)]
        foodSpawn = True

    playSurface.fill(white)
    for pos in snakeBody:
        pg.draw.rect(playSurface, green, pg.Rect(pos[0], pos[1], Size, Size))

    pg.draw.rect(playSurface, red, pg.Rect(snakeHead[0], snakeHead[1], Size, Size))
    pg.draw.rect(playSurface, brown, pg.Rect(food[0], food[1], Size, Size))

    if drawHead.bottom>gameSize[1]:
        print('벽 조심')
        gameOver()
    elif drawHead.top<0:
        print('벽 조심')
        gameOver()
    elif drawHead.left<0:
        print('벽 조심')
        gameOver()
    elif drawHead.right>gameSize[0]:
        print('벽 조심')
        gameOver()

    for tail in snakeBody[1:]:
        if snakeHead == tail:
            print('꼬리 조심')
            gameOver()

    showScore()
    pg.display.flip()
    fps.tick(30)