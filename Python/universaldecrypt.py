import urllib.request
from bs4 import BeautifulSoup
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
    ciphertext = ciphertext[::-1]
    print(ciphertext)


