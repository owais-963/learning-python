import os
import time as t
from datetime import datetime as dt
from plyer import notification as nt
flag=True
while flag:
    P="02:50"
    y=dt.strptime(P,"%H:%M")
    #Sleep=y.hour
    Y=t.strftime("%H:%M")
    s=dt.strptime(Y,"%H:%M")
    #Sleep_Time=s.hour
    if y==s:
        nt.notify(
            title="My Daily Schedule",
            message="Hi!\nowais it's time to take break",
            app_icon=None,
            timeout=20,
            )
        break

