# Class and Object, Inheritance, Encapsulation Practise
class Car:

    def __init__(self):
        self.car_name = ""
        self.car_model = 0
    
    def name(self):
        # self.car_name = "swift"
        print(f"name of car is : {self.car_name}")
    
    def model(self):
        # car_model = 2015
        print(f"model of car is : {self.car_model}")

name = str(input("Ente the car name : "))
model = int(input("Enter the car model : "))

car1 = Car()
car1.car_name = name
car1.car_model = model

car1.name()
car1.model()
    