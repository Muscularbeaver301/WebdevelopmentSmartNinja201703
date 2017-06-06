cars = ['Ford', 'Opel', 'Renault']
cars2 = ['Audi', 'RangeRover', 'Kraxn']
print cars
cars.append('Toyota')
print cars
completelist = cars + cars2
print completelist
print completelist[:-1]
print len(completelist)
completelist [-2:]
print completelist
print len(completelist)
completelist = completelist [-2:]
print completelist
print len(completelist)
removed = completelist.pop()
print removed
print completelist