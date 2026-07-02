class Employee():
    def __init__(Self, salary , name , bond):
        Self.salary = salary # creat an instance attribute of name salary and assign it with salary
        Self.name = name
        Self.bond = bond
    
    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"the name of the employee is {self.name}. Salary is {self.salary}. the bond is for {self.bond} years ")



e1 = Employee(34000, "Johan Doe", 4)
#print(e1.get_salary())
e1.get_info()
