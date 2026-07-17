city = input("Enter you city name:")
temp = float(input("Enter temp of your city in C:"))


print("City:",city)
print("Temperature:", temp)


# if statement------------------------------------------------


if temp > 35:
    print("Weather was very hot,stay on your home ")
    
elif temp > 25:
    print("It's warm weather")
    
elif temp < 15:
    print("wear jacket it's cold")
    
else:
    print("stay safe😊😊")
    
    
    
    
    
# datetime-module------------------------------------------------

import datetime
import calendar



now = datetime.datetime.now()
print("City:", city)
print("Time now", now)


print("Time now:", now.strftime("%Y-%m-%H:%M:%S"))
print("\n--- Year Calendar ---")


print(calendar.calendar(now.year))



#other-project's------------------------------------------

number = int(input("Enter Number to check")) 
print("Number to be checked :", number)

if number%2==0:
    print("This is an even number")
else:
    print("This is an odd number")
    
    
    
    # another -------------------------------------------
    
    num = int(input("Enter number to check :"))
    
    if num > 50:
        print("Number is greater than 50")
        if num % 2 == 0:
            print("And it is even too")
        else:
            print("And it is odd")
    else:
        print("Number is less than 50")

    print("Number is less than 50")
    
    

    
    

