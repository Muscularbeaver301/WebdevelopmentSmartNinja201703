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

    guess_number = int(guess.get())
    if guess_number == secret:
        result_text = "CORRECT!"
    elif guess_number > secret:
        result_text = "WRONG! Your guess is too high."
    else:
        result_text = "WRONG! Your guess is too low."

    tkMessageBox.showinfo("Result", result_text)


secret = random.randint(1, 100)
z
### TKINTER ELEMENTS ###

window = Tkinter.Tk()

# greeting text
greeting = Tkinter.Label(window, text="Guess the secret number!")
greeting.pack()

# guess entry field
guess = Tkinter.Entry(window)
guess.pack()

# submit button
submit = Tkinter.Button(window, text="Submit", command=check_guess) # without () !!, only show_msg_box
submit.pack()

window.mainloop()
