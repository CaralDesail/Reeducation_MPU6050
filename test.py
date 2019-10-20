import re


string1="testsanschiffres"
string2="b'   567 -16073   -554\r\n'"
string3="adz 231"


string = "TEST fs -654 -87945"
regexp = r"([0-9]+)*"


print (re.findall("(.[0-9]+)",string2))