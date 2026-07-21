class A:
    varA = "welcome to A"

class B :
    varB = "welcome to B"

class C(A , B):
    varC = "welcome to c"


c1 = C()
print(c1.varA)
