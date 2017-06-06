"""
More information on https://pyformat.info/
"""

word1 = "Hallo"
word2 = "No."
number = 1
points = 99999.5555

print
print '"%s %s %i "%(word1, word2, number)'
print "%s %s %i " % (word1, word2, number)
print

print
print '"%s %s %i %0.2f"%(word1, word2, number, points)'
print "%s %s %i %0.2f" % (word1, word2, number, points)
print

print
print '"%10s"%(word1,)'
print "'%10s'" % (word1,)
print

print
print '"%-10s" % (word1,)'
print "'%-10s'" % (word1,)
print

person = {'first': 'Jean-Luc', 'last': 'Picard'}
print
print "'%(first)s %(last)s' % person"
print '%(first)s %(last)s' % person
print
