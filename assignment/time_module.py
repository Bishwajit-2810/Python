import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def factorial(n):
    return math.factorial(n)

def power(a, b):
    return math.pow(a, b)

from datetime import datetime

now = datetime.now()
print("Current date and time:", now)
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)
print("Formatted Date (DD-MM-YYYY):", now.strftime("%d-%m-%Y"))
print("Formatted Date (YYYY/MM/DD):", now.strftime("%Y/%m/%d"))

from datetime import timedelta, date

date1 = date(2024, 1, 1)
today = date.today()
days_between = (today - date1).days
print("Days between 2024-01-01 and today:", abs(days_between))

add_100_days = today + timedelta(days=100)
print("Date after adding 100 days:", add_100_days)

subtract_50_days = today - timedelta(days=50)
print("Date after subtracting 50 days:", subtract_50_days)

from datetime import time

specific_time = time(14, 30, 15)
print("Specific time:", specific_time)

new_time = (datetime.combine(date.today(), specific_time) + timedelta(hours=1, minutes=45)).time()
print("Time after adding 1 hour and 45 minutes:", new_time)

time1 = datetime.combine(date.today(), time(14, 30, 15))
time2 = datetime.combine(date.today(), time(18, 0, 0))
time_difference = time2 - time1
print("Difference between 14:30:15 and 18:00:00:", time_difference)

formatted_date = now.strftime("%B %d, %Y at %I:%M %p")
print("Formatted current date and time:", formatted_date)

string_date = "06-12-2024"
parsed_date = datetime.strptime(string_date, "%d-%m-%Y")
print("Parsed date:", parsed_date)

invalid_date = "2024-13-01"
try:
    validated_date = datetime.strptime(invalid_date, "%Y-%m-%d")
    print("Valid date:", validated_date)
except ValueError:
    print("Invalid date format:", invalid_date)

input_date = date(2000, 1, 1)
day_of_week = input_date.strftime("%A")
print("Day of the week for 2000-01-01:", day_of_week)

is_weekend = today.weekday() >= 5
print("Today is a weekend:" if is_weekend else "Today is a weekday.")

from pytz import timezone, all_timezones
import pytz

utc_now = datetime.now(pytz.utc)
print("Current UTC time:", utc_now)

for tz in ["Asia/Dhaka", "America/New_York"]:
    tz_time = utc_now.astimezone(timezone(tz))
    print(f"Current time in {tz}:", tz_time)

source_tz = timezone("Asia/Dhaka")
dest_tz = timezone("America/New_York")
source_time = source_tz.localize(datetime(2024, 12, 15, 12, 0, 0))
converted_time = source_time.astimezone(dest_tz)
print("Time in Dhaka converted to New York time:", converted_time)

import time
start_time = time.time()
time.sleep(5)  
end_time = time.time()
elapsed_time = end_time - start_time
print("Elapsed time in seconds:", elapsed_time)

dob_input = input("Enter your date of birth (YYYY-MM-DD): ")
try:
    dob = datetime.strptime(dob_input, "%Y-%m-%d").date()
    age = today - dob
    years = age.days // 365
    months = (age.days % 365) // 30
    days = (age.days % 365) % 30
    print(f"You are {years} years, {months} months, and {days} days old.")
    print("You were born on a:", dob.strftime("%A"))
except ValueError:
    print("Invalid date format.")

countdown_seconds = int(input("Enter countdown time in seconds: "))
while countdown_seconds:
    mins, secs = divmod(countdown_seconds, 60)
    hours, mins = divmod(mins, 60)
    print(f"{hours:02}:{mins:02}:{secs:02}", end="\r")
    time.sleep(1)
    countdown_seconds -= 1
print("Time's up!")
