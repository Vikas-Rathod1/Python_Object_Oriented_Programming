class Employee:
    def __init__(self):
        print("Inside the Initial Constructor")
        self.Name = "Vikas"
        self.Id = 123
        self.Dept  = "AI"
        self.Salary   = 100000
        self.Designation = "Senior Developer"
        print("Inside at end of the attribute in Constructor")


    def Travel(self,destination):
        print("Inside Travel function")

        print(f"Employee is now traving to the {destination}")
        





emp = Employee()

emp.Travel("Japan")
