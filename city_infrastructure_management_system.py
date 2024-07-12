

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    
    
    def update_owner(self, updated_owner):
        self.owner = updated_owner
        
        
        
    
Vehicle1 = Vehicle(321, "car", "John")
Vehicle2 = Vehicle(152, "bike", "Amy")
Vehicle3 = Vehicle(455, "motorcycle","Hector")

Vehicle1.update_owner("Scott")
print(Vehicle1.owner)

Vehicle2.update_owner("Jenny")
print(Vehicle2.owner)

Vehicle3.update_owner("Sam")
print(Vehicle3.owner)


