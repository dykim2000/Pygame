import pygame as pg
import sys
import random

size=[960,679]

width = size[0]
height = size[1]

pg.init()

def drawobj(obj,x,y):
    game.blit(obj,(x,y))

def run():
    check = True

    x=width * 0.05
    y=height*0.8
    y_ch = 0

    back_x=0
    back_x2=width

    enemy_x=width
    enemy_y=random.randrange(0,height)


    while check:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    y_ch = -15
                elif event.key == pg.K_DOWN:
                    y_ch = 15
            if event.type == pg.KEYUP:
                if event.key == pg.K_UP or event.key == pg.K_DOWN:
                    y_ch = 0

        y+=y_ch

        back_x-=8
        back_x2-=8

        enemy_x-=15
        if enemy_x<=0:
            enemy_x = width
            enemy_y = random.randrange(0, height)


        if back_x == -width:
            back_x=width
        if back_x2 == -width:
            back_x2=width

        drawobj(backgr,back_x,0)
        drawobj(backgr2, back_x2, 0)
        drawobj(enemyrly,enemy_x,enemy_y)
        drawobj(playerrly,x,y)
        pg.display.flip()
        fps.tick(60)

def main():
    global game,fps
    global playerrly,backgr,backgr2
    global enemyrly,bulletrly

    game = pg.display.set_mode((size))
    pg.display.set_caption('Shooting')
    player = pg.image.load('img/plane.png')
    playerrly = pg.transform.scale(player,(120,90))
    backgr = pg.image.load('img/sky.png')
    backgr2 = backgr.copy()
    enemy = pg.image.load('img/enemy.png')
    enemyrly = pg.transform.scale(enemy,(120, 90))
    bullet = pg.image.load('img/bullet.png')
    bulletrly = pg.transform.rotate(bullet,180)
    bulletrly = pg.transform.scale(bullet, (120,90))
    fps = pg.time.Clock()

    run()

main()