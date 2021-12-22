# make a class, and use a class variable

class Car:
    
    # Class variable - the number of cars in stock
    numOfCars = 0
    
    # Class variable - sale percentage
    salePercent = 0.2
    
    def __init__(self,speed,price,colour):
        self.speed = speed
        self.price = price
        self.colour = colour
        # update the number of cars anytime a new instance is made
        Car.numOfCars += 1
        
    # Method that returns the colour of the car
    def getColour(self):
        return self.colour


    # Method that puts a car on sale (reduces price)
    def reducePrice(self):
        self.price -= self.price * Car.salePercent
        
    def reducePrice2(self,salePercent):
        self.price -= self.price * salePercent
        return self.price
    
    
    # representation of instance
    def __repr__(self):
        str_to_return = 'Car({}, {}, {})'.format(self.speed,self.price,self.colour)
        return str_to_return


        
    
print(Car.numOfCars)
car1 = Car(90,30000,'red')
print(Car.numOfCars)
car2 = Car(110,50000,'yellow')
print(Car.numOfCars)
print()

print(car1.price)
Car.reducePrice(car1)
print(car1.price)



### THIS IS A CLASS VARIABLE, SO IT UPDATES THE SALE PERCENTAGE VARIABLE FOR THE WHOLE CLASS
Car.salePercent = 0.5 
### ANY TIME THE REDUCE PRICE METHOD IS NOW RUN, IT WILL BE RUN WITH A NEW SALE PRICE

print()
print('Car2')
print('original price: ',car2.price)
print('Sale percentage: ',100*Car.salePercent)
Car.reducePrice(car2)
print('New price: ',car2.price)


### SECOND WAY BY PASSING THE 
car3 = Car(150,95000,'blue')
print()
print('Car3')
print('original price: ',car3.price)
userDefinedSale = 0.3
print('Sale percentage: ',userDefinedSale)
Car.reducePrice2(car3,userDefinedSale)
print('New price: ',car3.price)
print()

print('Cars in stock: ',Car.numOfCars)

print()
print(car1)