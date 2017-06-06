# coding=utf-8

if __name__ == '__main__':

    tagesmenus = []

    while True:
        answer = raw_input("\nWas möchtest du machen?\n"
                           "(1) Alle Gerichte anzeigen\n"
                           "(2) Set (Vorspeise, Hauptspeise, Nachspeise) hinzufügen\n"
                           "(3) Schreibe Menu in ein File\n"
                           "(4) Set löschen\n"
                           "(5) Menu File lesen\n"
                           "(q) Programm verlassen\n")

        if answer.lower() == "q":
            break

        elif answer == "1":
            print "\nGerichte werden angezeigt"

            print "*" * 30
            for menu_dict in tagesmenus:
                for speise, info in menu_dict.iteritems():
                    print speise, info
            print "*" * 301


        elif answer == "2":
            print "\nSet hinzufügen"
            print "*"*30
            menuset = dict()
            speisentypen = ("Vorspeise", "Hauptspeise", "Nachspeise")
            for speise in speisentypen:
                name = raw_input("Was ist der Name der {}?\n".format(speise))
                preis = raw_input("Was ist der Preis der {}?\n".format(speise))
                menuset[speise] = (name, preis)
            tagesmenus.append(menuset)
        elif answer == "3":
            # todo: implement
            print "In File schreiben"
            content = "Speisentyp,Name,Preis\n"
            for menu_dict in tagesmenus:
                for speise, info in menu_dict.iteritems():
                    content += "{},{},{}\n".format(speise,info[0],info[1])
            with open("menukarte.txt","w") as f:
                f.write(content)

        elif answer == "4":
            # todo: implement
            print "Set löschen"

        elif answer == "5":
            print "File lesen"
            with open("menukarte.txt","r") as f:
                lines = f.readlines()
            new_dict = dict()
            for line in lines[1:]:
                line = line.strip("\n")
                speisentyp2, name2 ,preis2 = line.split(",")
                new_dict[speisentyp2] = (name2,preis2)
            tagesmenus.append(new_dict)
        else:
            print "Unknown Input..."

    print "Exit Restaurant Program..."