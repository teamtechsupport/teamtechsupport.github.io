import urllib.request
from bs4 import BeautifulSoup
import vigenere
import substitution
import re
import column_transposition

challengeno = 0
aorb = "none"
try:
    challengeno = int(input("Enter challenge number (1-10)"))
except ValueError:
    print("Not an integer \nAssuming Challenge 9")
    challengeno = 9
aorb = input("Enter challenge number (1-10)").lower()
x=0
if aorb != "a":
    x += 1
elif aorb != "b":
    x += 1
if x == 2:
    print("Not A or B \nAssuming B ")
    aorb = "b"
class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"
opener = AppURLopener()
quote_page = ("https://www.cipherchallenge.org/challenges/challenge-" + str(challengeno))
page = opener.open(quote_page)
soup = BeautifulSoup(page, "html.parser")
if aorb == "a":
    name_box = soup.find("div", attrs={"class": "a"})
else:
    for item in soup.find_all('div',class_="challenge__content"):
     if len(item["class"]) != 1:
         continue;
     else:
         name_box = item.p
ciphertext = name_box.text.strip()

if input("Reverse text? (yes)").lower() in ["yes","true" ,"y"]:
    print("reversed input")
    ciphertext = ciphertext[::-1]
    
userinput = ciphertext.upper()

def crackermenu(userinput):
    choice = int(input("\n\n\nWhat would you like to run?\nSubstitution (1)\nVigenere (2) \nColumnar Transposition (3)\nJust output ciphertext (4)\n\n\n"))
    if choice == 1:
        substitution.substitutionsolver(userinput)
    elif choice == 2:
        try:
            keylen = int(input("Enter number of letters in key; if unknown enter '0' to cycle through 2-20: "))
        except:
            print("Not an integer, cycling through possibilities 2-20.")
            keylen = 1
        vigenere.runvigenere(userinput,keylen)
    elif choice == 3:
        try:
            colno = int(
            input("Enter number of columns; if unknown enter '0' to cycle through 2-20: "))
        except:
            print("Not an integer, cycling through possibilities 1-9.")
            colno = 1
        column_transposition.coltransolver(colno,userinput)
    elif choice == 4:
        regex = re.compile('[^A-Z]')
        print(regex.sub('', userinput))
    else:
        print("Choice is not recognised.")
        crackermenu(userinput)
        
crackermenu(userinput)

