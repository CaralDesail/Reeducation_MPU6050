
# a calibration visualisation

import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 600))
done = False
rectScreen = screen.get_rect()

clock = pygame.time.Clock()

police = pygame.font.Font(None, 72)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    with open("calibration.txt", "r") as mycalfile:  # put it into a calibration_vars
        text_of_limits=mycalfile.read()
        list_of_limits=text_of_limits.split()

    print(list_of_limits)

    texte = police.render(text_of_limits, True, pygame.Color("#F00F00"))
    rectTexte = texte.get_rect()

    screen.fill((0, 0, 0))
    color1 = (0, 128, 255)
    color2 = (128,0 , 255)
    color3 = (128,128 , 255)
    color4 = (128,0 , 128)

    xmax_longueur=float(list_of_limits[0])/17000*1000
    xmin_longueur=float(abs(float(list_of_limits[1])))/17000*1000
    ymax_longueur=float(abs(float(list_of_limits[2])))/17000*1000
    ymin_longueur=float(abs(float(list_of_limits[3])))/17000*1000


    pygame.draw.rect(screen, color1, pygame.Rect(30, 50, xmax_longueur, 60))
    pygame.draw.rect(screen, color2, pygame.Rect(30, 140, xmin_longueur, 60))
    pygame.draw.rect(screen, color3, pygame.Rect(30, 230, ymax_longueur, 60))
    pygame.draw.rect(screen, color4, pygame.Rect(30, 350, ymin_longueur, 60))

    screen.blit(texte, rectTexte)

    pygame.display.flip()
    clock.tick(30)