# coding=utf-8
class Account(object):

    def __init__(self,name, money):
        self.name = name
        self.money = money

    def print_details(self):
        print '%s\'s Account Balance: %15.2f €'%(self.name, self.money)

    def earn_money(self, amount):
        self.money += amount

    def spend_money(self, amount):
        self.money -= amount

if __name__ == '__main__':
    anton = Account('Alfred',0)
    anton.print_details()
    anton.earn_money(100)
    anton.earn_money(1000.34)
    anton.spend_money(86.22)
    anton.print_details()
