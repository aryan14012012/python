print("Book ticket from NDLS")
destination = input("Enter your destination from NDLS(New delhi): ")
name = input("Enter your name:")
age = input("Enter your age: ")
passengers = int(input("Number of passengers: "))
price_per_ticket = 22

print("price of 1ticket=22$")



total_price = passengers * price_per_ticket
print(f"Total price for {passengers} passengers: {total_price}$")