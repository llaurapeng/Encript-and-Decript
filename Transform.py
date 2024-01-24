'''
Created on Feb 6, 2022

@author: Laura peng
'''
import string
import tkinter.filedialog
import Vowelizer
import sys
import PigLatin
import CaesarCipher
import os.path
def clean(word):
    """
    Remove all leading/trailing characters
    that are not ascii_letters
    """

    # remove leading non letter characters
    for dex in range(len(word)):
        ch = word[dex]
        if ch in string.ascii_letters:
            word = word[dex:]
            break
        
    #remove trailing non letter characters
    for dex in range(len(word)-1,0,-1):
        ch = word[dex]
        if ch in string.ascii_letters:
            word = word[:dex+1]
            break
    
    return word

def readFileAsLines(fname, doclean=False):
    """
    return list of lists where each inner
    list is the words on a line of the file
    
    if doclean == True, remove leading/trailing non-alpha
    characters from each word
    """
    f = open(fname, encoding="utf-8")
    ret = []
    for line in f:
        line = line.split()
        if doclean:
            line = [clean(w) for w in line]
        ret.append(line)
        
    f.close()
    return ret
   
def writeFileAsLines(fname,lines):
    """
    fname is a String, a path to a file that
    will be created.

    lines is a list of line-lists, where each line-list
    is a list of words (representing lines in a file)
    
    Create a file with fname and write
    each element/sub-list of lines to the file as a line
    Each line written will have a single space between
    the words on the line
    """
    f = open(fname, "w", encoding="utf-8")
    count = 0
    for line in lines:
        f.write(' '.join(line))
        f.write("\n")
        count += 1
        if count % 100 == 0:
            print(".... writing", count, "lines")
    f.close()
    print("Successfully wrote to {}".format(fname))
    print("You may need to refresh the 'data' folder in Pycharm to see the "
          "transformed file :)")

def doTransform(suffix, transform):
    """
    suffix is a string representing a suffix for
    a file name, e.g., "-pig" for piglatin or
    "-nvw" for novowels. A file with this suffix
    will be created.
    
    transform is a function that has a single parameter:
    a string, and returns a transformed form of
    that string. 
    
    This method prompts the user for a file, reads
    all the lines, transforms each word on each line
    and writes the transformed file to a new
    file with the specified suffix
    """
    # let user choose file, deal with nothing chosen
    global root 
    root.update()
    fname = tkinter.filedialog.askopenfilename(initialdir="./data")

    if len(fname) == 0:
        return
    
    # create new file name
    newname = fname + suffix
    if "." in fname:
        dex = fname.rfind(".")
        newname = fname[:dex] + suffix + fname[dex:]
    
    lines = readFileAsLines(fname)
    print("Successfully read {} lines from {}".format(len(lines), newname))
    
    error = False
    newlines = []
    for line in lines:
        transformedLine = [transform(w) for w in line]

        # Check to make sure transform returned valid values, if not stop transforming
        if None in transformedLine:
            print("\n***** ERROR *****")
            print("Make sure your {}() function always returns a value".format(transform.__name__))
            error = True
            break

        newlines.append(transformedLine)
        if len(newlines) % 100 == 0:
            print("...transforming {} lines".format(len(newlines)))

    if not error:
        print("Done transforming -- starting new file write...")
        writeFileAsLines(newname, newlines)


if __name__ == '__main__':
    global root

    # check version to ensure that TKinter will work
    # error message to explicitly direct students to change interpreter
    error_message = "Your interpreter is improperly configured, so you're " \
                    "running Python 2 instead of Python 3. Change your " \
                    "settings in Pycharm to use a Python 3 interpreter."
    if sys.version_info[0] < 3:
        raise Exception(error_message)
    
    # see StackOverflow and other posts for this
    # remove 'window' from being displayed
    
    root = tkinter.Tk()
    root.withdraw()
    
    # specific transform code called here
    # any set up needed followed by a call
    # to the doTransform function
    
    #doTransform("-nvw", Vowelizer.encrypt)
    #doTransform("-rvw", Vowelizer.decrypt)

    #encripts a file by using piglatin and creates a another file of the encrypted message

    #doTransform ("-pig", PigLatin.encrypt)

    # decrypts a file with piglatin words and creates a another file of the decrypted message
    doTransform("-upg", PigLatin.decrypt)


    #using caesar cipher to shift words by 18
    CaesarCipher.setShift(18)

    doTransform("-csr", CaesarCipher.encrypt)

    #verify that a shift 18 was used to encryt macbeth
    file = os.path.join("data", "twain-csr.txt")
    f = open(file)
    st = f.read()
    shift = CaesarCipher.findShift(st)
    print(shift)



    #decrypts the file decryptme-csr.text
    file = os.path.join("data","decryptme-csr.txt")
    f = open(file)
    st = f.read()
    shift = CaesarCipher.findShift(st)
    print(shift)

    CaesarCipher.setShift(26-shift)
    doTransform("-uncsr", CaesarCipher.encrypt)
    







