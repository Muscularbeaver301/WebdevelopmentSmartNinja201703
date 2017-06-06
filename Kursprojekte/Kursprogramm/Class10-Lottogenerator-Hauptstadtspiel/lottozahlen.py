"""Lottozahlen"""
import random
def lottozahlengenerator(zahlen):
    Lottozahlenlist = []
    zahlen = min([zahlen,49])
    zahlen = zahlen if zahlen <= 49 else 49
    while len(Lottozahlenlist) < zahlen:
        zahl = random.randint(1, 49)
        if zahl not in Lottozahlenlist:
            Lottozahlenlist.append(zahl)
    return Lottozahlenlist

if __name__ == '__main__':
    print sorted(lottozahlengenerator(-1))

