import annealing_decryption
import re
import random


def transpos(text, colno):
    columns = []
    rows = [text[i:i+colno] for i in range(0, len(text), colno)]
    for l in range(len(rows[0])):
        columns.append([])
    for x in range(len(rows)):
        for y in range(len(rows[x])):
            columns[y].append(list(rows[x][y]).pop())
    print(rows)
    print(columns)


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
