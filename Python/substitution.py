import annealing_dectryption
import re


userinput = input("Enter encoded text:\n").upper()
print(userinput)
regex = re.compile('[^A-Z]')
print(regex.sub('', userinput))
annealing_dectryption.anneal(regex.sub('', userinput))
