import pygame as pg
import random, time, sys

WHITE       = (255, 255, 255)
BLACK       = (  0,   0,   0)
RED         = (155,   0,   0)
GREEN       = (  0, 155,   0)
BLUE        = (  0,   0, 155)
YELLOW      = (155, 155,   0)

SIZE = [800,640]
WIDTH = SIZE[0]
HEIGHT = SIZE[1]

# 블럭 디자인 값
BOXSIZE = 30
BOXWIDTH = 5
BOXHEIGHT = 5

# 보드 디자인 값
BOARDWIDTH = 10
BOARDHEIGHT = 20
BLANK = '.'

COLORS =(BLUE, GREEN, RED, YELLOW)

XMARGIN = (WIDTH - BOARDWIDTH * BOXSIZE) / 2
YMARGIN = (HEIGHT -BOARDHEIGHT * BOXSIZE) - 5

S = [['.....',
                     '.....',
                     '..0O.',
                     '.OO..',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..OO.',
                     '...O.',
                     '.....']]

Z= [['.....',
                     '.....',
                     '.OO..',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OO..',
                     '.O...',
                     '.....']]

I = [['..O..',
                     '..O..',
                     '..O..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     'OOOO.',
                     '.....',
                     '.....']]

O = [['.....',
                     '.....',
                     '.OO..',
                     '.OO..',
                     '.....']]

J = [['.....',
                     '.O...',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..OO.',
                     '..O..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '...O.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..O..',
                     '.OO..',
                     '.....']]

L = [['.....',
                     '...O.',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..O..',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '.O...',
                     '.....'],
                    ['.....',
                     '.OO..',
                     '..O..',
                     '..O..',
                     '.....']]

T= [['.....',
                     '..O..',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..OO.',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '..O..',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OO..',
                     '..O..',
                     '.....']]

PIECES = {'S': S,
          'Z': Z,
          'J': J,
          'L': L,
          'I': I,
          'O': O,
          'T': T}

def end(sc):
    check = True
    while check:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                check = False
                sys.exit()

        GAME.fill(BLACK)
        endFont = pg.font.SysFont('times new roman', 72)
        reFont = pg.font.SysFont('monaco', 70)

        GOsurf = endFont.render("Game Over", True, RED)
        GAME.blit(GOsurf, ( (WIDTH/ 2) - 150 , (HEIGHT / 2) - 50) )

        Ssurf = endFont.render("Score  :  {0}".format(sc), True, RED)
        GAME.blit(Ssurf, ( (WIDTH / 2) - 130 , (HEIGHT / 2) + 50) )

        pg.draw.rect(GAME, WHITE, pg.Rect((WIDTH / 2) - 60, (HEIGHT / 2) + 150, 120, 50))
        text = reFont.render("RE?", True, BLACK)
        GAME.blit(text, ( (WIDTH / 2)-45 , (HEIGHT / 2)+155 ) )

        cur = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        if ((WIDTH / 2) - 60) + 120 > cur[0] > (WIDTH/ 2) - 60 and ((HEIGHT / 2) + 150) + 50 > cur[1] > (HEIGHT / 2) + 150:
            print('버튼 포인트')
            if (click[0] == 1):
                print('버튼 클릭')
                runGame()
        pg.display.flip()

def main():
    global FPS, GAME

    pg.init()
    GAME = pg.display.set_mode(SIZE)
    pg.display.set_caption('Tetris')
    FPS = pg.time.Clock()

    check = True
    while check:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                check = False
                sys.exit()

        GAME.fill(BLACK) # 검은색 배경
        TFont = pg.font.SysFont('Stencil', 100) # 타이틀 폰트
        GOsurf = TFont.render("Tetris", True, GREEN)
        GAME.blit(GOsurf, ((WIDTH / 2) - 150, (HEIGHT / 2) - 50))

        global MFont # 메인 폰트
        MFont = pg.font.SysFont('monaco', 50)

        pg.draw.rect(GAME, WHITE, pg.Rect((WIDTH / 2) - 60, (HEIGHT / 2) + 150, 120, 50)) # 버튼 디자인
        text = MFont.render("START", True, BLACK) # 버튼 글자
        GAME.blit(text, ((WIDTH / 2) - 55, (HEIGHT / 2) + 160))

        cur = pg.mouse.get_pos() # 커서 위치
        click = pg.mouse.get_pressed() # 마우스 클릭
        if ((WIDTH / 2) - 60) + 120 > cur[0] > (WIDTH / 2) - 60 and ((HEIGHT / 2) + 150) + 50 > cur[1] > (HEIGHT / 2) + 150:
            if (click[0] == 1):
                runGame()
                check = False
        pg.display.flip()

