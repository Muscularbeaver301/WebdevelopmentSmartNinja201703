class Car(object):
    def __init__(self, Type, Engine, Horsepower, Date):
        self.Type = Type
        self.Engine = Engine
        self.Horsepower = Horsepower
        self.Date = Date




Renault = Car('Espace', '1,9 DCI', 120, 2008)

Ford = Car('Mustang', '2.0T', 299, 1969)
print (Ford.Type, Ford.Engine)
print (Renault.Engine, Renault.Type)







