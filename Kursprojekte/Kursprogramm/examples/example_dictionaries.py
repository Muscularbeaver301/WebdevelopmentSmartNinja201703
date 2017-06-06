"""
dictionaries:
key-value-pairs
"""

myDict = {}
print myDict
print

# add element
myDict['name'] = 'Peter'
print myDict
print

# initialize with entry
newDict = {'phone': '066410100200'}
print newDict
print

# update with new
myDict.update(newDict)
print myDict
print

# view values:
print myDict.keys()
print

# view values:
print myDict.values()
print

# view items
print myDict.items()
print

# delete item
del myDict['phone']
print myDict
print

# clear entire dict
myDict.clear()
print myDict
print


# Taskmanager:
# key - value
# taskname : completed
myTasks={}
myTasks['Homework_Week9'] = {'taskname': 'Taskmanager', 'completed': False}

einkaufsliste = ['Banana', 'Milk']
# einkaufsliste[0] -> 'Banana'
# einkaufsliste[1] -> 'Milk'