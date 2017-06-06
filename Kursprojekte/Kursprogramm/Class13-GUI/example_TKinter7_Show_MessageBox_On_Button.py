import Tkinter
import random
import tkMessageBox

def show_msg_box():
    tkMessageBox.showinfo("Result", "This is a messagebox")
    # there is also showerror, showwarning

def show_warning_box():
    tkMessageBox.showwarning("warning", "This is a warning!")

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
submit = Tkinter.Button(window, text="Submit", command=show_msg_box) # without () !!, only show_msg_box
submit.pack()

warningbutton = Tkinter.Button(window, text="call warning", command=show_warning_box)
warningbutton.pack()


window.mainloop()
