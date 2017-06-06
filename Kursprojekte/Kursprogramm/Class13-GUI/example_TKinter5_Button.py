import Tkinter
import random

secret = random.randint(1, 100)

### TKINTER ELEMENTS ###

window = Tkinter.Tk()

# greeting text
greeting = Tkinter.Label(window, text="Guess the secret number!")
greeting.pack()

# guess entry field
guess = Tkinter.Entry(window)
guess.pack()

# submit button
submit = Tkinter.Button(window, text="Submit") # add a button, but this button is doing nothing
submit.pack()

window.mainloop()
