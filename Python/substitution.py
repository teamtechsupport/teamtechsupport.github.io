import annealing_decryption
import re


userinput = input("Enter encoded text:\n").upper()
print(userinput)
regex = re.compile('[^A-Z]')
print(regex.sub('', userinput))
print(annealing_decryption.anneal(regex.sub('', userinput)))
