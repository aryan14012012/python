city = input("Enter you city name:")
temp = float(input("Enter temp of your city in C:"))


print("City:",city)
print("Temperature:", temp)


# if statement


if temp > 35:
    print("Weather was very hot,stay on your home ")
    
elif temp > 25:
    print("It's warm weather")
    
elif temp < 15:
    print("wear jacket it's cold")
    
else:
    print("stay safe😊😊")
    
    
    
    
    
# datetime-module

import datetime
import calender



now = datetime.datetime.now()
print("City:", city)
print("Time now", now)


print(calender.calender(now.year))



