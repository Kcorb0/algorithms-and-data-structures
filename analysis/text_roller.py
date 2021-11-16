import os
import time

def text_roller(text):

    run = True
    text_line = list(text)

    for i in range(20 - len(text)):
        text_line.append(" ")
    

    while run:
            
        start = text_line.pop(0)
        text_line.append(start)

        os.system('cls')
        print("--------------------")
        print("".join(text_line))
        print("--------------------")
        time.sleep(.1)


if __name__ == "__main__":
    text_roller('ATTACK ON TITAN')

