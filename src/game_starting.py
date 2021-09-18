import pygame
import os

ONECOUNT = 100
count = ONECOUNT
ONEPLAYER = 1
step = 1
players_list = []
current_player = "1"
players_list.append("1")
players_list.append("2")


def start_game():
    pygame.init()
    pygame.font.init()
    global gameScreen
    global myfont
    global button_1
    global button_2
    global button_3
    global button_4
    global button_5
    global button_6
    global button_7
    global button_8
    global button_9
    global button_10
    global button_11
    global button_12
    x = 100
    y = 100
    os.environ['Sp_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)
    pygame.display.set_caption("100 matches")
    gameScreen = pygame.display.set_mode((500, 500))
    gameScreen.fill((255, 255, 255))
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface3 = myfont.render('Player', False, (0, 0, 0))
    gameScreen.blit(textsurface3, (100, 50))
    button_1 = pygame.Rect(10, 200, 50, 50)
    button_2 = pygame.Rect(70, 200, 50, 50)
    pygame.draw.rect(gameScreen, (0, 200, 64), button_1)
    textsurface4 = myfont.render('1', False, (0, 0, 0))
    gameScreen.blit(textsurface4, (10, 200))
    pygame.draw.rect(gameScreen, (0, 200, 64), button_2)
    textsurface5 = myfont.render('2', False, (0, 0, 0))
    gameScreen.blit(textsurface5, (70, 200))
    button_3 = pygame.Rect(130, 200, 50, 50)
    button_4 = pygame.Rect(190, 200, 50, 50)
    pygame.draw.rect(gameScreen, (0, 200, 64), button_3)
    textsurface6 = myfont.render('3', False, (0, 0, 0))
    gameScreen.blit(textsurface6, (130, 200))
    pygame.draw.rect(gameScreen, (0, 200, 64), button_4)
    textsurface7 = myfont.render('4', False, (0, 0, 0))
    gameScreen.blit(textsurface7, (190, 200))
    button_5 = pygame.Rect(250, 200, 50, 50)
    button_6 = pygame.Rect(310, 200, 50, 50)
    pygame.draw.rect(gameScreen, (0, 200, 64), button_5)
    textsurface8 = myfont.render('5', False, (0, 0, 0))
    gameScreen.blit(textsurface8, (250, 200))
    pygame.draw.rect(gameScreen, (0, 200, 64), button_6)
    textsurface9 = myfont.render('6', False, (0, 0, 0))
    gameScreen.blit(textsurface9, (310, 200))
    button_7 = pygame.Rect(370, 200, 50, 50)
    button_8 = pygame.Rect(430, 200, 50, 50)
    pygame.draw.rect(gameScreen, (0, 200, 64), button_7)
    textsurface10 = myfont.render('7', False, (0, 0, 0))
    gameScreen.blit(textsurface10, (370, 200))
    pygame.draw.rect(gameScreen, (0, 200, 64), button_8)
    textsurface11 = myfont.render('8', False, (0, 0, 0))
    gameScreen.blit(textsurface11, (430, 200))
    button_9 = pygame.Rect(10, 260, 50, 50)
    button_10 = pygame.Rect(70, 260, 50, 50)
    pygame.draw.rect(gameScreen, (0, 200, 64), button_9)
    textsurface12 = myfont.render('9', False, (0, 0, 0))
    gameScreen.blit(textsurface12, (10, 260))
    pygame.draw.rect(gameScreen, (0, 200, 64), button_10)
    textsurface13 = myfont.render('10', False, (0, 0, 0))
    gameScreen.blit(textsurface13, (70, 260))
    pygame.display.flip()
    button_react()
    runGame = True
    while runGame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runGame = False
                pygame.quit()

if __name__ == '__game_starting__':
    start_game()