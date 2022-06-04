from tkinter import *
from tkinter .ttk import *
from time import strftime

# **FALTA MOSTRAR HORA **
root = Tk()
root.title( "Reloj de JK ")

def time():
    string = strftime(" %H:%M:" )
    label.config( text=string)
    label.after( 1000, time)

label = Label(root, font=("ds-digital", 150), background= "black")
time()

mainloop()