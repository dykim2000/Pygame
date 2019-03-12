import pygame as pg
import sys
import random

size=[960,679]
width = size[0]
height = size[1]

'''player_width = 150
player_height = 150'''

def drawobj(obj,x,y):
    game.blit(obj,(x,y))

def run():
    check = True

    x=0
    y=0
    y_ch = 0

    bullet_xy=[]

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
                elif event.key == pg.K_s:
                    bullet_x = x
                    bullet_y = y+50
                    bullet_xy.append([bullet_x, bullet_y])

            if event.type == pg.KEYUP:
                if event.key == pg.K_UP or event.key == pg.K_DOWN:
                    y_ch = 0
        y+=y_ch
        if y<0:
            y=0
        elif y>height-100:
            y=height-100

        back_x-=8
        back_x2-=8
        if back_x == -width:
            back_x=width
        if back_x2 == -width:
            back_x2=width

        enemy_x-=15
        if enemy_x<=0:
            enemy_x = width
            enemy_y = random.randrange(0, height)

        if len(bullet_xy)!=0:
            for i,bxy in enumerate(bullet_xy):
                bxy[0]+=15
                bullet_xy[i][0]=bxy[0]
                if bxy[0]>=width:
                    bullet_xy.remove(bxy)

        drawobj(backgr,back_x,0)
        drawobj(backgr2, back_x2, 0)
        drawobj(player, x, y)
        drawobj(enemy,enemy_x,enemy_y)
        if len(bullet_xy)!=0:
            for bx,by in bullet_xy:
                drawobj(bullet,bx,by)
        pg.display.flip()
        fps.tick(60)

def main():
    pg.init()
    global game,fps
    global player,backgr,backgr2
    global enemy,bullet

    game = pg.display.set_mode((size))
    pg.display.set_caption('Shooting')
    fps = pg.time.Clock()

    player = pg.image.load('img/plane.png')
    player = pg.transform.scale(player,(120,70))
    backgr = pg.image.load('img/sky.png')
    backgr2 = backgr.copy()

    enemy = pg.image.load('img/enemy.png')
    enemy= pg.transform.scale(enemy,(100, 90))

    bullet = pg.image.load('img/bullet.png')
    bullet = pg.transform.rotate(bullet,180)
    bullet = pg.transform.scale(bullet, (50,10))

    run()

main()