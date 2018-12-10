import annealing_decryption
import re
import random
import math
import string
from threading import Thread
# http://practicalcryptography.com/cryptanalysis/stochastic-searching/cryptanalysis-vigenere-cipher-part-2/


def vigenere(text, keylen):
    key = "A"*keylen

    print(annealing_decryption.anneal(
        text, key, "vigenere", "rand", ""))


def runvigenere(userinput,keylen):
    regex = re.compile('[^A-Z]')
    if keylen > 1:
        vigenere(regex.sub('', userinput), keylen)
    else:
        for x in range(2, 21):
            vigenere(regex.sub('', userinput), x)
