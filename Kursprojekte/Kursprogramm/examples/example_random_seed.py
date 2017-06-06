import random

N = 10
lowerBound = 0
upperBound = 9
seed = 9999

print "%i Random Numbers in the range %i - %i with seed %i" % (N, lowerBound, upperBound, seed)

# we use seed, to be able to rerun and check outcomes of random experiments
random.seed(seed)

for _ in xrange(N):
    print random.randint(lowerBound, upperBound)
