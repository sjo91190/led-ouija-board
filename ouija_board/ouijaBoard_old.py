def phrase():
    word = input("Enter phrase: ")
    with open("/home/pi/led-ouija-board/WebGUI/webphrase.txt", "w") as phraseFile:
        phraseFile.write(word)


while True:
    try:
        phrase()
        quit()
    except KeyboardInterrupt:
        quit()
