class Snake(object):
    def __init__(self, name):
        self.name = name
        self.food = []

    def eat(self, newfood):
        self.food.append(newfood)



if __name__ == '__main__':
    franz = Snake("Franz")
    franz.eat("Apfel")
    franz.eat("Maus")
    franz.eat("Martin")
    print franz.name
    print franz.food
