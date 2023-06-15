from datetime import datetime, timedelta
#  

one_bill_sec = 1000000000

# Create a timedelte object wihtin the given numbmer of seconds
delta = timedelta(seconds=one_bill_sec)

current_datetime = datetime.now()
#subtract the timedelta from the birthday when the user born

#result_time_delts = delta - birthday.date()

target_datetime = current_datetime + delta

#print(result_time_delts)
print(target_datetime)