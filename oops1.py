#initate class
class employee:
    #special method/magic method/dunder method
    def __init__(self):
        print("Started executing attributes/data members")
        self.id=101
        self.name="John"
        self.designation="Developer"
        print("attributes/data members execution completed")
    
    def travel(self,destination):
        print("This travel function was called manually")
        print(f"{self.name} is travelling to {destination}")

#creating object of class
sam=employee()

#   print(sam.id)
#sam.travel("New York")

print(type(sam))
