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
                exit
            elif play_with=='c':
                while True:
                    color=input("Play As: ").upper()
                    if color=="0":
                        exit
                    #print(f"your tokens are"+{color})
                    elif color=='RED':
                        color=RED
                        color1=Red
                        print("Computer play as Blue")
                        print("Your tokens are ",RED )
                        break
                    elif color=="BLUE":
                        color=BLUE
                        color1=Blue
                        print("Computer play as Red")
                        print("Your tokens are ",color)
                        break
                    elif color=='GREEN':
                        color=GREEN
                        color1=Green
                        print("Computer play as Yellow")
                        print("Your tokens are ",GREEN )
                        break
                    elif color=="YELLOW":
                        color=YELLOW
                        color1=Yellow
                        print("Computer play as Green")
                        print("Your tokens are ",YELLOW )
                        break
                    else:
                        print("Please chose 'Red' , 'Green' , 'Yellow' or 'Blue'")
                while True:
                    H_turn=input("Your Turn For Roll the Dice press Enter: ".title())
                    if H_turn=="0":
                        exit
                    elif H_turn=="":
                        roll=rd.randrange(1,7)
                        print(roll)
                        if roll==6:
                            #print(f"Token no are \n(1={color[0]},2={color[1]},3={color[2]},4={color[3]})")
                            while True:
                                Tk_no=int(input("Enter The Token no of which you want to take out: "))
                                if Tk_no==0:
                                    exit
                                elif Tk_no>0 and Tk_no<=4:
                                    PoP_Tk=color.pop(Tk_no-1)
                                    color1.insert(0,PoP_Tk)
                                    print(color1)
                                    break
                                else:
                                    print("Not Valid operation for rolling the dice".title())
                        
                        
    else:
        print("Not valid")
        play()
play()