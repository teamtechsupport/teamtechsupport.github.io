#Prav's Test WIP
!pip install nltk
import nltk
nltk.download("words")
import string
english = set(w.lower() for w in words.words())
def bruteForce(message):
  letters = list(message)
  letterpos = []
  for letter in letters:
    if letter == " " or letter == "," or letter == "." or letter == ";" or letter == ":" or letter == "'":
      pos = letter
    else:
      pos = ord(letter)-97
    letterpos.append(pos)
  a = 1
  b = 1
  avars = [1,9,21,15,3,19,7,23,11,5,17,25]
  abvars = []
  for letter in letterpos:
    if letter == " " or letter == "," or letter == "." or letter == ";" or letter == ":" or letter == "'": 
      currentletter = []
      for a in avars:
        b = 1
        while b<=26:
          currentletter.append(letter)
          b=b+1
    else:
      currentletter = []
      for a in avars:
        b=1
        currenta = []
        while b<=26:
          ax = letter - b
          abx = ax * a
          if abx % 26 !=0:
            abx = abx % 26
          else:
            abx = 0
          aby = chr(abx+97)
          currentletter.append(aby)
          currenta.append(aby)
          b = b + 1
    abvars.append(currentletter)
  times = 0
  while times < 311: 
    listwords = ([i[times] for i in abvars])
    wordjoined = ("".join(listwords))
    correct = 0
    lengthto = len(wordjoined.split())
    for word in wordjoined.split():
        if correct <= (0.4*lengthto):
            #not too sure is 40% is too harsh or too relaxed.
            if len(word) > 2:
                if word in english:
                    correct += 1
        else:
            print(wordjoined)
            break
    times += 1
  
def affineShifts():
  message = input("Input message ").lower()
  bruteForce(message)
  
affineShifts()
