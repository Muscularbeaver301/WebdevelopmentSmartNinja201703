newList = []

while True:
    item = raw_input("Enter item, or 'X' to exit: ")
    if item == 'X':
        break
    else:
        newList.append(item)

print "Your List: ", newList
