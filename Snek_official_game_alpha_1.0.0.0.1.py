import random, pygame, sys
from pygame.locals import *
#             R    G    B
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (220, 220, 220)

bg = pygame.image.load("little_snek.jpg")
gowbg = pygame.image.load("snekizded.jpg")
goebg = pygame.image.load("snekeat.jpg")
top_score_liste = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
top_score_liste = sorted(top_score_liste)

class Spiel:
    def __init__(self, groesse):
        self.felder = [[0 for j in range(groesse)] for i in range(groesse)]

        for i in range(groesse):
            self.felder[0][i] = 1
            self.felder[groesse - 1][i] = 1
            self.felder[i][0] = 1
            self.felder[i][groesse - 1] = 1

        self.snek = [{'x': 12, 'y': 12}, {'x': 11, 'y': 12}, {'x': 10, 'y': 12}, {'x': 9, 'y': 12}, {'x': 8, 'y': 12}]
        self.snek_food = {'x': random.randint(1, 25), 'y': random.randint(1, 25)}

    def verschieben(self, nfeld):
        for i in range(len(self.snek)):
            temp = self.snek[i]
            self.snek[i] = nfeld
            nfeld = temp

    def hinzufuegen(self, nfeld):
        self.snek.insert(0, nfeld)
def add_score(list,score):
    list.append(score)

def sort_list():
    global top_score_liste
    top_score_liste = sorted(top_score_liste)



