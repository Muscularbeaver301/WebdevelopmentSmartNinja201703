import json
import random

capitals = {}

with open('capitals.json','r') as f:
    capitals = json.load(f)

n_questions = 10
points = 0

for i in range(n_questions):
    country = random.choice(capitals.keys())
    answer = raw_input("What is the capital of %s ? "%country)
    if answer.strip().lower() == capitals[country].lower():
        points += 1
        print 'Correct'
    else:
        print 'Sorry, Capital of %s: %s'%(country,capitals[country])
        
    del capitals[country]

print 'You got %i of %i Points!'%(points,n_questions)

