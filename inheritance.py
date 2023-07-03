class Animal:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def speak(self):
        raise NotImplementedError("Child classes must implement this method")
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"
class Lion(Animal):
    def speak(self):
        return "Roar!"


# create am object
dog=Dog("Bosco","White")
print(dog.name)
print(dog.color)
print(dog.speak())
print("  ")


cat=Cat("Greyie","Grey")
print(cat.name)
print(cat.color)
print(cat.speak())
print("  ")

lion=Lion("Simba","Brown")
print(lion.name)
print(lion.color)
print(lion.speak())
print("  ")
 # class called vehicle with model and brand

class vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def speak(self):
        NotImplementedError("Child classes must implement this method")
class fastcars(vehicle):
    def speak(self):
        return "skrrrrrr!"
class luxuriouscars(vehicle):
    def speak(self):
        return "vrooom!"
class electriccars(vehicle):
    def speak(self):
        return "vooooom"
fastcars=fastcars("Toyota","Supra")
print(fastcars.brand)
print(fastcars.model)
print(fastcars.speak())
print("  ")
luxuriouscars=luxuriouscars("RollsRoyce","Cullinan")
print(luxuriouscars.brand)
print(luxuriouscars.model)
print(luxuriouscars.speak())
print("  ")
electriccars=electriccars("Tesla","Model Y")
print(electriccars.brand)
print(electriccars.model)
print(electriccars.speak())