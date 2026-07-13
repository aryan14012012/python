

snack_name="chips"
price=2.5
quantity=3
is_available=True


print("Snack Name:", snack_name)
print("Price:", price)
print("Quantity:", quantity)
print("Is Available:", is_available)



print(type(snack_name))
print(type(price))
print(type(quantity))
print(type(is_available))



total= price * quantity
print("Total Cost:$", total)
print("Sale Price:$",price  - 0.25)
print("Double Price:$",quantity * 2)




print("is price under $2?", price < 2)
print("is there more than 5 in stock?", quantity > 5)
print("is price exactly $2.5?", price == 2.5)



shop_name ="quick" +" "+"snack"
print("Shop Name:", shop_name)
print("letter in snack name :", len(snack_name))
print("First letter:", snack_name[0])





price_a= 2.5
price_b= 3.0

print("before :", price_a, "and" , price_b)

temp      = price_a
price_a     = price_b
price_b     = temp
