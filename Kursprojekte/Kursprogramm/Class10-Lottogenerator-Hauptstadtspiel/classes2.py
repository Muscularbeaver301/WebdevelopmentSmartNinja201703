class Person(object):
    def sprechen(self):
        print "Hallo ich bin eine Person"


class Frau(Person):
    def sprechen(self):
        print "Hallo, ich bin eine Frau"


class Mann(Person):
    def sprechen(self):
        print "Hallo, ich bin ein Mann"


if __name__ == '__main__':
    P1 = Person()
    P1.sprechen()
    Lili = Frau()
    Lili.sprechen()
    Leo = Mann()
    Leo.sprechen()

