#FutureTime.py
#Name: Gavin Lakner
#Date: 9/7/2025
#Assignment: Future Time

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour -5 ) % 24
  currentMinute = (now.minute + 1) 

  print (currentHour, currentMinute) #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours
moreHour = 1
  #Ask user for minutes
moreMins = 1

  #Calculate the time after the user-supplied time has passed.
futureMins = (currentMinute + moreMins ) % 60 
extraHour = (currentMinute + moreMins ) // 60 
# I have no idea why these won't work and after watching your lecture and video it should work and google gives no help

print (extraHour)
print (futureMins)
  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"
formatted_time = datetime.strftime("%H:%M")
#Found this online but I don't know if it works

if __name__ == '__main__':
  main()
