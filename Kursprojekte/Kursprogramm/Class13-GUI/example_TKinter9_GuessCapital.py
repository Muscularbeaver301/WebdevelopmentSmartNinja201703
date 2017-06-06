import Tkinter
import random
import tkMessageBox

def check_guess():
    """
    This function takes the Entry from the Entrybox, parses it to an int, and compares it with the secret
    Depending on whether guess equals the secret or not, a messagebox is shown with the appropriate message
    :return:
    :rtype: None
    """

    guess_city = guess.get()
    if answer == guess_city:
        result_text = "CORRECT!"
    else:
        result_text = "WRONG! That is not the capital"

    tkMessageBox.showinfo("Result", result_text)


capitals={}
capitals['France'] = 'Paris'
answer = 'Paris'

### TKINTER ELEMENTS ###

window = Tkinter.Tk()

# greeting text
greeting = Tkinter.Label(window, text="What is the capital of France?")
greeting.pack()

# guess entry field
guess = Tkinter.Entry(window)
guess.pack()

# submit button
submit = Tkinter.Button(window, text="Submit", command=check_guess) # without () !!, only show_msg_box
submit.pack()

window.mainloop()
