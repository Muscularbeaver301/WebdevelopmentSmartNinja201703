import json

with open('capitals.json','r') as f:
    capitals = json.load(f)

print capitals['Saint Martin']
