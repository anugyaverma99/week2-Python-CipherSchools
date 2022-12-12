

#The __init__ method
#Dunders(magic methods)
'''
__<name of dunder>__
'''
class Person:
    def __init__(self,name):
        self.name=name
    def say_hi(self):
        print("Hello, My Name is",self.name)
p=Person("ASHU")
p.say_hi()

a=1
print(a+1)
print(str(a))

class a:
    def __init__(self):
        print(self)
        print("initialized")
    def __del__(self):
        print(self)
        print("I am fine")
b=a()
'''
class a:
    def __init__(self):
        raise Exception()
        print(self)
        print("initialized")
    def __del__(self):
        print(self)
        print("I am fine")
b=a()
'''

a=1
print(type(a))
print(a.__add__(5))
'''
a=1 has a dunder add
'''

print("Anugya"*2)
print("Anugya".__mul__(2))

class A:
    a=1
    b=2
    def __add__(self,x):
        return self.a+self.b+x
a=A()
a=a+3