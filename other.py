class Computer:
    
    def __init__(self, price):
        self.maxprice = price
    
    def sell(self):
        print("Selling Price: {}".format(self.maxprice))
    
    def setMaxPrice(self, price):
        self.maxprice = price

c = Computer(1000)
c.sell()

# change the price
c.maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()