"""
Created on 10/19/22

@author: Laura Peng
"""

import os.path
file = os.path.join("data","lowerwords.txt")
f = open(file)
wordsClean = [w.strip() for w in f.read().split()]


#variables for the shifted and regular alphabet in lower and upper case
shift = 3

lower_alph = "abcdefghijklmnopqrstuvwxyz"

upper_alph = lower_alph.upper()

shifted_lower = lower_alph[shift:] + lower_alph[:shift]

shifted_upper = upper_alph[shift:] + upper_alph[:shift]

#takes a word and does a caesar cipher
def encrypt(word):
    value = ""

    for x in word:

        if x in lower_alph:
            charNum = lower_alph.find (x)
            value+= shifted_lower [charNum]
        elif x in upper_alph:
            charNum2 = upper_alph.find(x)
            value = value + shifted_upper[charNum2]
        else:
            value+=x

    return value

"""takes a number and that number is the shift for the caesar cipher 
so it changes the global variables based on the shift number
"""
def setShift(num):
    global shift, shifted_lower, shifted_upper
    shift = num
    upper_alph = lower_alph.upper()
    shifted_lower = lower_alph[shift:] + lower_alph[:shift]

    shifted_upper = upper_alph[shift:] + upper_alph[:shift]


#returns the shift that was originally used to encrypt the words

def findShift(st):
    values = []
    for sh in range (26):
        setShift (sh)

        value = encrypt(st)
        value = value.split()

        num = set(value).intersection (wordsClean)


        values.append(num)

    return  26-values.index(max (values, key = len))
    #return values.index (max (values))


#tests the functions on top by encrypting and decrypting the words and finding the shift by calling the functions
if __name__ == '__main__':
    setShift (10)
    ew = encrypt ("Zebra")
    setShift (16)
    w = encrypt (ew)
    print (ew,w)


    print (findShift ("Zkdw grhv wkh ira vdb?"))
    print (findShift ("Bxvncrvnb rc'b njbh cx lxdwc oaxv 1-10, kdc wxc jufjhb"))
