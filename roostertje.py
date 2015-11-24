import sys, pygame

pygame.init()

black = (0,0,0)
red = (255,0,0)
white = (255,255,255)
gekkigheid = (255, 240, 240)
grey = (158,158,158)

display_x = 500
display_y = 500

gameDisplay = pygame.display.set_mode((display_x, display_y))
pygame.display.set_caption('Gimmah')

gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    gameDisplay.fill(gekkigheid)
    # pygame.draw.rect(gameDisplay, black, [400,300,10,10])
    screen = gameDisplay.fill(grey, rect=[857,100,350,600])

    # header line
    pygame.draw.line(gameDisplay, red, (0,100), (1200,100), 3)

    # rectangle op (0,0)
    pygame.draw.rect(gameDisplay, red, (0,100,display_x/7,120), 4)

    i = 0
    while i < display_x:
        # horizonal lines
        pygame.draw.line(gameDisplay, black, (0,220), (1200,220), 1)
        pygame.draw.line(gameDisplay, black, (0,340), (1200,340), 1)
        pygame.draw.line(gameDisplay, black, (0,460), (1200,460), 1)
        pygame.draw.line(gameDisplay, black, (0,580), (1200,580), 1)

        #
        pygame.draw.line(gameDisplay, black, (i,100), (i,900), 1)
        i += display_x/7
        if i > 1150:
            break

	pygame.display.set_caption('Basic Pygame program')
    pygame.display.update()

pygame.quit()
quit()
