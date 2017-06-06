# initialize
newList = []
print "newList = []"
print "newList ="
print newList
print


# append single elements
print "newList.append('Banana')"
print "newList="
newList.append('Banana')
print newList
print

# append add multiple elements with other lists
print "oldList = ['Milk', 'Honey']"
print "shoppingList = newList + oldList"
print "shoppingList="
oldList = ['Milk', 'Honey']
shoppingList = newList + oldList
print shoppingList
print

# refer to elements
print "shoppingList[0] ="
print shoppingList[0]
print "shoppingList[-1]="
print shoppingList[-1]
print

# refer to multiple elements
print "shoppingList[:-1]"
print shoppingList[:-1]
print "shoppingList[1:]"
print shoppingList[1:]
print

# reverse
print "shoppingList.reverse()"
shoppingList.reverse()
print "shoppingList = "
print shoppingList
shoppingList.reverse()
print

# remove
print "shoppingList.remove('Banana')"
shoppingList.remove('Banana')
print "shoppingList="
print shoppingList
print

# loop through list
print """\
for item in shoppingList:
    print item"""
for item in shoppingList:
    print item
