import datetime

event = input("Enter event title: ")
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

event_date = datetime.date(year, month, day)
formatted_date = event_date.strftime("%B %d, %Y")
month_name = event_date.strftime("%B")
weekday = event_date.strftime("%A")

print("\nFormatted Output:")
print("Event:", event.upper())
print("Date:", formatted_date)
print("Year:", year)
print("Month:", month_name)
print("Day:", day)
print("Weekday:", weekday)
