"""
Else executives if the loop runs orderly until the end
Else will not execute if loop stopped after a break
"""

for i in range(5):
    print i
else:
    print "orderly",
print "finished \n"


for i in range(5):
    print i
    if i == 3:
        break
else:
    print "orderly",
print "finished \n"
