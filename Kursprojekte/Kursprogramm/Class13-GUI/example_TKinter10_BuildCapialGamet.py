import Tkinter
import tkMessageBox
import random


capitals = {}
capitals['Oesterreich'] = 'Wien'
capitals['Deutschland'] = 'Berlin'
capitals['Ungarn'] = 'Budapest'


def check_entry():
    entry = entryfield.get()
    tkMessageBox.showinfo("InfoBox","Pressed Submit Button, entered %s, the capital is: %s" % (entry,capitals[currentCountry]) )


all_country = capitals.keys()
currentCountry = random.choice(all_country)


window = Tkinter.Tk()

labelfield = Tkinter.Label(window, text="This is the capitals game. What is the capital of %s" % currentCountry)
labelfield.pack()

entryfield = Tkinter.Entry(window)
entryfield.pack()

button = Tkinter.Button(window, text="Submit Answer", command=check_entry)
button.pack()

window.mainloop()