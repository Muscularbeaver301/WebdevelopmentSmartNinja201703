class Snake(object):
    def __init__(self,name):
        self.name = name
        self.belly = []
    def eat(self,food):
        self.belly.append(food)

if __name__ == '__main__':
    s1 = Snake("Billy")
    s2 = Snake("Johnny")
    s1.eat("Apple")
    s1.eat("Honey")
    s2.eat("Spaghetti")
    print s1.belly
    print s1.__dict__