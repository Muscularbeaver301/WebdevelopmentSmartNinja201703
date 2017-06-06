import random

N = 10
lowerBound = 0
upperBound = 9

print "%i Random Numbers in the range %i - %i " % (N, lowerBound, upperBound)
for _ in range(N):
    print random.randint(lowerBound, upperBound)
