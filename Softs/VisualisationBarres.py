import serial
import re
from statistics import mean
import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 600))
done = False
rectScreen = screen.get_rect()

ser = serial.Serial('COM3')  # open serial port
ser.baudrate = 57600 #  don't works with any other values ie 9600
num_val_mean = 5
clock = pygame.time.Clock()
police = pygame.font.Font(None, 72)

color1 = (0, 128, 255) #blue
color2 = (128, 0, 255) #purple bright
color3 = (128, 128, 255) #lavender
color4 = (128, 0, 128) #purple less bright

print(ser.readline())
print(ser.readline())
print(ser.readline())

# initial positions of current x y and z
x_m=int(0)
y_m=int(0)
z_m=int(0)


list_to_meanX=[] #create a list in wich we'll put "num_val_mean" values before meaning it.
list_to_meanY=[] #the same with y
list_to_meanZ=[]

with open("../calibration.txt", "r") as mycalfile:  # put it into a calibration_vars
    text_of_limits = mycalfile.read()
    list_of_limits = text_of_limits.split()
    print(list_of_limits)


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # reading part
    info_serial_tr=ser.readline() # basis reading from serial port
    liste_acc_val= re.findall("(.[0-9]+)",str(info_serial_tr)) # we simplify the sentence, and extract data in a list

    if len(liste_acc_val)==3 :
        # meaning part
        list_to_meanX.append(int(liste_acc_val[1]))
        list_to_meanY.append(int(liste_acc_val[0]))
        list_to_meanZ.append(int(liste_acc_val[2]))
    else :
        continue


    if len(list_to_meanX)==num_val_mean: #when a list reaches num-val_mean : meaning starts and produces x_m and y_m
        x_m=int(mean(list_to_meanX)) # x_m will be the meaned value
        y_m=int(mean(list_to_meanY)) # y_m will be the meaned value
        z_m=int(mean(list_to_meanZ)) # z_m will be the meaned value
        print("x = ",x_m,"y = ",y_m,"z = ",z_m )

        list_to_meanX = [] #putting the xlist to 0
        list_to_meanY = [] #putting the ylist to 0
        list_to_meanZ = [] #putting the ylist to 0


 #   texte = police.render(text_of_limits, True, pygame.Color("#F00F00"))
 #   rectTexte = texte.get_rect()

    screen.fill((0, 200, 0)) # fullfillment of the screen with a color


    x_longueur_max=float(x_m/float(list_of_limits[0]))*1000
    x_longueur_min=float(x_m/float(list_of_limits[1]))*1000
    y_longueur_max=float(y_m/float(list_of_limits[2]))*1000
    y_longueur_min=float(y_m/float(list_of_limits[3]))*1000

# print of different histograms with x/xmax and xmin and y / ymax and min
    pygame.draw.rect(screen, color1, pygame.Rect(30, 50, x_longueur_max, 50))
    pygame.draw.rect(screen, color2, pygame.Rect(30, 150, x_longueur_min, 50))
    pygame.draw.rect(screen, color3, pygame.Rect(30, 250, y_longueur_max, 50))
    pygame.draw.rect(screen, color4, pygame.Rect(30, 350, y_longueur_min, 50))


 #   screen.blit(texte, rectTexte)

    pygame.display.flip()

    clock.tick(300)
#    tac=time.time() # second time
#    print(tac-tic," seconde") # printing the duration of an interpretation

ser.close()             # close port