def makeGUI(FPS=10):
    FPS = FPS
    WINDOWWIDTH = 540
    WINDOWHEIGHT = WINDOWWIDTH
    CELLSIZE = 20
    CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Snek')

    my_feld = Spiel(CELLWIDTH)



    kup = {'x': -1, 'y': 0}
    kdown = {'x': 1, 'y': 0}
    kright = {'x': 0, 'y': 1}
    kleft = {'x': 0, 'y': -1}
    richtung = kdown

    def game_over_wall():
        # Game Over wenn in Wand
        # Text für den Endbildschirm
        DISPLAYSURF.fill(BLACK)
        fontObj = pygame.font.Font('freesansbold.ttf', 40)
        fontObj2 = pygame.font.Font('freesansbold.ttf', 30)
        textSurfaceObj = fontObj.render("Little snek iz ded..", True, RED)
        textSurfaceObj2 = fontObj.render('Click "Esc" to quit life', True, RED)
        textSurfaceObj3 = fontObj.render("Score:  " + str(score), True, RED)
        textSurfaceObj4 = fontObj2.render('Press "Space" to go back to menu', True, RED)

        textRectObj = textSurfaceObj.get_rect()
        textRectObj2 = textSurfaceObj2.get_rect()
        textRectObj3 = textSurfaceObj3.get_rect()
        textRectObj4 = textSurfaceObj4.get_rect()

        textRectObj.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
        textRectObj2.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2 + 50)
        textRectObj3.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 6 + 50)
        textRectObj4.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2 + 100)

        DISPLAYSURF.blit(gowbg, [-50,90])
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        DISPLAYSURF.blit(textSurfaceObj2, textRectObj2)
        DISPLAYSURF.blit(textSurfaceObj3, textRectObj3)
        DISPLAYSURF.blit(textSurfaceObj4, textRectObj4)

        pygame.display.update()
        while True:
            for event in pygame.event.get():  # event handling loop
                if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        selection_menu()

    def game_over_eat_itself():
        # Game Over bei Kollision mit Körper
        # Text für den Endbildschirm
        DISPLAYSURF.fill(BLACK)
        fontObj = pygame.font.Font('freesansbold.ttf', 40)
        fontObj2 = pygame.font.Font('freesansbold.ttf', 30)
        textSurfaceObj = fontObj.render('Click "Esc" to quit life', True, RED)
        textSurfaceObj2 = fontObj.render("Little Snek iz ded..", True, RED)
        textSurfaceObj3 = fontObj.render("Score:  " + str(score), True, RED)
        textSurfaceObj4 = fontObj2.render('Press "Space" to go back to menu', True, RED)

        textRectObj = textSurfaceObj.get_rect()
        textRectObj2 = textSurfaceObj2.get_rect()
        textRectObj3 = textSurfaceObj3.get_rect()
        textRectObj4 = textSurfaceObj4.get_rect()

        textRectObj.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 1.2)
        textRectObj2.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 1.4 )
        textRectObj3.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 8 - 5)
        textRectObj4.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2 + 220)

        DISPLAYSURF.blit(goebg, [90, 90])
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        DISPLAYSURF.blit(textSurfaceObj2, textRectObj2)
        DISPLAYSURF.blit(textSurfaceObj3, textRectObj3)
        DISPLAYSURF.blit(textSurfaceObj4, textRectObj4)

        pygame.display.update()
        while True:
            for event in pygame.event.get():  # event handling loop
                if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        selection_menu()

    while True:  # the main game loop
        global top_score_liste
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

        # Rand
        for i in range(len(my_feld.felder)):
            for j in range(len(my_feld.felder[i])):
                if my_feld.felder[i][j] == 1:
                    x, y = board_to_pixel_koord(i, j, CELLSIZE)
                    appleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
                    pygame.draw.rect(DISPLAYSURF, GREEN, appleRect)
        score = len(my_feld.snek)-5

        fontObj = pygame.font.Font('freesansbold.ttf', 18)
        textSurfaceObj = fontObj.render("SCORE: "+str(score), True, RED)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (WINDOWWIDTH / 2 +140, WINDOWHEIGHT / 2 - 260)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)


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
            score = len(my_feld.snek) - 5
            add_score(top_score_liste,score)
            sort_list()
            game_over_wall()

        #Stopp bei Kollision mit Körper
        for i in range(1, len(my_feld.snek)):
            if my_feld.snek[0] == my_feld.snek[i]:
                score = len(my_feld.snek) - 5
                add_score(top_score_liste, score)
                sort_list()
                game_over_eat_itself()

        #Farbe des Körpers
        for i in my_feld.snek:
            make_rectangle_green(i, DISPLAYSURF, CELLSIZE)
        #Farbe des Foods
        make_rectangle_red(my_feld.snek_food, DISPLAYSURF, CELLSIZE)

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def score_menu():
    WINDOWWIDTH = 540
    WINDOWHEIGHT = WINDOWWIDTH
    pygame.init()
    pygame.display.set_caption("Snek")
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    fontObj = pygame.font.Font('freesansbold.ttf', 35)
    fontdifficulty = pygame.font.Font('freesansbold.ttf', 20)
    textSurfaceObj = fontObj.render("Top 10 Scores", True, GREEN)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2 -200 )
    DISPLAYSURF.fill(BLACK)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)

    textSurfaceObj2 = fontdifficulty.render("1.  "+str(top_score_liste[-1]), True, GREEN)
    textRectObj2 = textSurfaceObj2.get_rect()
    textRectObj2.center = ((30 + (80 / 2)), (110 + (40 / 2)))
    DISPLAYSURF.blit(textSurfaceObj2, textRectObj2)

    textSurfaceObj3 = fontdifficulty.render("2.  "+str(top_score_liste[-2]), True, GREEN)
    textRectObj3 = textSurfaceObj3.get_rect()
    textRectObj3.center = ((30 + (80 / 2)), (150 + (40 / 2)))
    DISPLAYSURF.blit(textSurfaceObj3, textRectObj3)

    textSurfaceObj5 = fontdifficulty.render("3.  "+str(top_score_liste[-3]), True, GREEN)
    textRectObj5 = textSurfaceObj5.get_rect()
    textRectObj5.center = ((30 + (80 / 2)), (190 + (40 / 2)))
    DISPLAYSURF.blit(textSurfaceObj5, textRectObj5)

    textSurfaceObj6 = fontdifficulty.render("4.  "+str(top_score_liste[-4]), True, GREEN)
    textRectObj6 = textSurfaceObj6.get_rect()
    textRectObj6.center = ((30 + (80 / 2)), (230 + (40 / 2)))
    DISPLAYSURF.blit(textSurfaceObj6, textRectObj6)

    textSurfaceObj7 = fontdifficulty.render("5.  "+str(top_score_liste[-5]), True, GREEN)
    textRectObj7 = textSurfaceObj7.get_rect()
    textRectObj7.center = ((30 + (80 / 2)), (270 + (40 / 2)))
    DISPLAYSURF.blit(textSurfaceObj7, textRectObj7)

    textSurfaceObj8 = fontdifficulty.render("6.  "+str(top_score_liste[-6]), True, GREEN)
    textRectObj8 = textSurfaceObj8.get_rect()
    textRectObj8.center = ((30 + (80 / 2)), (310 + (40 / 2)))
    DISPLAYSURF.blit(textSurfaceObj8, textRectObj8)

    textSurfaceObj9 = fontdifficulty.render("7.  "+str(top_score_liste[-7]), True, GREEN)
    textRectObj9 = textSurfaceObj9.get_rect()
    textRectObj9.center = ((30 + (80 / 2)), (350 + (40 / 2)))
    DISPLAYSURF.blit(textSurfaceObj9, textRectObj9)

    textSurfaceObj10 = fontdifficulty.render("8.  "+str(top_score_liste[-8]), True, GREEN)
    textRectObj10 = textSurfaceObj10.get_rect()
    textRectObj10.center = ((30 + (80 / 2)), (390 + (40 / 2)))
    DISPLAYSURF.blit(textSurfaceObj10, textRectObj10)

    textSurfaceObj11 = fontdifficulty.render("9.  "+str(top_score_liste[-9]), True, GREEN)
    textRectObj11 = textSurfaceObj11.get_rect()
    textRectObj11.center = ((30 + (80 / 2)), (430 + (40 / 2)))
    DISPLAYSURF.blit(textSurfaceObj11, textRectObj11)

    textSurfaceObj12 = fontdifficulty.render("10.  "+str(top_score_liste[-10]), True, GREEN)
    textRectObj12 = textSurfaceObj12.get_rect()
    textRectObj12.center = ((30 + (80 / 2)), (470 + (40 / 2)))
    DISPLAYSURF.blit(textSurfaceObj12, textRectObj12)

    back_button = pygame.draw.rect(DISPLAYSURF, BLACK, (400, 470, 82, 40))

    textSurfaceObj13 = fontObj.render("Back", True, GREEN)
    textRectObj13 = textSurfaceObj13.get_rect()
    textRectObj13.center = ((400 + (80 / 2)), (470 + (40 / 2)))
    DISPLAYSURF.blit(textSurfaceObj13, textRectObj13)

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                position = event.pos
                if back_button.collidepoint(position[0], position[1]) == True:
                    selection_menu()

