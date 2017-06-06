class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print 'I am a Person'

if __name__ == '__main__':
    anton = Person('Anton',25)
    anton.talk()
