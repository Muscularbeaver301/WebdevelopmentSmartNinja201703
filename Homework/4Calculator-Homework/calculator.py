#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Diese Lösung zur Verwendung von
Umlauten in Python
steht auf: http://stackoverflow.com/questions/728891/correct-way-to-define-python-source-code-encoding
"""



a = int(raw_input("Nennen Sie einen Wert für a: "))
print a

b = int(raw_input("Nennen Sie einen Wert für b: "))
print b

Rechenart = raw_input("Welche Rechenart wünschen Sie? (+, -, *, /:")

print Rechenart

if Rechenart == "+":
    print a + b
elif Rechenart == "-":
    print a - b
elif Rechenart == "*":
    print a * b
elif Rechenart == "/":
    print a / b
else:
    print "Sie haben keine gültige Rechenart angegeben!"
