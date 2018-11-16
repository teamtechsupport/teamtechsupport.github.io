import annealing_decryption
import decrypt
import re
import random
import math
import itertools


def transpos(text, colno):
    initkey = list(str(math.floor(1234567890 / (10**(10-colno)))))

    perms = list(itertools.permutations(initkey))

    key=""
    cost = 0
    ngram = annealing_decryption.ngram_obj("https://gist.githubusercontent.com/DomDale/9a582deed33b20bb47e0363301d2c6c4/raw/62e7416f6be95893649398f0470f1dcd2668e608/english_trigrams.txt")
    for x in range(len(perms)):
        newcost = ngram.cost(decrypt.decrypt(text, "".join((perms[x])), "transposition"))
        print(newcost)
        if newcost < cost:
            cost = newcost
            key = "".join((perms[x]))
    
    print(key)

userinput = input("Enter encoded text:\n").upper()
regex = re.compile('[^A-Z]')

try:
    colno = int(
        input("Enter number of columns; if unknown enter '0' to cycle through 2-20: "))
except:
    print("Not an integer, cycling through possibilities 1-20.")
    colno = 1

if colno > 1:
    transpos(regex.sub('', userinput), colno)

else:
    for x in range(2, 21):
        transpos(regex.sub('', userinput), x)
