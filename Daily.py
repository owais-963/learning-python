
import os
import time as tm
from plyer import notification as nt
import schedule as sd
from datetime import datetime as dt

Time=["05:55"
,"6:00"
,"06:30"
,"08:30"
,"09:00"
,"10:00"
,'11:15'
,"12:30"
,"13:15"
,'14:00'
,"15:00"
,"15:45"
,"16:30"
,"18:30"
,"19:30"
,"20:30"
,'21:30'
,'22:00'
,"21:15"]
#Time=[T0,T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16,T17,T18]
Ruteen=["you have to leave the bad prepeaare your self for Nmaze Fajar"
,"You have to perform Nmaze-e-Fajar"
,"Go to ground and run it's good for health"
,"Take break fast"
,"Read book and take rest"
,"Learn and practice of Math"
,'Take Out your Physics book and learn some physics'
,"Learn English"
,'Perform Nmaz-e-Zohar'
,"Watch video and learn software development"
,"Learn digital marketing"
,"Watch video of python programing"
,"Perform Nmaz-e-Asar"
,"Do programing on python"
,"Perform Nmaz-e-Esha"
,"Do Programing Again"
,"Shut dwon your Pc"
,"Go for exercise with your friends"
,"Go to the Bed"]
def noti():
    Tm=tm.strftime("%H:%M")
    if Tm in Time:
        MSG_No=Time.index(Tm)
        MSG=Ruteen[MSG_No]
        return nt.notify(title="My Daily Schedule",message=f"HI! Owais\n{MSG}",app_icon=None,timeout=20,)
    else:
        return noti()

#Ruteen=[r0,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16,r17,r18]
##########################################################################
"*************************************************************************"
print("I am your noifier to ntoify you about your daily schedule".upper())
name="owais ali"
password="myschedule.123"
Start=True
while Start:
    starter=input("to See the schedule press '1' and Enter your name and password\nPress 3 to continue\nAnd press 0 to dismiss: ".title())
    if starter=='0':
        Start=False
        exit
    elif starter=='1':
        Start=False
        Runing=True
        while Runing:
            a=input("Name: ")
            b=input("Password: ")
            if a+b==name+password:
                Runing=False
                Date=tm.ctime()
                print(f"Hi! Owais Today is {Date}")
                print("So,it's your today's schedule".upper())
                for i in range(0,len(Time)):
                    SCH=(f"At {Time[i]} o'clock \n {Ruteen[i]}")
                    print(SCH)
                    sd.every(30).seconds.do(noti)
                    while True:
                        sd.run_pending()
                        tm.sleep(1)
                        
            elif a+b!=name+password:
                wrng=input("Invalid user name or password\npress 'B' to back or 'R' to retry: ")
                if wrng=="b":
                    break
                elif wrng=='r':
                    Runing=True
    elif starter=="3":
        sd.every(30).seconds.do(noti)
        while True:
            sd.run_pending()
            tm.sleep(1)

                

    else:
        print("Not Valid Operation please press 1")
        start=True
