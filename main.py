import datetime, bday_message

today = datetime.date.today()
next_birthday = datetime.date(2025, 10, 13)

print(today)
print(next_birthday)
days_away = next_birthday - today
print(days_away.days)

if today == next_birthday:
    print(bday_message.random_message)
else:
    print(f"My next birthday is {days_away.days} days away!")