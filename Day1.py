class Employee:
    def __init__(self):
        self.Name = "Vikas"
        self.Id = 123
        self.Dept  = "AI"
        self.Salary   = 100000
        self.Designation = "Senior Developer"


    def Travel(self,destination):

        print(f"Employee is now traving to the {destination}")
        





emp = Employee()

emp.Travel("Japan")
