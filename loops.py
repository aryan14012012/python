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

