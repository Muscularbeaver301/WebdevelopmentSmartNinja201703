#!/usr/bin/env python
# -*- coding: utf-8 -*-



import random


def Nummernwuerfel(Eingabewert):

    Lottozahlenlist = []

    while True:
        if len(Lottozahlenlist) == Eingabewert:
            break
        neuzahl = random.randint(1, 49)


        if neuzahl not in Lottozahlenlist:
            Lottozahlenlist.append(neuzahl)
    return Lottozahlenlist

def main():

    print "Willkommen beim Lottozahlengenerator!"

    Zahlenwahl = raw_input("Wieviele Zahlen möchtest du generieren (bis 49): ")

    try:
        Lottozahlenanzahl = int(Zahlenwahl)
    
        print Nummernwuerfel(Lottozahlenanzahl)

    except ValueError:
        print "Bitte gib eine Zahl(Anzahl der Zahlen)ein!"

    print "Bitteschön."




if __name__ == '__main__':
    main()
