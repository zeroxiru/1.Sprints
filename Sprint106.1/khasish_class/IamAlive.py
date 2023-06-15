from datetime import datetime, timedelta
user_birthday_input = input("Enter your birth date  (format: DD/MM/YYYY): ")

#convert the date string to datetime

birthday = datetime.strptime(user_birthday_input, "%d/%m/%Y")

# calculate the number of days
curr_date = datetime.now()
time_till_alive = curr_date - birthday

days_still_live = time_till_alive.days

print(f" NUmber of days alive: {days_still_live}")
