import Tkinter

### TKINTER ELEMENTS ###

window = Tkinter.Tk()

# greeting text
greeting = Tkinter.Label(window, text="Guess the secret number!")
greeting.pack()

# guess entry field
guess = Tkinter.Entry(window)
guess.pack()

window.mainloop()
