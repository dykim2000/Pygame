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

BOXSIZE = 30
BOXWIDTH = 5
BOXHEIGHT = 5
BOARDWIDTH = 10
BOARDHEIGHT = 20
BLANK = '.'

COLORS =(BLUE, GREEN, RED, YELLOW)

MOVESIDEWAYSFREQ = 0.15
MOVEDOWNFREQ = 0.1

XMARGIN = (WIDTH - BOARDWIDTH * BOXSIZE) / 2
YMARGIN = (HEIGHT -BOARDHEIGHT * BOXSIZE) - 5

S = [['.....',
                     '.....',
                     '..OO.',
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

        GAME.fill(BLACK)
        TFont = pg.font.SysFont('Stencil', 100)
        global MFont
        MFont = pg.font.SysFont('monaco', 50)

        GOsurf = TFont.render("Tetris", True, GREEN)
        GAME.blit(GOsurf, ((WIDTH / 2) - 150, (HEIGHT / 2) - 50))

        pg.draw.rect(GAME, WHITE, pg.Rect((WIDTH / 2) - 60, (HEIGHT / 2) + 150, 120, 50))
        text = MFont.render("START", True, BLACK)
        GAME.blit(text, ((WIDTH / 2) - 55, (HEIGHT / 2) + 160))

        cur = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        if ((WIDTH / 2) - 60) + 120 > cur[0] > (WIDTH / 2) - 60 and ((HEIGHT / 2) + 150) + 50 > cur[1] > (HEIGHT / 2) + 150:
            print('버튼 포인트')
            if (click[0] == 1):
                print('버튼 클릭')
                runGame()
                check = False
        pg.display.flip()

def runGame():
    board = getBlankBoard()
    lastMoveDownTime = time.time()
    lastMoveSidewaysTime = time.time()
    lastFallTime = time.time()

    movingDown = False
    movingLeft = False
    movingRight = False

    score = 0
    level, fallsp = ingamesp(score)

    fallingPiece = getNewPiece()
    nextPiece = getNewPiece()

    check = True
    while check:
        if fallingPiece == None:
            fallingPiece = nextPiece
            nextPiece = getNewPiece()
            lastFallTime = time.time()

            if not CHpiece(board, fallingPiece):
                print('Game Over')
                return

        for event in pg.event.get():
            if event.type == pg.QUIT:
                check = False
                sys.exit()

            if event.type == pg.KEYUP:
                if event.key == pg.K_LEFT:
                    movingLeft = False
                elif event.key == pg.K_RIGHT:
                    movingRight = False
                elif event.key == pg.K_DOWN:
                    movingDown = False

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT and CHpiece(board, fallingPiece, X=-1):
                    fallingPiece['x'] -= 1
                    movingLeft = True
                    movingRight = False
                    lastMoveSidewaysTime = time.time()
                elif event.key == pg.K_RIGHT and CHpiece(board, fallingPiece, X=1):
                    fallingPiece['x'] += 1
                    movingRight = True
                    movingLeft = False
                    lastMoveSidewaysTime = time.time()

                elif event.key == pg.K_UP:
                    fallingPiece['rotation'] = (fallingPiece['rotation'] + 1) % len(PIECES[fallingPiece['shape']])
                    if not CHpiece(board, fallingPiece):
                        fallingPiece['rotation'] = (fallingPiece['rotation'] - 1) % len(PIECES[fallingPiece['shape']])
                elif event.key == pg.K_DOWN:
                    movingDown = True
                    if CHpiece(board, fallingPiece, Y=1):
                        fallingPiece['y'] += 1
                    lastMoveDownTime = time.time()
                elif event.key == pg.K_SPACE:
                    movingDown = False
                    movingLeft = False
                    movingRight = False
                    for i in range(1, BOARDHEIGHT):
                        if not CHpiece(board, fallingPiece, Y=i):
                            break
                    fallingPiece['y'] += i - 1

        if (movingLeft or movingRight) and time.time() - lastMoveSidewaysTime > MOVESIDEWAYSFREQ:
            if movingLeft and CHpiece(board, fallingPiece, X=-1):
                fallingPiece['x'] -= 1
            elif movingRight and CHpiece(board, fallingPiece, X=1):
                fallingPiece['x'] += 1
            lastMoveSidewaysTime = time.time()

        if movingDown and time.time() - lastMoveDownTime > MOVEDOWNFREQ and CHpiece(board, fallingPiece, Y=1):
            fallingPiece['y'] += 1
            lastMoveDownTime = time.time()

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

def ingamesp(score):
    level = int(score / 3) + 1
    fallsp = 0.6 -(level*0.1)+0.1
    return level, fallsp

def getNewPiece():
    shape = random.choice(list(PIECES.keys()))
    newPiece = {'shape': shape,
                'rotation': random.randint(0, len(PIECES[shape]) - 1),
                'x': int(BOARDWIDTH / 2) - int(BOXWIDTH / 2),
                'y': -2,
                'color': random.randint(0, len(COLORS)-1)}
    return newPiece

def drawBoard(board):
    pg.draw.rect(GAME, BLUE, (XMARGIN - 3, YMARGIN - 7, (BOARDWIDTH * BOXSIZE) + 8, (BOARDHEIGHT * BOXSIZE) + 8), 5)
    pg.draw.rect(GAME, BLACK, (XMARGIN, YMARGIN, BOXSIZE * BOARDWIDTH, BOXSIZE * BOARDHEIGHT))

    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            drawBox(x, y, board[x][y])

def drawStatus(score, level):
    scoreSurf = MFont.render('Score: %s' % score, True, WHITE)
    GAME.blit(scoreSurf, (WIDTH - 150, 20))

    levelSurf = MFont.render('Level: %s' % level, True, WHITE)
    GAME.blit(levelSurf, (WIDTH - 150, 60))

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

def drawBox(boxx, boxy, color, pixelx=None, pixely=None):
    if color == BLANK:
        return
    if pixelx == None and pixely == None:
        pixelx, pixely = convertToPixelCoords(boxx, boxy)
    pg.draw.rect(GAME, COLORS[color], (pixelx + 1, pixely + 1, BOXSIZE - 1, BOXSIZE - 1))

def addToBoard(board, piece):
    # fill in the board based on piece's location, shape, and rotation
    for x in range(BOXWIDTH):
        for y in range(BOXHEIGHT):
            if PIECES[piece['shape']][piece['rotation']][y][x] != BLANK:
                board[x + piece['x']][y + piece['y']] = piece['color']

def getBlankBoard():
    board = []
    for i in range(BOARDWIDTH):
        board.append([BLANK] * BOARDHEIGHT)
    return board

def isOnBoard(x, y):
    return x >= 0 and x < BOARDWIDTH and y < BOARDHEIGHT

def CHpiece(board, piece, X=0, Y=0):
    for x in range(BOXWIDTH):
        for y in range(BOXHEIGHT):
            isAboveBoard = y + piece['y'] + Y < 0
            if isAboveBoard or PIECES[piece['shape']][piece['rotation']][y][x] == BLANK:
                continue
            if not isOnBoard(x + piece['x'] + X, y + piece['y'] + Y):
                return False
            if board[x + piece['x'] + X][y + piece['y'] + Y] != BLANK:
                return False
    return True

def isCompleteLine(board, y):
    for x in range(BOARDWIDTH):
        if board[x][y] == BLANK:
            return False
    return True

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

def convertToPixelCoords(boxx, boxy):
    return (XMARGIN + (boxx * BOXSIZE)), (YMARGIN + (boxy * BOXSIZE))

main()