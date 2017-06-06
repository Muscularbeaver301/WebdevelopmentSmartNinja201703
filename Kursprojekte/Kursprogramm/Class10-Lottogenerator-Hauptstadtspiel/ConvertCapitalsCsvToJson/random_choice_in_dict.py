import json
import random

capitals = {}

with open('capitals.json','r') as f:
    capitals = json.load(f)

country = random.choice(capitals.keys())

print 'Capital of %s: %s'%(country,capitals[country])
