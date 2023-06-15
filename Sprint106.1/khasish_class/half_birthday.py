from datetime import datetime, timedelta

birthday = "28/06/1989"

days = 182

delta = timedelta(days=days)

convert_Str_to_datetime = datetime.strptime(birthday, "%d/%m/%Y")
exact_half_birthday_calculation = convert_Str_to_datetime + delta

print(exact_half_birthday_calculation)
