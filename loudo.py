import random as rd
RED=["Red 1","Red 2","Red 3","Red 4"]
GREEN=["Green 1","Green 2","Green 3","Green 4"]
YELLOW=["Yellow 1","Yellow 2","Yellow 3","Yellow 4"]
BLUE=["Blue 1","Blue 2","Blue 3","Blue 4"]
Red=[]
Green=[]
Yellow=[]
Blue=[]
def play():
    choice=input("Are you ready for game enter '1' for yes and '0' for exit: ")
    if choice=='0':
        return print("Good Bye")
    elif choice=='1':
        print("Wellcome to fun land".upper().center(100,"*"))
        print("Follow the instructions to play and press '0' to exit at any point".title())
        while True:
            play_with=input("Enter 'H' to play against human \nEnter 'C' to play against computer: ")
            if play_with=='0':
                return print("Good Bye")
                exit()
            elif play_with=='C':
                print(1)