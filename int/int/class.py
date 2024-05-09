class Car:
    def __init__(self,name,price,color):
        self.name=name
        self.price=price
        self.color=color
    def start(self):   
        print("guyss")


car1=Car(name="audi",price=100000,color="black")
car2=Car(name="creta",price=150000,color="blue")

print(car1.color)
print(car2.price)
car2.start()