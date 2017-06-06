# initialize
newList = []
print newList
print

# append single elements
newList.append('Banana')
print newList
print

# append add multiple elements with other lists
oldList = ['Milk', 'Honey']
shoppingList = newList + oldList
print shoppingList
print

# refer to elements
print shoppingList[0]
print shoppingList[-1]
print

# refer to multiple elements
print shoppingList[:-1]
print shoppingList[1:]
print

# reverse
shoppingList.reverse()
print shoppingList
shoppingList.reverse()
print

# remove
shoppingList.remove('Banana')
print shoppingList
print

# loop through list
for item in shoppingList:
    print item

# length
print len(shoppingList)
print
