import pygame as pg
import sys

white = (255,255,255)
size=[960,679]
width = size[0]
height = size[1]
bwidth = width

pg.init()

def back(bg,x,y):
    game.blit(bg,(x,y))

def air(x,y):
    game.blit(playerrly,(x,y))

def run():
    check = True

    x=width * 0.05
    y=height*0.8
    y_ch = 0

    back_x=0
    back_x2=bwidth

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

        if back_x == -bwidth:
            back_x=bwidth
        if back_x2 == -bwidth:
            back_x2=bwidth

        #game.fill(white)
        back(backgr,back_x,0)
        back(backgr2, back_x2, 0)
        air(x,y)
        pg.display.flip()
        fps.tick(60)

def main():
    global game,fps,playerrly,backgr,backgr2

    game=pg.display.set_mode((width,height))
    pg.display.set_caption('Shooting')
    player = pg.image.load('img/plane.png')
    playerrly=pg.transform.scale(player,(120,90))
    backgr=pg.image.load('img/sky.png')
    backgr2=backgr.copy()
    fps = pg.time.Clock()

    run()

main()