#FutureTime.py
#Name: Gavin Lakner
#Date: 9/7/2025
#Assignment: Future Time

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour -8 ) % 24
  currentMinute = (now.minute - 4)

  print (currentHour, currentMinute) #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours
moreHr = (currentHour + moreHr) % 60
  #Ask user for minutes
moreMins = 5

futureMins = (currentMinute + moreMins ) % 60
extraHour = (currentMinute + moreMins ) // 60

  #Calculate the time after the user-supplied time has passed.

  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"


if __name__ == '__main__':
  main()
