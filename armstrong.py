def is_armstrong(number):
   
    num_str = str(number)
    power = len(num_str)
    
    
    total_sum = sum(int(digit) ** power for digit in num_str)
    

    return total_sum == number


num = int(input("Enter a number: "))

if is_armstrong(num):
    print(f"{num}  is a Armstrong number")
else:
    print(f"{num} is not a Armstrong number")