def selection_menu():
    WINDOWWIDTH = 540
    WINDOWHEIGHT = WINDOWWIDTH
    pygame.init()
    pygame.display.set_caption("Snek")
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    fontObj = pygame.font.Font('freesansbold.ttf', 35)
    fontObj2 = pygame.font.Font('freesansbold.ttf', 60)
    DISPLAYSURF.fill(BLACK)

    play_button = pygame.draw.rect(DISPLAYSURF, BLACK, (30, 210, 80, 40))
    score_button = pygame.draw.rect(DISPLAYSURF, BLACK, (30, 310, 200, 35))
    quit_button = pygame.draw.rect(DISPLAYSURF, BLACK, (30, 410, 80, 35))

    textSurfaceObj2 = fontObj.render("Play", True, GREEN)
    textRectObj2 = textSurfaceObj2.get_rect()
    textRectObj2.center = ((27 + (80 / 2)), (210 + (40 / 2)))
    DISPLAYSURF.blit(textSurfaceObj2, textRectObj2)

    textSurfaceObj3 = fontObj.render("Scoreboard", True, GREEN)
    textRectObj3 = textSurfaceObj3.get_rect()
    textRectObj3.center = ((30 + (200 / 2)), (310 + (40 / 2)))
    DISPLAYSURF.blit(textSurfaceObj3, textRectObj3)

    textSurfaceObj4 = fontObj.render("Quit", True, GREEN)
    textRectObj4 = textSurfaceObj4.get_rect()
    textRectObj4.center = ((28 + (80 / 2)), (410 + (40 / 2)))
    DISPLAYSURF.blit(textSurfaceObj4, textRectObj4)

    textSurfaceObj5 = fontObj2.render("~~Little Snek~~", True, GREEN)
    textRectObj5 = textSurfaceObj5.get_rect()
    textRectObj5.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2 - 180)
    DISPLAYSURF.blit(textSurfaceObj5, textRectObj5)


    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                position = event.pos
                if play_button.collidepoint(position[0], position[1]) == True:
                    start_screen()
                elif score_button.collidepoint(position[0], position[1]) == True:
                    score_menu()
                elif quit_button.collidepoint(position[0], position[1]) == True:
                    pygame.quit()
                    sys.exit()

