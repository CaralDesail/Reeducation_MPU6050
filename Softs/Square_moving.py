import serial
import re
from statistics import mean
import pygame

pygame.init()
h_screen=1200
w_screen=600
screen = pygame.display.set_mode((h_screen, w_screen))
done = False
rectScreen = screen.get_rect()

ser = serial.Serial('COM3')  # open serial port
ser.baudrate = 57600 #  don't works with any other values ie 9600
num_val_mean = 5
clock = pygame.time.Clock()
police = pygame.font.Font(None, 72)

x = h_screen//2
y = w_screen//2


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

    screen.fill((0, 0, 0)) # fullfillment of the screen with a color

    if x_m > float(list_of_limits[0]) * 0.5 : x+=3
    if x_m < float(list_of_limits[1]) * 0.5 : x-=3
    if y_m > float(list_of_limits[2]) * 0.5 : y+=3
    if y_m < float(list_of_limits[3]) * 0.5 : y-=3


# print of different histograms with x/xmax and xmin and y / ymax and min


 #   screen.blit(texte, rectTexte)
    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(x, y, 60, 60))
    pygame.display.flip()

    clock.tick(300)
#    tac=time.time() # second time
#    print(tac-tic," seconde") # printing the duration of an interpretation

ser.close()             # close port