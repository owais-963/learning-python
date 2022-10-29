#Trying to make a daily schedule
import time as tm
from datetime import datetime as dt
import os
from plyer import notification as nt
import schedule as sd
Time=["05:55"
,"6:00"
,"06:30"
,"08:30"
,"09:00"
,"10:00"
,'11:15',
"12:30"
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
,"18:47"]
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
name="owais ali"
password="myschedule.123"
Tm=tm.strftime("%H:%M")
def noti():
    if Tm in Time:
        MSG_No=Time.index(Tm)
        MSG=Ruteen[MSG_No]
        for i in range(0,1):
            nt.notify(title="My Daily Schedule",message=f"{MSG}",app_icon=None,timeout=20,)
        
#Ruteen=[r0,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16,r17,r18]
##########################################################################
"*************************************************************************"
Flag=True
while Flag:
    print("I am your noifier to ntoify you about your daily schedule".upper())
    starter=input("to See the schedule press '1' and Enter your name and password\nPress 3 to continue\nAnd press 0 to dismiss: ".title())
    if starter=='0':
        break
    elif starter=='1':
        Flag=False
        Run=True
        while Run:
            a=input("Name: ")
            b=input("Password: ")
            if a+b==name+password:
                Date=tm.ctime()
                print(f"Hi! Owais Today is {Date}")
                print("So,it's your today's schedule".upper())
                for n in range (0,len(Time)):
                    print(f"At {Time[n]} o'clock \n{Ruteen[n]}")
                    sd.every(30).seconds.do(noti)
                    while True:
                        sd.run_pending()
                        tm.sleep(1)
            elif a+b!=name+password:
                wrng=input("Invalid user name or password\npress 'B' to back or 'R' to retry: ")
                if wrng=="b":
                    Run=False
                    Flag=False
                    break
                elif wrng=='r':
                    Run=True
    elif starter=="3":
        sd.every(30).seconds.do(noti)
        while True:
            sd.run_pending()
            tm.sleep(1)

    else:
        print("Not Valid Operation please press '1' , '3' & '0' ")







