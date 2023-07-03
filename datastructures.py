# list datastructure
# a list enables you to change data
myclassmate = ["Eric", "Joan", "Daniel", "Susan", "Purity"]
mynumber = [4, 9, 20, 3, 1, 50, -9]
myclassmate[0] = "Daniel"
mynumber.sort()
myclassmate.append("Christine")
myclassmate.insert(2, "Michael")
myclassmate.pop(0)
print(myclassmate)
print(mynumber)
for names in myclassmate:
    print(names)

# this is a tuple
countries = ("Kenya", "Uganda", "Tanzania", "Burundi")
print(countries)

# sets datastructure

cars = {"Toyota", "Nissan", "Mercedes", "Subaru", "Rangerover"}
print(cars)
for brands in cars:
    print(brands)

# dictionaries data structure

matunda = {
    "price": 50,
    "color": "Green",
    "Name": "banana"
}
matunda["shape"] = "Oval"


print(matunda)
manguo = {
    "price": 1000,
    "color": "Black",
    "Name": "Mom jeans"
}
print(manguo)
x = matunda["price"]
print(x)
y = matunda["Name"]
print(y)
