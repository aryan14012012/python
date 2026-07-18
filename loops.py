for a in range(1,11):
    
    print(f"22  x {a}  = {22 * a}")
    
# stars------------------------------------------

n = int(input("Enter the number of rows :"))
for i in range(1,n+1):
    for j in range(i):
      print('*', end='')    
    print()
        
     #while-------------------------------------------
     
total_sum= 0
num = 1
      
      
while num <=10:
          total_sum += num
          num += 1
          
print(f"The sum of the first ten natural number is {total_sum}")

# prime number------------------------

num= int(input("Enter a number:"))

if num > 1:
     
     
     for i in range(2,int(num**0.5)+  1):
         
        if num % i ==0:
            print(f"{num} is not a prime number.")
            break
        
     else:
    
         print(f"{num} is a prime number.")
    
    
else:

    print(f"{num} is not a prime number.")
                     