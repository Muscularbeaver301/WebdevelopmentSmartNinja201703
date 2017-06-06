class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print 'I am a Person'

    def introduce(self):
        print 'Hi, my name is %s'%self.name

if __name__ == '__main__':
    anton = Person('Anton', 25)
    marie = Person('Marie', 26)
    anton.introduce()
    marie.introduce()
