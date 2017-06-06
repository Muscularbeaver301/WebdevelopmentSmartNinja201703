import Tkinter

### TKINTER ELEMENTS ###

window = Tkinter.Tk()

# greeting text
greeting = Tkinter.Label(window, text="Guess the secret number!")
greeting.pack()

window.mainloop()
