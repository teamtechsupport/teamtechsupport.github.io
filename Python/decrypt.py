# this script is for decypting various ciphers when provided with a key
import string
import math

alpha = string.ascii_uppercase
letvals = dict(zip(string.ascii_uppercase, list(range(1, 27))))


def decrypt(encoded, key, ciphertype):
    decrypted = ""
    if ciphertype == "substitution":
        # create a dictionary with each letter of the key corresponding to a letter in the text
        sol = dict(zip(string.ascii_uppercase, key))
        for l in encoded:
            decrypted += sol[l]

    elif ciphertype == "transposition":
        key = list(map(int, key))  # key is split into list
        colno = len(key)  # find the amount of columns
        # find the amount of rows discounting extras (chars per column)
        rowno = math.floor(len(encoded)/colno)
        extrachars = (len(encoded) % colno)  # find the amount of extra chars
        columns = []
        # creates a list of the rows with an extra char to offset during col gen
        offsets = key[:extrachars]
        for x in key:  # for every number in key (in order)
            # calculate the offset based on the amount of offsets below the number
            offset = sum(i <= x for i in offsets)
            # if there is any extra chars (this will be on the first numbers of key)
            if extrachars > 0:
                # add the column
                columns.append(
                    encoded[((x-1)*rowno)+offset-1:(x*rowno)+offset])
                extrachars -= 1  # remove the processed extrachar
            else:
                columns.append(
                    encoded[((x-1)*rowno)+offset:(x*rowno)+offset])

        for y in range(rowno+1):
            for x in range(colno):
                try:
                    # get the first letter from each column and append; then second and so on.
                    decrypted += columns[x][y]
                except:
                    pass  # only some columns will have an extrachar so instead of excepting continue
    # IF THE CIPHERTEXT LETTER IS P AND THE KEY LETTER IS M, DO AN M CAESAR SHIFT (+12) Then find then find P in the list (4th letter) to get D (4th in alpha)
    elif ciphertype == "vigenere":
        key = list(key)
        keyindex = 0
        offset = 0
        for x in encoded:
            offset = letvals[key[keyindex]]
            if offset+letvals[x] > 26:
                letval = letvals[x] + offset - 26
            else:
                letval = letvals[x] + offset
            print(letval, letvals[x], offset, x, key[keyindex])

            for let, val in letvals.items():
                if val == letval:
                    decrypted += let
            keyindex += 1

            if keyindex >= len(key):
                keyindex = 0

    return decrypted


print(decrypt("PEZO", "MEME", "vigenere"))
