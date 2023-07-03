class fruits:
    def __init__(self,type,color,price,shape):
        self.fruittype=type
        self.fruitcolor=color
        self.fruitprice=price
        self.fruitshape=shape

    def display(self):
        print(self.fruittype,self.fruitcolor,self.fruitprice,self.fruitshape)

myobj=fruits("Banana","Green",20,"square")
myobj.display()





