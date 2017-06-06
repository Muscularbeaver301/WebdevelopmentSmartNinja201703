import random

capitals = {}
capitals['Oesterreich'] = 'Wien'
capitals['Italien'] = 'Rom'
capitals['Schweden'] = 'Stockholm'
capitals['Finnland'] = 'Helsinki'
capitals['Tschechien'] = 'Prag'
capitals['Ungarn'] = 'Budapest'

Punkte = 0

n_fragen = 3

for i in range(n_fragen):
    land = random.choice(capitals.keys())
    antwort = raw_input('Was ist die Hauptstadt von %s ? '%land)
    if antwort.lower() == capitals[land].lower():
        Punkte += 1
    del capitals[land]

print "Du hast %i von %i Punkten erreicht!"%(Punkte, n_fragen)






