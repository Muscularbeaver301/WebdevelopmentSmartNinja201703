"""
This file is about:
1) Creating a class
    Class is a blueprint for a datastructure
    it can bundle different datatypes and functions

2) set fields of that class by using the __init__ function

3) we create an instance of a Person. we call that instance 'anton'

4) we print the fields 'name' and 'age' saved for the instance anton
"""

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Account(object):
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

if __name__ == '__main__':
    anton = Person('Anton', 25)
    frauke = Person('Frauke', 25)

    myAccount = Account('Pat', -1000)

    print "Account of %s has Balance of %.3f EUR"%(myAccount.name,myAccount.balance)
    myAccount.balance = 1000000
    print "Account of %s has Balance of %.3f EUR" % (myAccount.name, myAccount.balance)
