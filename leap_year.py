import calendar
y=int(input("Enter year:"))
print("Leap year"if calendar.isleap(y) else "Not leap year")
