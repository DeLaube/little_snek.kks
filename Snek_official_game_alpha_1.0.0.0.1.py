import random, pygame, sys
from pygame.locals import *

#             R    G    B
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARKGRAY = (40, 40, 40)

class Spiel:
    def __init__(self, groesse):
        self.felder = [[0 for j in range(groesse)] for i in range(groesse)]

        for i in range(groesse):
            self.felder[0][i] = 1
            self.felder[groesse - 1][i] = 1
            self.felder[i][0] = 1
            self.felder[i][groesse - 1] = 1

        self.snek = [{'x': 9, 'y': 12}, {'x': 8, 'y': 12}]
        self.snek_food = {'x': random.randint(1,25), 'y': random.randint(1,25)}

    def verschieben(self, nfeld):
        for i in range(len(self.snek)):
            temp = self.snek[i]
            self.snek[i] = nfeld
            nfeld = temp

    def hinzufuegen(self, nfeld):
        self.snek.insert(0, nfeld)

def makeGUI():
    FPS = 10
    WINDOWWIDTH = 540
    WINDOWHEIGHT = WINDOWWIDTH
    CELLSIZE = 20

    assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
    assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."
    CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
    CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)

    my_feld = Spiel(CELLWIDTH)

    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Snek')

    # Text für den Endbildschirm
    fontObj = pygame.font.Font('freesansbold.ttf', 32)
    textSurfaceObj = fontObj.render('Kollision!', True, RED, BLUE)
    textSurfaceObj2 = fontObj.render('Click "Esc" to quit.', True, (0, 0, 0))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj2 = textSurfaceObj2.get_rect()
    textRectObj.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
    textRectObj2.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2 + 50)
    pygame.key.set_repeat(50, 50)

    kup = {'x': -1, 'y': 0}
    kdown = {'x': 1, 'y': 0}
    kright = {'x': 0, 'y': 1}
    kleft = {'x': 0, 'y': -1}
    richtung = kdown

    def game_over():
        # Game Over
        # Text für den Endbildschirm
        fontObj = pygame.font.Font('freesansbold.ttf', 40)
        textSurfaceObj = fontObj.render('Little snek iz ded.. ', True, WHITE, RED)
        textSurfaceObj2 = fontObj.render('Click "Esc" to quit life', True, WHITE)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj2 = textSurfaceObj2.get_rect()

        textRectObj.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
        textRectObj2.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2 + 50)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        DISPLAYSURF.blit(textSurfaceObj2, textRectObj2)
        pygame.display.update()
        while True:
            for event in pygame.event.get():  # event handling loop
                if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()

    while True:  # the main game loop
        DISPLAYSURF.fill(BLACK)

        npunkt = {'x': my_feld.snek[0]['x'] + richtung['x'], 'y': my_feld.snek[0]['y'] + richtung['y']}
        my_feld.verschieben(npunkt)

        for event in pygame.event.get():  # event handling loop

            if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if richtung == kdown:
                        pass
                    else:
                        richtung = kup

                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if richtung == kup:
                        pass
                    else:
                        richtung = kdown

                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if richtung == kright:
                        pass
                    else:
                        richtung = kleft

                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if richtung == kleft:
                        pass
                    else:
                        richtung = kright

        # Gitter im Spielfeld
        for x in range(0, WINDOWWIDTH, CELLSIZE):  # draw vertical lines
            pygame.draw.line(DISPLAYSURF, BLACK, (x, 0), (x, WINDOWHEIGHT))
        for y in range(0, WINDOWHEIGHT, CELLSIZE):  # draw horizontal lines
            pygame.draw.line(DISPLAYSURF, BLACK, (0, y), (WINDOWWIDTH, y))


        # Rand
        for i in range(len(my_feld.felder)):
            for j in range(len(my_feld.felder[i])):
                if my_feld.felder[i][j] == 1:
                    x, y = board_to_pixel_koord(i, j, CELLSIZE)
                    appleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
                    pygame.draw.rect(DISPLAYSURF, GREEN, appleRect)

        # Kollision mit food
        for i in range(len(my_feld.snek)):
            if (my_feld.snek[i]['x'] == my_feld.snek_food['x'] and my_feld.snek[i]['y'] == my_feld.snek_food['y']):
                if (my_feld.snek_food['x'] == 1 or my_feld.snek_food['x'] == 25 or my_feld.snek_food['y'] == 1 or
                    my_feld.snek_food['y'] == 25):
                    npunkt = {'x': my_feld.snek[0]['x'] + richtung['x'], 'y': my_feld.snek[0]['y'] + richtung['y']}
                    my_feld.snek_food['x'] = random.randint(1, 25)
                    my_feld.snek_food['y'] = random.randint(1, 25)
                    my_feld.hinzufuegen(npunkt)

                else:
                    npunkt = {'x': my_feld.snek[0]['x'] + richtung['x'], 'y': my_feld.snek[0]['y'] + richtung['y']}
                    my_feld.snek_food['x'] = random.randint(1, 25)
                    my_feld.snek_food['y'] = random.randint(1, 25)
                    my_feld.hinzufuegen(npunkt)


                # Stopp bei Kollision mit Wand
        if my_feld.snek[0]['x'] == 0 or my_feld.snek[0]['x'] == 26 or \
            my_feld.snek[0]['y'] == 0 or my_feld.snek[0]['y'] == 26:
            game_over()

        for i in range(1, len(my_feld.snek)):
            if my_feld.snek[0] == my_feld.snek[i]:
                game_over()

        for i in my_feld.snek:
            make_rectangle_green(i, DISPLAYSURF, CELLSIZE)

        make_rectangle_red(my_feld.snek_food, DISPLAYSURF, CELLSIZE)

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def board_to_pixel_koord(i, j, width):
    return j * width, i * width


def pixel_to_board_koord(x, y, width):
    return y // width, x // width


def make_rectangle_red(liste, display, size):
    x, y = board_to_pixel_koord(liste['x'], liste['y'], size)
    the_rect = pygame.Rect(x, y, size, size)
    pygame.draw.rect(display, RED, the_rect)


def make_rectangle_green(dict, display, size):
    x, y = board_to_pixel_koord(dict['x'], dict['y'], size)
    the_rect = pygame.Rect(x, y, size, size)
    pygame.draw.rect(display, GREEN, the_rect)


def make_rectangle_blue(dict, display, size):
    x, y = board_to_pixel_koord(dict['x'], dict['y'], size)
    the_rect = pygame.Rect(x, y, size, size)
    pygame.draw.rect(display, BLUE, the_rect)



if __name__ == '__main__':
    makeGUI()