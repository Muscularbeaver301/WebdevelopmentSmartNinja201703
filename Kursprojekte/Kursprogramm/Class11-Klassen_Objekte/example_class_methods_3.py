class Dish(object):
    def __init__(self, name, price, currency):
        self.name = name
        self.price = price
        self.currency = currency

    def toohot(self):
        print("The dish %s is too hot!") %self.name

    def toocold(self):
        print("The dish %s is too cold!") %self.name

    def inflation(self):
        self.price = self.price * 1.05
        print("The dish %s got more expensive because of inflation. New price: %2.2f %s." %(self.name, self.price, self.currency))

if __name__ == '__main__':
    dish1 = Dish('Pasta Bolognese', 8.90, 'EUR')
    dish2 = Dish('Pasta Carbonara', 9.20, 'EUR')
    print("The first dish on the menu is %s and costs %2.2f %s." % (dish1.name, dish1.price, dish1.currency))

    print("Set currency to USD.")
    dish2.currency = 'USD'

    print("The first dish on the menu is %s and costs %2.2f %s." % (dish1.name, dish1.price, dish1.currency))
    print("The second dish on the menu is %s and costs %2.2f %s." % (dish2.name, dish2.price, dish2.currency))

    dish1.toohot()
    dish2.toocold()
    dish1.inflation()