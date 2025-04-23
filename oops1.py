
class Employee:
    def __init__(self,id,salry,designation="SrE"):
        self.id=id 
        self.salary=salry
        self.designation=designation
        
        
    def travel(self,destination):
        print(f"Employee with his {self.id} and {self.designation} is now travelling to {destination}")

sam=Employee(12,500000,"Ram")   
sam.travel("Kerala")



