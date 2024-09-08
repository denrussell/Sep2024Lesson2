year = int(input("Please enter a year: "))

leapyear = year % 4 == 0
leap100 = year % 100 == 0
leap400 = year % 400 == 0

if leapyear and leap100 and leap400:
     print(year,"is a leap year.")
elif leapyear and leap100:
     print(year,"is Not.")
elif leapyear:
     print(year,"is a leap year!")
else:
     print(year,"is Not.")

'''      

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year," is a leap year.")
    print(year," is a leap year.")
else:
        print(year, "is Not.")
'''