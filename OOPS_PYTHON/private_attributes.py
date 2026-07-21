class Account:
    def __init__(self , acc_no , acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass #now this is become private at we can not acces it outside the class

    def reset_pass(self):
        print(self.__acc_pass)


acc1 = Account("12345" , "abcdfe")

print(acc1.acc_no)

print(acc1.reset_pass()) #printed beacuse it is out of the class
