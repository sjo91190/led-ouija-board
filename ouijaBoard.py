def phrase():
    word = input("Enter phrase: ").lower()
    wordform = "\n".join(word)
    with open("/home/pi/led-ouija-board/phrase.txt", "w") as phraseFile:
        phraseFile.write(wordform)


while True:
    try:
        phrase()
        quit()
    except KeyboardInterrupt:
        quit()
