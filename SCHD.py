import schedule
import time as tm
def pr():
    print("xyz")
schedule.every(30).seconds.do(pr)
while True:
    schedule.run_pending()
    tm.sleep(1)