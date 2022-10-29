import math as mt
import numpy as np

def calculator():
    Flag=True
    while Flag:
        no1=input("Enter the number of which you want to divide: ")
        print("chose a operator")
        operator=input("/, *, +, - : ")
        no2=input("Enter the number from which you want to divide: ")
        try:
            no1=int(no1)
            no2=int(no2)
            if operator=='/':
                Ans=no1/no2
            elif operator=="*":
                Ans=no1*no2
            elif operator=="+":
                Ans=no1+no2
            elif operator=="-":
                Ans=no1-no2
            print(Ans)
            print("do you perform another calculation")
            choice=input("Yes/No: ").title()
            # print(choice)
            if choice=='Yes':
                Flag=True
            elif choice=='No':
                Flag=False
        except Exception as e:
            print(f"Exception {(e)} occourd")  




if __name__=="__main__":
    calculator()