import requests
import string
import random
import math
import re

def transpos(text):
    for n in range(2,11):
        r = [text[i:i+n] for i in range(0, len(text), n)]
        print(r)
    


userinput = input("Enter encoded text:\n").upper()
print(userinput)
regex = re.compile('[^A-Z]')
print(regex.sub('', userinput))
transpos(regex.sub('', userinput))

  
