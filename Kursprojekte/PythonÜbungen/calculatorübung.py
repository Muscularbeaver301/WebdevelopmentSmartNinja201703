
try:
    zahl1 = int(raw_input("Hallo, bitte gib eine erste Zahl ein: "))
except:
    print ("Verwende eine Zahl!")
    exit()
try:
    zahl2 = int(raw_input("Bitte gib eine zweite Zahl ein "))
except:
    print ("Verwende eine Zahl!")






Rechnungsart = (raw_input("Bitte gib eine Rechnungsart an(+,-,/,*):"))

if Rechnungsart == "+":
    wert = zahl1 + zahl2
    print zahl1, Rechnungsart, zahl2, "=", wert
elif Rechnungsart == "-":
    wert = zahl1 - zahl2
    print zahl1, Rechnungsart, zahl2, "=", wert
elif Rechnungsart == "/":
    wert = zahl1 / zahl2
    print zahl1, Rechnungsart, zahl2, "=", wert
elif Rechnungsart == "*":
    wert = zahl1 * zahl2
    print zahl1, Rechnungsart, zahl2, "=", wert
else:
    print ("Ich habe ihre Eingabe leider nicht verstanden, verwenden Sie die vorgegebenen Befehle!")