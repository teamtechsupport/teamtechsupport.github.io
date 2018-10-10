# this script is for decypting various ciphers when provided with a key
import string


def decrypt(encoded, key, cipher):
    decrypted = ""
    if cipher == "substitution":
        # create a dictionary with each letter of the key corresponding to a letter in the text
        sol = dict(zip(string.ascii_uppercase, key))
        for l in encoded:
            decrypted += sol[l]
        return decrypted
    elif cipher == "transposition":
        columns = []
        colno = len(key)
        rows = [encoded[i:i+colno] for i in range(0, len(encoded), colno)]
        for x in range(len(rows[0])):
            columns.append([])
        for x in range(len(rows)):
            for y in range(len(rows[x])):
                columns[y].append(list(rows[x][y]).pop())

        for x in range(len(columns)):
            try:
                for y in range(len(columns[0])):
                    decrypted.append(columns[x][])
