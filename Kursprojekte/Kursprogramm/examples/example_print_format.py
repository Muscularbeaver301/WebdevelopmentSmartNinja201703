"""
More information on https://pyformat.info/
"""

word1 = "Hallo"
word2 = "No."
number = 1
points = 99999.5555

print
print '"{} {} {}".format(word1, word2, number)'
print "{} {} {}".format(word1, word2, number)
print

print
print '"{2} {1} {0}".format(number, word2, word1)'
print "{2} {1} {0}".format(number, word2, word1)
print

print
print '"{:>10}".format(word1)'
print '"{:>10}"'.format(word1)
print

print
print '"{:10}".format(word1)'
print '"{:10}"'.format(word1)
print

person = {'first': 'Jean-Luc', 'last': 'Picard'}
print
print "'{first} {last}'.format(**person)"
print '{first} {last}'.format(**person)
print

print
print "'{p[first]} {p[last]}'.format(p=person)"
print '{p[first]} {p[last]}'.format(p=person)
print

print
print "'{first} {last}'.format(first='Friedrich', last='Nietzsche')"
print '{first} {last}'.format(first='Friedrich', last='Nietzsche')
print
