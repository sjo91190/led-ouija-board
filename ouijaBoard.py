import time
import string

LET = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s", "t", "u", "v", "w", "x", "y", "z"]
ULET = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S", "T", "U", "V", "W", "X", "Y", "Z"]

def phrase():

        word = raw_input("Enter phrase: ")
        wordForm = "\n".join(word)
        for let, ulet in zip(LET,ULET):
                wordForm = wordForm.replace(ulet, let)
                with open("/home/pi/phrase.txt", "w") as phraseFile:
                        phraseFile.write(wordForm)

while True:
        try:
                phrase()
		quit()
        except KeyboardInterrupt:
                quit()
