#FutureTime.py
#Name:Nomaan Ahmed 
#Date:2/2/25
#Assignment:Lab 2 

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = now.hour
  currentMinute = now.minute

  print (currentHour, currentMinute) #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours
  additional_hours = int(input("Enter additional hours: "))
  #Ask user for minutes
  additional_minutes = int(input("Enter additional minutes: "))
  #Calculate the time after the user-supplied time has passed.
  total_minutes = currentMinute + additional_minutes
  total_hours = currentHour + additional_hours + (total_minutes // 60)
  new_minutes = total_minutes % 60
  new_hours = total_hours % 12
  new_hours = 12 
  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"
  print("The time after {additional_hours} hours and {additional_minutes} minutes will be {new_hours:02}:{new_minutes:02}")

if __name__ == '__main__':
  main()
