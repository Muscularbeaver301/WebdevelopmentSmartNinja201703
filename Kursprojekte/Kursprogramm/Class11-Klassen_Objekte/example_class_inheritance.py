class Person(object):
    def talk(self):
        print 'I am a Person'

class Woman(Person):
    def gender(self):
        print 'I am female'


class Man(Person):
    def gender(self):
        print 'I am male'


if __name__ == '__main__':
    anton = Man()
    johanna = Woman()

    # both classes have their own gender function
    anton.gender()
    johanna.gender()

    # both classes can access the talk method of the parent class
    anton.talk()
    johanna.talk()
