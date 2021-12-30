class Plane:
    plane = "singapur to india"
    print("*****Welcome to spice Jet*****")

    def __init__(self,name,age,price,seats,FlightNo):
        self.name = name
        self.age = age
        self.price = price
        self.seats = seats
        self.FlightNo = FlightNo


    def getDetail(self):
        print(f"Respected {self.name}!")
        print(f"\nThe Flight NO. for your ticket is {self.FlightNo}")
        print(f"\nThe seats available in the flight are {self.seats}")

    def bill(self):
        print(f"\nThe price for one ticket is {self.price}")

    def bookTicket(self):
        if(self.seats>0):
            print(f"\nYour ticket is booked and Your ticket number is {self.seats}")
            print(f"Your bill is {self.price}\n")
            self.seats = self.seats - 1
        else:
            print("Sorry,The seats are full!\n")
            print("You can check business class\n")

p1 = Plane("passenger1",35,2500,3,"G-1990")
p2 = Plane("passenger2", 20, 3400, 2, "G-1990")
p3 = Plane("passenger3", 41, 4000, 1, "G-1990")
p4 = Plane("passenger4", 24, 2500, 0, "G-1990")

p1.getDetail()
p1.bill()
p1.bookTicket()

p2.getDetail()
p2.bill()
p2.bookTicket()

p3.getDetail()
p3.bill()
p3.bookTicket()

p4.getDetail()
p4.bill()
p4.bookTicket()
