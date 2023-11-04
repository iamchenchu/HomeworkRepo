class Professor:
    def __init__(self,prof_name,subject,experience,city):
        self.prof_name = prof_name
        self.subject = subject
        self.experience = experience
        self.city = city

    def display_Details(self):
        print(f"Name         :{self.prof_name}")
        print(f"Department   : {self.subject} department")
        print(f"Experience   : {self.experience}")
        print(f"City         : {self.city}")

