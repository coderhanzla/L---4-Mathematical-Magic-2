import datetime
import time

while True:
    now = datetime.datetime.now()
    print(now.strftime('%Y-%m-%d %H:%M:%S'), end="\r")
    time.sleep(1)



   
