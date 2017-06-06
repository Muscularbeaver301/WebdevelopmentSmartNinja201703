
#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Libraries
import random

#variablen
secret = int(10 * random.random()) + 1
oldsecret = secret
guess = 0
#Nachfolgend die Bedingung für die whileschleife(Haben wir falsch geraten?)
"""
while guess != secret:
    guess = int(raw_input("Errate die Geheimzahl bis 10:"))
    if guess == secret:
        print "Du hast es!"
        oldsecret = secret
        secret = int(10 * random.random()) + 1
        while secret == oldsecret:
            secret = int(10 * random.random()) + 1
        print("Secret = "+str(secret))
    else:
        print "Leider nicht, sehr ärgerlich! versuche es erneut! " + str(guess)+(" ist falsch")
"""
#zweite Möglichkeit:
"""
def getSecret():
    return int(10 * random.random()) + 1

while guess != secret:
    guess = int(raw_input("Errate die Geheimzahl bis 10:"))
    if guess == secret:
        print "Du hast es!"
        secret = getSecret()
        print("Secret = "+str(secret))
        guess = 0
    else:
        print "Leider nicht, sehr ärgerlich! versuche es erneut! " + str(guess)+(" ist falsch")
"""

#dritte mit mehr funktionen

def getSecret():
    return int(10 * random.random()) + 1

def istFalsch():
    global guess
    global secret
    return guess != secret

def pruefung():
    global guess
    global secret
    guess = int(raw_input("Errate die Geheimzahl bis 10:"))
    if guess == secret:
        print "Du hast es!"
        secret = getSecret()
        print("Secret = " + str(secret))
        guess = 0
    else:
        print "Leider nicht, sehr ärgerlich! versuche es erneut! " + str(guess) + (" ist falsch")

while istFalsch(): pruefung()