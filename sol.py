from datetime import datetime, timedelta
current_datetime = datetime.now()

#Task1 


year = current_datetime.year
month = current_datetime.strftime("%B")
week = current_datetime.strftime("%U")
weekday = current_datetime.strftime("%w")
day = current_datetime.strftime("%j")
day_month = current_datetime.day
day_wich = current_datetime.strftime("%A")


print(f"Current date and time: {current_datetime}")
print(f"Current year: {current_datetime.year}")
print(f"Month of year: {month}")
print(f"Week number of the year: {week}")
print(f"Weekday of the week: {weekday}")
print(f"Day of year: {day}")
print(f"Day of the month : {day_month}")
print(f"Day of week: {day_wich}")



#Task 2
current_datetime = datetime.now().date()
yester = current_datetime - timedelta(days=1)
tomor = current_datetime + timedelta(days=1)



print(f"Yesterday : {yester}\nToday : {current_datetime}\nTomorrow : {tomor}")


#Task 3

current_datetime = datetime.now()

moms_later = current_datetime + timedelta(seconds=5)

print(f"Current time: {current_datetime}\nAfter adding 5 seconds: {moms_later}")


#Task 4

print(f"Today: {current_datetime}\nNext 5 days:")
i = 0
while i <= 4:
    print(current_datetime)
    current_datetime = current_datetime + timedelta(days=1) 
    i += 1

#Task 5

print(f"Today: {current_datetime}\nDay of the year:{current_datetime.strftime('%j')}")

#Task 6
current_datetime = datetime.now().date()
today = current_datetime.weekday()
monday= current_datetime - timedelta(days=today)

print(f"The first Monday of this week was: {monday}")


#Task 7
year= int(input("Input a year:"))

sunday = 6

found_sundays= []

date = datetime(year, 1, 1)

while date.year == year:
    if date.weekday() == sunday:
        found_sundays.append(date)
    date += timedelta(days=1)

for found in found_sundays:
    print(found.strftime("%Y-%m-%d"))
