# coding: utf8

import collections
import pprint

if __name__ == '__main__':

    print ('Hallo, willkommen im Tagesmenü-Editor!\n\n')

    print ("Bitte wähle eine Option aus:\n")

    Tageskarte = {}
    while True:
        answer = raw_input("(1) Tageskarte (Vorspeise, Hauptspeise, Nachspeise) hinzufügen\n"
                           "(2) Tageskarte anzeigen\n"
                           "(3) Tageskarte in eine Textdatei ausgeben\n"
                           "(4) Tageskarte löschen\n"
                           "(q) Editor verlassen\n")

        if answer.lower() == "q":
            break

        elif answer == "1":
            print "\nTageskarte hinzufügen"
            print "*" * 30

            gericht1 = raw_input("\nVorspeise: ")
            preis1 = raw_input("Preis: ")
            gericht2 = raw_input("Hauptspeise: ")
            preis2 = raw_input("Preis: ")
            gericht3 = raw_input("Nachspeise: ")
            preis3 = raw_input("Preis: ")

            speisen = collections.defaultdict(list)
            speisen["Vorspeise"].extend([gericht1, preis1])
            speisen["Hauptspeise"].extend([gericht2, preis2])
            speisen["Nachspeise"].extend([gericht3, preis3])

            Tageskarte.update(speisen)

        elif answer == "2":
            print "*" * 30
            print "\nTageskarte wird angezeigt"
            print "*" * 30
            for k,v in Tageskarte.iteritems(): #sorted print machen
                print k,v
            print "*" * 30

        elif answer == "3":
            print "*" * 37
            print "Tageskarte in eine Textdatei ausgeben"
            print "*" * 37

            with open("Tageskarte.txt","w") as tageskarte:
                tageskarte.write('Heutiges Menü:\n' + pprint.pformat(Tageskarte) + '\n')

            print "*" * 25
            print "Textdatei wurde erstellt!"
            print "*" * 25

        elif answer == "4":
            Tageskarte.clear();
            print "*" * 27
            print "Tageskarte wurde gelöscht!"
            print "*" * 27

        elif answer == "q":
            if answer.lower() == "q":
                break

        else:
            print "Ungültige Eingabe"