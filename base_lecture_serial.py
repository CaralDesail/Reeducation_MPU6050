import serial
import time
import re
from statistics import mean

ser = serial.Serial('COM3')  # open serial port
ser.baudrate = 57600 # don't works with any other values is 9600
num_val_mean = 5


print(ser.name)         # check which port was really used

trash=ser.readline() # a reading of serial that avoid initialisation bugs (because of only a part of the data arrived)

list_to_meanX=[] #create a list in wich we'll put "num_val_mean" values before meaning it.
list_to_meanY=[] #the same with y
list_to_meanZ=[]

print(ser.readline())
print(ser.readline())
print(ser.readline())

while True:
#    tic=time.time()  # first time

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
        x_m=mean(list_to_meanX) # x_m will be the meaned value
        y_m=mean(list_to_meanY) # y_m will be the meaned value
        z_m=mean(list_to_meanZ) # z_m will be the meaned value
        print("x = ",x_m,"y = ",y_m,"z = ",z_m )

        list_to_meanX = [] #putting the xlist to 0
        list_to_meanY = [] #putting the ylist to 0
        list_to_meanZ = [] #putting the ylist to 0


#    tac=time.time() # second time
#    print(tac-tic," seconde") # printing the duration of an interpretation

ser.close()             # close port