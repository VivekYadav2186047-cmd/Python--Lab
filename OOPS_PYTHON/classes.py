class employee():
    company = "HP"

    def get_salary(self):
        return 50000
    
e1 = employee()#an object of class employee is created here 
print(e1.get_salary())#employee e's get salary method is called 

e2 = employee()
print(e2.get_salary())
print(e2.company)