def new_start_screen():
    WINDOWWIDTH = 540
    WINDOWHEIGHT = WINDOWWIDTH
    pygame.init()
    pygame.display.set_caption("Snek")
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    fontObj = pygame.font.Font('freesansbold.ttf', 35)
    fontObj2 = pygame.font.Font('freesansbold.ttf', 60)
    textSurfaceObj = fontObj.render('Press "Space" to start game!', True, GREEN)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2 + 80)
    DISPLAYSURF.fill(BLACK)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)

    textSurfaceObj2 = fontObj2.render("~~Little Snek~~", True, GREEN)
    textRectObj2 = textSurfaceObj2.get_rect()
    textRectObj2.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2 - 180)
    DISPLAYSURF.blit(textSurfaceObj2, textRectObj2)

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    selection_menu()


def start_screen():
    WINDOWWIDTH = 540
    WINDOWHEIGHT = 400
    pygame.init()
    pygame.display.set_caption('Snek')
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    fontObj = pygame.font.Font('freesansbold.ttf', 35)
    textSurfaceObj = fontObj.render("How Bad do You want it BOI?!", True, WHITE, BLUE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 20 + 50)
    DISPLAYSURF.blit(bg, [0, 0])
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    fontdifficulty = pygame.font.Font('freesansbold.ttf', 20)

    easy_rahmen = pygame.draw.rect(DISPLAYSURF, GREY, (27, 297, 106, 66))
    medium_rahmen = pygame.draw.rect(DISPLAYSURF, GREY, (207, 297, 106, 66))
    hard_rahmen = pygame.draw.rect(DISPLAYSURF, GREY, (387, 297, 106, 66))

    easy = pygame.draw.rect(DISPLAYSURF, RED, (30, 300, 100, 60))
    medium = pygame.draw.rect(DISPLAYSURF, RED, (210, 300, 100, 60))
    hard = pygame.draw.rect(DISPLAYSURF, RED, (390, 300, 100, 60))

    textSurfaceObj2 = fontdifficulty.render("EASY", True, WHITE)
    textRectObj2 = textSurfaceObj2.get_rect()
    textRectObj2.center = ((30+(100/2)), (300+(60/2)))
    DISPLAYSURF.blit(textSurfaceObj2, textRectObj2)

    textSurfaceObj3 = fontdifficulty.render("MEDIUM", True, WHITE)
    textRectObj3 = textSurfaceObj3.get_rect()
    textRectObj3.center = ((210 + (100 / 2)), (300 + (60 / 2)))
    DISPLAYSURF.blit(textSurfaceObj3, textRectObj3)

    textSurfaceObj4 = fontdifficulty.render("HARD", True, WHITE)
    textRectObj4 = textSurfaceObj4.get_rect()
    textRectObj4.center = ((390 + (100 / 2)), (300 + (60 / 2)))
    DISPLAYSURF.blit(textSurfaceObj4, textRectObj4)

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                position = event.pos
                if easy_rahmen.collidepoint(position[0], position[1]) == True:
                    makeGUI(10)
                elif medium_rahmen.collidepoint(position[0], position[1]) == True:
                    makeGUI(15)
                elif hard_rahmen.collidepoint(position[0], position[1]) == True:
                    makeGUI(20)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    makeGUI(10)
                elif event.key == pygame.K_2:
                    makeGUI(15)
                elif event.key == pygame.K_3:
                    makeGUI(20)
def board_to_pixel_koord(i, j, width):
    return j * width, i * width

def make_rectangle_red(liste, display, size):
    x, y = board_to_pixel_koord(liste['x'], liste['y'], size)
    the_rect = pygame.Rect(x, y, size, size)
    pygame.draw.rect(display, RED, the_rect)

def make_rectangle_green(dict, display, size):
    x, y = board_to_pixel_koord(dict['x'], dict['y'], size)
    the_rect = pygame.Rect(x, y, size, size)
    pygame.draw.rect(display, GREEN, the_rect)

if __name__ == '__main__':
    new_start_screen()