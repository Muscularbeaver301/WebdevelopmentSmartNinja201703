class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friends=[]

    def talk(self):
        print 'I am a Person'

    def introduce(self):
        print 'Hi, my name is %s'%self.name

    def getOlder(self):
        self.age += 1

    def make_friend(self,newfriend):
        self.friends.append(newfriend)

    def show_friends(self):
        print 'This is a list of my friends: ', self.friends

if __name__ == '__main__':
    anton = Person('Anton',15)
    anton.make_friend('Thomas')
    anton.make_friend('Thea')
    anton.make_friend('Theresa')
    anton.make_friend('Thor')
    anton.show_friends()
