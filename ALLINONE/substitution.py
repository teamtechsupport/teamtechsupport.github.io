import annealing_decryption
import re
import string

key = string.ascii_uppercase
ciphertype = "substitution"

def substitutionsolver(userinput):
    regex = re.compile('[^A-Z]')
    print(annealing_decryption.anneal(
        regex.sub('', userinput), key, ciphertype, "swap", ""))
