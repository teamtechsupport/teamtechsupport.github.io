import annealing_decryption
import re
import random


def transpos(text, colno):
    key = "12345"

    print(annealing_decryption.anneal(
        text, key, "transposition"))


userinput = input("Enter encoded text:\n").upper()
regex = re.compile('[^A-Z]')

try:
    colno = int(
        input("Enter number of columns; if unknown enter '0' to cycle through 2-10: "))
except:
    print("Not an integer, cycling through possibilities 1-10.")
    colno = 1

if colno > 1:
    transpos(regex.sub('', userinput), colno)

else:
    for x in range(2, 11):
        transpos(regex.sub('', userinput), x)
