class calculator :

    def __init__(self, num) :
        self.num = num
    
    def square(self) :
        print(f"square of {self.num} is {self.num **2}")
        
    def root(self) :
        print(f"square root of {self.num} is {self.num **0.5}")
        
    def cube(self) :
        print(f"cube of {self.num} is {self.num **3}")
    
a = calculator(9)
a.square()
a.cube()
a.root()
