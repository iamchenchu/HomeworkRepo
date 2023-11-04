class Student:
    def __init__(self,first_name,last_name,age,major,gpa,university):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.major = major
        self.gpa = gpa
        self.university = university

    def display_Details(self):
        print(f"Name         :{self.first_name} {self.last_name}")
        print(f"Age          : {self.age}")
        print(f"Major        : {self.major}")
        print(f"CGPA         : {self.gpa}")
        print(f"University   : {self.university}")

