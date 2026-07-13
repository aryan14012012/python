# My Travel Ticket Counter

passenger_name = "Ava"
destination = "Paris"
ticket_price = 120.50
number_of_tickets = 2
is_round_trip = True

print("Passenger Name:", passenger_name)
print("Destination:", destination)
print("Ticket Price:", ticket_price)
print("Number of Tickets:", number_of_tickets)
print("Round Trip:", is_round_trip)
print("Data Type of Passenger Name:", type(passenger_name))
print("Data Type of Ticket Price:", type(ticket_price))
print("Data Type of Number of Tickets:", type(number_of_tickets))
print("Data Type of Round Trip:", type(is_round_trip))

# Calculate the total ticket cost
total_cost = ticket_price * number_of_tickets
print("Total Ticket Cost:", total_cost)

# Compare values
print("Is the ticket price greater than 100?", ticket_price > 100)
print("Are there at least 2 tickets?", number_of_tickets >= 2)
print("Is the ticket a round trip?", is_round_trip == True)

# Work with text
booking_info = passenger_name + " is traveling to " + destination
print("Booking Info:", booking_info)
print("Length of Booking Info:", len(booking_info))
print("First Character:", booking_info[0])
print("Uppercase Booking Info:", booking_info.upper())

# Swap two ticket prices to show variable updates
price_a = 75.0
price_b = 90.0
print("Before swap:", price_a, "and", price_b)

temp = price_a
price_a = price_b
price_b = temp

print("After swap:", price_a, "and", price_b)
