class Person:
    def __init__(self,name,contact):
        self.name=name
        self.contact=contact
    def address():
        print("name and contact")
        
class Doctor(Person):
    pass
class Patient(Person):
    pass


person1=Doctor(name="rifa",contact=123)
person2=Patient(name="thasneem",contact=345)

print(person1.name)
print(person2.contact)

Person.address()