users=["Arshad Ali", "Shaheen Arshad", "Owais Ali", "Uzair Ali", "Usaid Ullaha", "Humaid Ullaha"]
password=["arshadali","shaheenarshad","owaisali", "uzairali", "usaidullaha", "humaidullaha"]

def calculator():
    Flag=True
    while Flag:
        no1=input("Enter the first number: ")
        print("chose a operator")
        operator=input("/, *, +, - : ")
        no2=input("Enter the second number: ")
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
def take_pass():
    global pas
    pas=input("Enter your password: ").lower()
    if pas==password[pass_at]:
        return print("welcome you can use our service"),calculator()
    else:
        print("wrong password \n plaese try again")
        return take_pass()
athuntication=True
while athuntication:
    name=input("Enter your name: ").title()
    if name in users:
        pass_at=users.index(name)
        take_pass()
        athuntication=False
    else:
        print("invalid user") 

#print(a)
#print(b)


 