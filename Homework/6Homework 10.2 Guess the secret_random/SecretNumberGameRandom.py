#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random


def generator():

    secret = random.randint(1, 10)

    while True:
        try:
            guess = int(raw_input("Errate die Geheimzahl bis 10:"))

            if guess == secret:
                print "Du hast es!"
                print("Secret = " + str(secret))
            elif guess >= int(11):
                print "Deine Zahl ist grösser als erlaubt!"
            else:
                print "Leider nicht, sehr ärgerlich! versuche es erneut! " + str(guess) + (" ist falsch")
        except Exception as e:
            print "Bitte versuche es mit Zahlen!"

if __name__ == '__main__':
    generator()