def runGame():
    board = getBlankBoard() #보드 디자인

    lastFallTime = time.time()

    score = 0
    level, fallsp = ingamesp(score) # 게임 레벨 과 블럭 떨어지는 속도 지정

    # 떨어지는 블럭 과 다음 블럭 지정
    fallingPiece = getNewPiece()
    nextPiece = getNewPiece()

    check = True
    while check:
        if fallingPiece == None: # 떨어지는 블럭이 없다면 재갱신
            fallingPiece = nextPiece
            nextPiece = getNewPiece()
            lastFallTime = time.time()

            if not CHpiece(board, fallingPiece):
                end(score)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                check = False
                sys.exit()

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT and CHpiece(board, fallingPiece, X=-1):
                    fallingPiece['x'] -= 1
                elif event.key == pg.K_RIGHT and CHpiece(board, fallingPiece, X=1):
                    fallingPiece['x'] += 1
                elif event.key == pg.K_DOWN:
                    if CHpiece(board, fallingPiece, Y=1):
                        fallingPiece['y'] += 1
                elif event.key == pg.K_SPACE:
                    for i in range(BOARDHEIGHT):
                        if not CHpiece(board, fallingPiece, Y=i):
                            break
                    fallingPiece['y'] += i - 1
                elif event.key == pg.K_UP:
                    fallingPiece['rotation'] = (fallingPiece['rotation'] + 1) % len(PIECES[fallingPiece['shape']])
                    if not CHpiece(board, fallingPiece):
                        fallingPiece['rotation'] = (fallingPiece['rotation'] - 1) % len(PIECES[fallingPiece['shape']])


        if time.time() - lastFallTime > fallsp:
            # see if the piece has landed
            if not CHpiece(board, fallingPiece, Y=1):
                # falling piece has landed, set it on the board
                addToBoard(board, fallingPiece)
                score += removeCompleteLines(board)
                level, fallsp = ingamesp(score)
                fallingPiece = None
            else:
                # piece did not land, just move the piece down
                fallingPiece['y'] += 1
                lastFallTime = time.time()

        GAME.fill(BLACK)
        drawBoard(board)
        drawStatus(score, level)
        drawNextPiece(nextPiece)
        if fallingPiece != None:
            drawPiece(fallingPiece)

        pg.display.flip()
        FPS.tick(30)

def CHpiece(board, piece, X=0, Y=0):
    for x in range(BOXWIDTH):
        for y in range(BOXHEIGHT):
            ispiece = y + piece['y'] + Y < 0
            if ispiece or PIECES[piece['shape']][piece['rotation']][y][x] == BLANK: # 블럭의 Y값 혹은 보드 안에 있을 경우
                continue
            if not isOnBoard(x + piece['x'] + X, y + piece['y'] + Y): # 보드 안에 블럭 상속
                return False
            if board[x + piece['x'] + X][y + piece['y'] + Y] != BLANK: # 블럭 쌓기
                return False
    return True

def getBlankBoard():
    board = []
    for i in range(BOARDWIDTH):
        board.append([BLANK] * BOARDHEIGHT)
    return board

def ingamesp(score):
    level = int(score/3) + 1 # 3배수 단위
    if level < 6:
        fallsp = 0.6 -(level*0.1)+0.1
    else:
        fallsp = 0.1

    return level, fallsp

def getNewPiece():
    shape = random.choice(list(PIECES.keys())) # 블럭 타입 랜덤 지정
    newPiece = {'shape': shape,
                'rotation': random.randint(0, len(PIECES[shape]) - 1),
                'x': int(BOARDWIDTH / 2) - int(BOXWIDTH / 2),
                'y': -2,
                'color': random.randint(0, len(COLORS)-1)}
    return newPiece

def drawStatus(score, level):
    scoreSurf = MFont.render('Score: %s' % score, True, WHITE)
    GAME.blit(scoreSurf, (WIDTH - 150, 20))

    levelSurf = MFont.render('Level: %s' % level, True, WHITE)
    GAME.blit(levelSurf, (WIDTH - 150, 60))

def drawBoard(board):
    pg.draw.rect(GAME, BLUE, (XMARGIN - 3, YMARGIN - 7, (BOARDWIDTH * BOXSIZE) + 8, (BOARDHEIGHT * BOXSIZE) + 8), 5)

    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            drawBox(x, y, board[x][y])

def drawBox(boxx, boxy, color, pixelx=None, pixely=None):
    if color == BLANK:
        return
    if pixelx == None and pixely == None:
        pixelx, pixely = convertToPixelCoords(boxx, boxy)
    pg.draw.rect(GAME, COLORS[color], (pixelx + 1, pixely + 1, BOXSIZE - 1, BOXSIZE - 1))


def drawNextPiece(piece):
    MFont = pg.font.SysFont('monaco', 50)
    nextSurf = MFont.render('Next:', True, WHITE)
    GAME.blit(nextSurf, (WIDTH - 120, 100))

    drawPiece(piece, pixelx=WIDTH-120, pixely=150)

def drawPiece(piece, pixelx=None, pixely=None):
    shapeToDraw = PIECES[piece['shape']][piece['rotation']]
    if pixelx == None and pixely == None:
        pixelx, pixely = convertToPixelCoords(piece['x'], piece['y'])

    for x in range(BOXWIDTH):
        for y in range(BOXHEIGHT):
            if shapeToDraw[y][x] != BLANK:
                drawBox(None, None, piece['color'], pixelx + (x * BOXSIZE), pixely + (y * BOXSIZE))

def addToBoard(board, piece):
    # fill in the board based on piece's location, shape, and rotation
    for x in range(BOXWIDTH):
        for y in range(BOXHEIGHT):
            if PIECES[piece['shape']][piece['rotation']][y][x] != BLANK:
                board[x + piece['x']][y + piece['y']] = piece['color']

def isOnBoard(x, y):
    return x >= 0 and x < BOARDWIDTH and y < BOARDHEIGHT


def removeCompleteLines(board):
    numLinesRemoved = 0
    y = BOARDHEIGHT - 1
    while y >= 0:
        if isCompleteLine(board, y):
            for pullDownY in range(y, 0, -1):
                for x in range(BOARDWIDTH):
                    board[x][pullDownY] = board[x][pullDownY-1]
            # Set very top line to blank.
            for x in range(BOARDWIDTH):
                board[x][0] = BLANK
            numLinesRemoved += 1
        else:
            y -= 1
    return numLinesRemoved

def isCompleteLine(board, y):
    for x in range(BOARDWIDTH):
        if board[x][y] == BLANK:
            return False
    return True

def convertToPixelCoords(boxx, boxy):
    return (XMARGIN + (boxx * BOXSIZE)), (YMARGIN + (boxy * BOXSIZE))

main()