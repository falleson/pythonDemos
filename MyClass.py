class MyClass(object):
    common=10
    def __init__(self):
        self.myvariable=3
    def myfunction(self,arg1,arg2):
        return arg1+arg2+self.myvariable

classa = MyClass()
print(classa.myfunction(1,5))
import random
print(random.randint(1,100))

