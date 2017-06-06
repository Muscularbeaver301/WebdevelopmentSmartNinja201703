
def it():
    i = 0
    while True:
        i += 1
        yield i


iterator = it()
for _ in range(5):
    print iterator.next()
