class Car:

    # class attribute
    name = ""
    model = 0

# creation of object
car1 = Car()
car1.name = "Swift"
car1.model = 2015

car2 = Car()
car2.name = "nexon"
car2.model = 2019

print(f"car name : '{car1.name}' and model of car is : {car1.model}")
print(f"car name : '{car2.name}' and model of car is : {car2.model}")