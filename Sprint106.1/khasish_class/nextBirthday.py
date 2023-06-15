from datetime import datetime, timedelta
user_birthday_input = input("Enter your birth date  (format: DD/MM/YYYY): ")

#convert the date string to datetime

birthday = datetime.strptime(user_birthday_input, "%d/%m/%Y")
print(birthday)
# calculate the next birthday number of days
curr_date = datetime.now()
next_birthday = datetime(curr_date.year, birthday.month, birthday.day)
if curr_date > next_birthday:
    next_birthday = next_birthday.replace(year = curr_date.year + 1)

time_till_next_birthday = next_birthday - curr_date
days_till_next_birthday = time_till_next_birthday.days

# calculate exact float age
time_alive = curr_date - birthday
exact_age = time_alive.days / 365

#the day of the week the user born
birthday_weekday = birthday.strftime("%A")


# printing the output

print("Days until next birthday:", days_till_next_birthday)
print("Exact float age:", round(exact_age, 1))
print("Day of the week of birth:", birthday_weekday)


