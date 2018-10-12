import annealing_decryption
import re
import string

key = string.ascii_uppercase
ciphertype = "substitution"

userinput = input("Enter encoded text:\n").upper()
print(userinput)
regex = re.compile('[^A-Z]')
print(regex.sub('', userinput), "HE")
print(annealing_decryption.anneal(regex.sub('', userinput), key, ciphertype))
