#!/usr/bin/env python
# -*- coding: utf-8 -*-
print "Viel Spaß mit FizzBuzz!"
festzahl = raw_input("Gib eine Zahl zwischen 1 und 100 ein: ")


try:
    festzahl = int(festzahl)
    for zahlen in range(1,int(festzahl) +1):
        if zahlen % 3 == 0 and zahlen % 5 == 0:
            print "FizzBuzz"
        elif zahlen % 3 == 0:
            print "Fizz"
        elif zahlen % 5 == 0:
            print "Buzz"
        else:
            print int(zahlen)
except ValueError:
    print "Bitte geben Sie nur Zahlen ein -> " + festzahl + " <- ist keine Zahl!"


