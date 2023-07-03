# class called people that has name,age and gender
class people:
    def __init__(self, name, age, gender):
        self.peoplename = name
        self.peopleage = age
        self.peoplegender = gender

    def display(self):
        print(self.peoplename, self.peopleage, self.peoplegender)


mylist = people("Maryanne", 19, "Female")
mylist1 = people("John", 20, "Male")
mylist2 = people("April", 21, "Female")
mylist.display()
mylist1.display()
mylist2.display()
