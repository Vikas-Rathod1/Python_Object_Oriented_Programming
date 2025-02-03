class Employee:
    # special method/ magic method/ dunder method ---- Constructor
    def __init__(self):
        # print("Inside the Initial Constructor")
        self.Name = "Vikas"
        self.Id = 123
        self.Dept  = "AI"
        self.Salary   = 100000
        self.Designation = "Senior Developer"
        #print("Inside at end of the attribute in Constructor")


    def Travel(self,destination):
        print("Inside Travel function")

        print(f"Employee is now traving to the {destination}")
        


#

# creating object of Class
emp = Employee()


#printing the attributs 

print(emp.Dept , emp.Designation, emp.Name, emp.Salary)

#Calling method using object
emp.Travel("Japan")
