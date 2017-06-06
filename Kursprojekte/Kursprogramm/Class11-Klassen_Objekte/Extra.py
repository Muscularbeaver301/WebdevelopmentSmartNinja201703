import time
import math
"""Test if a number is prime"""

_NUMBER_TO_TEST = 21


limit = int(math.sqrt(_NUMBER_TO_TEST))
if _NUMBER_TO_TEST == 1:
    print "Not Prime"
if _NUMBER_TO_TEST==2 or _NUMBER_TO_TEST==3:
    print "Prime"
else:
    print "Test dividing by..."
    for i in range(2,limit+1):
        print '{0}'.format(i),
        if _NUMBER_TO_TEST%i==0:
            print
            print _NUMBER_TO_TEST, 'Is Not prime'
            break
        elif i==limit:
            print
            print _NUMBER_TO_TEST, 'Is Prime'
        time.sleep(0.01)