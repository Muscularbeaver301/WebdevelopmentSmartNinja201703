z1 = float(raw_input("Gebe bitte die erste Zahl ein: "))
z2 = float(raw_input("Gebe bitte die zweite Zahl ein: "))

operator = raw_input("Waehle einen Operator ( +, -, *, /): ")

if operator == "+": # kommentar
    wert = z1 + z2
    print z1, operator, z2, " = ", wert

elif operator == "-":
    wert = z1 - z2
    print z1, operator, z2, " = ", wert

elif operator == "*":
    wert = z1 * z2
    print z1, operator, z2, " = ", wert

elif operator == "/":
    wert = z1 / z2
    print z1, operator, z2, " = ", wert

else:
    print "Eingabe nicht verstanden. Verzeihung."


