class employee:
    company = "asus" #this is a class attribute

    def __init__(self, salary, name, bond,company):
        self.salary = salary #create an instance attribute of name salary and assigns it with salary
        self.name = name
        self.bond = bond
        self.company = company
    
    def get_salary(self):
        return self.salary
    def get_info(self):
        print(f"the name of the employee is {self.name} . Salary is {self.salary} . the bond is for {self.bond} years")


e1 = employee(34000, "john", 3, "Tesla")
print(e1.company) #will always print instance attribute whenever present
print(employee.company)#this will always print the class attribute

