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