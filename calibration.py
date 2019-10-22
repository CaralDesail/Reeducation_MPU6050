import serial
import time
import re
from statistics import mean

ser = serial.Serial('COM3')  # open serial port
ser.baudrate = 57600 #  don't works with any other values ie 9600
num_val_mean = 5


print(ser.readline())
print(ser.readline())
print(ser.readline())

list_to_meanX=[] #create a list in wich we'll put "num_val_mean" values before meaning it.
list_to_meanY=[] #the same with y

print(" Programme de calibration ")
print(" Bougez dans les deux axes au maximum ")
print(" Etes vous pret ? ")
trash=input()
x_min=17000
x_max=0
y_min=17000
y_max=0


trash=ser.readline() # a reading of serial that avoid initialisation bugs (because of only a part of the data arrived)
trash=ser.readline() # a reading of serial that avoid initialisation bugs (because of only a part of the data arrived)
trash=ser.readline() # a reading of serial that avoid initialisation bugs (because of only a part of the data arrived)
trash=ser.readline() # a reading of serial that avoid initialisation bugs (because of only a part of the data arrived)
trash=ser.readline() # a reading of serial that avoid initialisation bugs (because of only a part of the data arrived)
trash=ser.readline() # a reading of serial that avoid initialisation bugs (because of only a part of the data arrived)



while True:
    # reading part
    info_serial_tr=ser.readline() # basis reading from serial port
    liste_acc_val= re.findall("(.[0-9]+)",str(info_serial_tr)) # we simplify the sentence, and extract data in a list

    if len(liste_acc_val)==3 :
        # meaning part
        list_to_meanX.append(int(liste_acc_val[1]))
        list_to_meanY.append(int(liste_acc_val[0]))
    else :
        continue

    if len(list_to_meanX)==num_val_mean: #when a list reaches num-val_mean : meaning starts and produces x_m and y_m
        x_m=mean(list_to_meanX) # x_m will be the meaned value
        y_m=mean(list_to_meanY) # y_m will be the meaned value
        print("x = ",x_m,"y = ",y_m )

        list_to_meanX = [] #putting the xlist to 0
        list_to_meanY = [] #putting the ylist to 0

        #put the limits on the max and min x and y positions
        if x_m>x_max :
            x_max=x_m
            print("x max devient : ",x_max)
        if x_m<x_min :
            x_min=x_m
            print("x min devient : ",x_min)
        if y_m>y_max :
            y_max=y_m
            print("y max devient : ",y_max)
        if y_m<y_min :
            y_min=y_m
            print("y min devient : ",y_min)

        calibration_vars=str(x_max)+str(" ")+str(x_min)+str(" ")+str(y_max)+str(" ")+str(y_min) #create a string with
                                                                    # xmax xmin ymax ymin

        with open("calibration.txt", "w") as mycalfile: #put it into a calibration_vars
            mycalfile.write(calibration_vars)




ser.close()             # close port