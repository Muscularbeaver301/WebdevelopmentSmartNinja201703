#!/usr/bin/env python
# -*- coding: utf-8 -*-
km = 1
meilen = 0.621371


print "Hi, ich helfe ihnen bei der Umrechnung von Kilometer in Meilen!"

while True:
    try:
        km = float(raw_input("Geben Sie die Kilometer als Zahl ein- Bei Dezimalzahlen verwenden sie Punkt: "))
        print km * meilen,("Meilen")

        Erneut = raw_input("Wollen Sie eine weitere Rechnung ausführen? (j/n): ")


        if Erneut == str("j"):
            print "Bitteschön..."
        else:
            print "Tschüss"
            break
    except Exception as e:
        print "Falsche Eingabe"




