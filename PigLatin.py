"""
Created on 10/19/22

@author: Laura Peng
"""
from pathlib import Path


#takes a word and encrypts the word using pig latin rules
def encrypt(word):
    num =0
    #sees if the word starts with vowel
    for x in "aeiouAEIOU":
        #x is a character

        #if word starts with a vowel then "way" is added to the end of the word
        if word[0]==x:
            num = 0
            return word+"-way"

        if word[0]!=x:
            num+=1


    #sees if the word contains no vowels, if it doesn't then way is added to the end

    no =0
    for x in word:
        val = 0
        for y in "aeiouAEIOUyY":
            if x!=y:
                val=1
            else:
                no =0
                break
        if (val==1):
            no+=1

    if no==len(word):
        print (1)
        return word+"-way"


    #goes through if statement if word begins with no vowel
    if num ==10 and no !=len(word):
        #find the first vowel
        counter = 0
        for y in word:

            if word[0:2]=="qu":
                for x in "aeioAEIO":
                    if y ==x:
                        return word[counter:]+"-" + word[:counter] + "ay"

            elif word[0]=="y" or word[0]=="Y":

                for x in "aeiouAEIOU":
                    if y == x:
                        return word[counter:] + "-" + word[:counter] + "ay"
            else:

                for x in "aeiouAEIOUyY":
                    if y ==x:
                        return word[counter:]+"-"+word[:counter]+"ay"


            counter+=1

#decripts the encrypted pig latin word by looking at the end of the word
def decrypt(word):

    if word [-3:]=="way":
        return word [:word.rfind ("-")]
    #if word doesn't start with a vowel
    else:
        start = word.index ("-")
        end = word.rfind ("ay")
        return word [start+1:end]+word [0:start]



if __name__ == '__main__':
    #encript message
    message = ["anchor", "oasis", "umbrella","AWOL"]
    message1 = ["computer", "yesterday","STRENGTH","my","rhythm","\"always!\""]
    message2=["quiz", "queue","quay","quran"]
    message3 = ["zzz","it", "wit"]

    emessage = []
    #all the lists are combined and each word in the list encrypted to piglatin
    for x in message+message1+message2+message3:
        emessage.append (encrypt(x))

    print (emessage)



    #all the lists are combined and each word in the list is encrypted using piglatn but then they will be decrypted
    message = ['anchor-way', 'oasis-way', 'umbrella-way', 'AWOL-way']
    message1 = ['omputer-cay', 'esterday-yay', 'ENGTH-STRay', 'y-may', 'ythm-rhay', 'always!"-"ay']
    message2 = ['iz-quay', 'eue-quay', 'ay-quay', 'an-quray', 'zzz-way']

    dmessage= []
    for x in message+message1+message2:
        dmessage.append (decrypt(x))

    print (dmessage)