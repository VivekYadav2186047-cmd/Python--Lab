class Student:
    college_name =  "GL BAJAJ"
    name = "anonymmous" #class attribite
    def __init__(self , name , marks):
        self.name = name #object attribute > class attribute
        self.marks = marks


s1 = Student("vivek" , 100)
print(s1.name , s1.marks)

s2 = Student("roshan" , 99.9)
print(s2.name , s2.marks)
