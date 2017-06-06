Curriculum Class13, Python GUI with TKinter
examples are taken from Smartninja Curriculum





Guide for creating GUI:

1)
#### start with:

import Tkinter
window = Tkinter.Tk()

#### this will import the TKInter library and start a window


2)
#### Finish with the mainloop, this should be in the last line

window.mainloop()


3) Adding elements
#### when you add any element, Label, Entry, ...
#### first initialize the element, then pack it.
#### example submit button
greeting = Tkinter.Label(window, text="Guess the secret number!")
greeting.pack()




###
Additionally, check out the pythonchallange website

this one:
http://www.pythonchallenge.com/

not this one:
http://pythonchallenge.org/