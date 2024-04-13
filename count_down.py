from functions import get_int
import time


def countdown(t): 
    
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1

print("Don`t leave any options empty, enter 0 for what you dont`t need")

hours = get_int("How many Hours: ")
minutes = get_int("How many Minutes: ")
seconds = get_int("How many Seconds: ")


total_second = (hours * 3600) + (minutes * 60) + seconds

# if second is negative
if total_second < 0:
    total_second *= -1


if seconds == 0:
    print("You can`t set a count down for 0 seconds")
    exit()

print("total seconds: ", total_second)

countdown(total_second)