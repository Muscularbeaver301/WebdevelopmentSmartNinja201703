def add(erstezahl, zweitezahl):
    mySum = erstezahl + zweitezahl
    return mySum

def multiplication(a,b):
    return a*b

def division(a,b):
    if b!=0:
        return a/b
    else:
        return None

def minus(a,b):
    diff = a-b
    return diff

num1 = 10
num2 = 20
summe = add(num1, num2)
product = multiplication(num1,num2)
ratio = division(num1,num2)

difference = minus(num1,num2)

print "add(%i,%i) returns: %i" % (num1, num2, summe)

print "multiplication(%i,%i) returns: %i" % (num1, num2, product)

print "subtract(%i,%i) returns: %i" % (num1, num2, difference)

