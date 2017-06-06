"""Lottozahlen"""
import random

Kuehlschrank = ["Banane","Brot","Milch","Honig","Salat"]

def zufalls_essen():
    auswahl = []
    for x in range(2):
        essen = random.choice(Kuehlschrank)
        Kuehlschrank.remove(essen)
        auswahl.append(essen)
    return auswahl

if __name__ == '__main__':
    essen_heute = zufalls_essen()
    print essen_heute