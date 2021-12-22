# This is my first time using python classes


# make a class for cars
class Car:
    
    def __init__(self,speed,colour,price):
        self.speed = speed
        self.price = price
        self.colour = colour
        
    def getValue(self):
        value = self.speed/self.price
        return value

    def getColour(self):
        return self.colour
    
test = Car(80,'black',40000)
secondInstance = Car(150,'red',55000)

print(Car.getValue(test))
print(Car.getValue(secondInstance))

print(secondInstance.getValue())

print(test.colour)
print(Car.getColour(test))
print(Car.getColour(secondInstance))