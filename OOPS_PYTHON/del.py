class Student:
    def __init__(self , name):
        self.name = name
        

s1 = Student("vivek")
del  (s1)
print(s1.name)#it will be not printed because we delete se by using del 
