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
pg.mixer.init()

gameSize = [800,480]
xx=gameSize[0]
yy=gameSize[1]
playSurface = pg.display.set_mode(gameSize)
pg.display.set_caption("Snake Game")
fps = pg.time.Clock()

file = 'song/eat.wav'
fd = 'song/end.mp3'
fl = 'song/up.wav'

def gameOver():
    check =True
    pg.mixer.music.load(fd)
    pg.mixer.music.play()
    while check:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        playSurface.fill(black)
        endFont = pg.font.SysFont('times new roman', 72)
        reFont = pg.font.SysFont('monaco', 70)

        GOsurf = endFont.render("Game Over", True, red)
        GOrect = GOsurf.get_rect()
        GOrect.midtop = (xx/2, (yy/2)-50)
        playSurface.blit(GOsurf, GOrect)

        Ssurf = endFont.render("Score  :  {0}".format(score), True, red)
        Srect = Ssurf.get_rect()
        Srect.midtop = (xx/2, (yy/2)+50)
        playSurface.blit(Ssurf, Srect)

        pg.draw.rect(playSurface,white,pg.Rect((xx/2)-60, (yy/2)+150, 120, 50))
        text=reFont.render("RE?",True,black)
        texts=text.get_rect()
        texts.center=((xx/2), (yy/2)+180)
        playSurface.blit(text,texts)

        cur = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        if ((xx/2)-60)+120>cur[0]>(xx/2)-60 and ((yy/2)+150)+50>cur[1]>(yy/2)+150:
            print('버튼 포인트')
            if(click[0]==1):
                print('버튼 클릭')
                main()
        pg.display.flip()

def showScore():
    SFont = pg.font.SysFont('monaco', 32)
    Ssurf = SFont.render("Score  :  {0}".format(score), True, black)
    Srect = Ssurf.get_rect()
    Srect.midtop = (80, 10)
    playSurface.blit(Ssurf, Srect)

    UFont = pg.font.SysFont('monaco', 32)
    Usurf = UFont.render("Speed  :  {0}".format(speed), True, black)
    Urect = Usurf.get_rect()
    Urect.midtop = (80, 50)
    playSurface.blit(Usurf, Urect)

    PFont = pg.font.SysFont('monaco', 32)
    Psurf = PFont.render("Level :  {0}".format(level), True, black)
    Prect = Psurf.get_rect()
    Prect.midtop = (80, 90)
    playSurface.blit(Psurf, Prect)

def inGame():
    check = True
    state = ''
    change = ''
    global score
    score = 0
    global speed
    speed = 5
    Size = 11
    global level
    level = 5

    snakeHead = [random.randrange(1, xx - 10), random.randrange(1, yy - 10)]
    snakeBody = [snakeHead]

    food = [random.randrange(1, xx - 10), random.randrange(1, yy - 10)]
    foodSpawn = True

    while check:
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
            state = 'RIGHT'
        elif change == 'LEFT' and state != 'RIGHT':
            state = 'LEFT'
        elif change == 'UP' and state != 'DOWN':
            state = 'UP'
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
            pg.mixer.music.load(file)
            pg.mixer.music.play()
            print('먹는다!')
            foodSpawn = False
            score += 1
        else:
            snakeBody.pop()

        if score == level:
            pg.mixer.music.load(fl)
            pg.mixer.music.play()
            level += 10
            speed += 1
            print('레벨 업! ' + str(speed))

        if foodSpawn == False:
            food = [random.randrange(1, xx - 10), random.randrange(1, yy - 10)]
            foodSpawn = True

        playSurface.fill(white)
        for pos in snakeBody:
            pg.draw.rect(playSurface, green, pg.Rect(pos[0], pos[1], Size, Size))

        pg.draw.rect(playSurface, red, pg.Rect(snakeHead[0], snakeHead[1], Size, Size))
        pg.draw.rect(playSurface, brown, pg.Rect(food[0], food[1], Size, Size))

        if drawHead.bottom > gameSize[1]:
            print('벽 조심')
            gameOver()
            check=False
        elif drawHead.top < 0:
            print('벽 조심')
            gameOver()
            check=False
        elif drawHead.left < 0:
            print('벽 조심')
            gameOver()
            check=False
        elif drawHead.right > gameSize[0]:
            print('벽 조심')
            gameOver()
            check=False

        for tail in snakeBody[1:]:
            if snakeHead == tail:
                print('꼬리 조심')
                gameOver()
                check = False
        showScore()
        pg.display.flip()
        fps.tick(30)

def main():
    check = True
    while check:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        playSurface.fill(black)
        endFont = pg.font.SysFont('times new roman', 100)
        reFont = pg.font.SysFont('monaco', 50)

        GOsurf = endFont.render("SNAKE GAME", True, green)
        GOrect = GOsurf.get_rect()
        GOrect.midtop = (xx / 2, (yy / 2) - 50)
        playSurface.blit(GOsurf, GOrect)

        pg.draw.rect(playSurface, white, pg.Rect((xx / 2) - 60, (yy / 2) + 150, 120, 50))
        text = reFont.render("START", True, black)
        texts = text.get_rect()
        texts.center = ((xx / 2), (yy / 2) + 180)
        playSurface.blit(text, texts)

        cur = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        if ((xx / 2) - 60) + 120 > cur[0] > (xx / 2) - 60 and ((yy / 2) + 150) + 50 > cur[1] > (yy / 2) + 150:
            print('버튼 포인트')
            if (click[0] == 1):
                print('버튼 클릭')
                inGame()
                check=False
        pg.display.flip()

main()