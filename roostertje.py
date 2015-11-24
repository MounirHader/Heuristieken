import sys, pygame

pygame.init()

black = (0,0,0)
red = (255,0,0)
white = (255,255,255)
gekkigheid = (255, 240, 240)
grey = (158,158,158)

display_x = 1200
display_y = 700

gameDisplay = pygame.display.set_mode((display_x, display_y))
pygame.display.set_caption('Gimmah')

gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        # if ...
        #     do this
        # if ...
        #     do that

    gameDisplay.fill(gekkigheid)
    # pygame.draw.rect(gameDisplay, black, [400,300,10,10])
    screen = gameDisplay.fill(grey, rect=[857,100,350,600])

    # header line
    pygame.draw.line(gameDisplay, red, (0,100), (1200,100), 3)

    i = 0
    while i < display_x:

        # horizonal lines
        pygame.draw.line(gameDisplay, black, (0,220), (1200,220), 1)
        pygame.draw.line(gameDisplay, black, (0,250), (1200,250), 1)
        pygame.draw.line(gameDisplay, black, (0,280), (1200,280), 1)
        pygame.draw.line(gameDisplay, black, (0,310), (1200,310), 1)
        
        pygame.draw.line(gameDisplay, black, (0,340), (1200,340), 1)
        pygame.draw.line(gameDisplay, black, (0,460), (1200,460), 1)
        pygame.draw.line(gameDisplay, black, (0,580), (1200,580), 1)

        #
        pygame.draw.line(gameDisplay, black, (i,100), (i,900), 1)
        i += display_x/7
        if i > 1150:
            break
        #
        # pygame.draw.line(gameDisplay, black, (0,0), (0,900), 1)
        # pygame.draw.line(gameDisplay, black, (240,0), (240,900), 1)
        # pygame.draw.line(gameDisplay, black, (480,0), (480,900), 1)
        # pygame.draw.line(gameDisplay, black, (720,0), (720,900), 1)
        # pygame.draw.line(gameDisplay, black, (960,0), (960,900),    1)

	pygame.display.set_caption('Basic Pygame program')

	# font = pygame.font.Font(None, 36)
	# text = font.render("Hello There", 1, (10, 10, 10))
	# textpos = text.get_rect()
	# textpos.centerx = pygame.Surface(screen.get_rect().centerx
	# pygame.Surface(screen.get_size().blit(text, textpos)

    pygame.display.update()

pygame.quit()
quit()
