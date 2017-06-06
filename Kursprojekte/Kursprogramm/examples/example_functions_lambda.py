def add():
    return lambda a,b: a+b

num1 = 10
num2 = 20

# add() returns a lambda function
adder = add()

print "add(%i,%i) returns: %i" % (num1, num2, adder(num1, num2))

