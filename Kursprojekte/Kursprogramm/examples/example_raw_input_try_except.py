number = None
while not number:
    try:
        userinput = raw_input("Enter an integer number: ")
        number = int(userinput)
    except Exception as e:
        print
        print "Error: "
        print e.message
        print "Please try again"
        print
else:
    print "You entered the valid number: ", number