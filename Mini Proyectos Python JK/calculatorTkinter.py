from tkinter import *
from sys import *

root=Tk()
root.title('Juank Calculator')

#**    FALTA ARREGLARLO    **

e=Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current)+str(number))
    
def button_clear():
    e.delete(0, END)
    
def button_add():
    first_number=e.get()
    global f_num
    global  math
    math= "addition"
    f_num=int(first_number)
    e.delete(0, END)
    
def button_sub():
    first_number=e.get()
    global f_num
    global math
    math="substraction"
    f_num=int(first_number)
    e.delete(0, END)
    
def button_mul():
    first_number=e.get()
    global f_num
    global math
    nath="multiply"
    f_num=int(first_number)
    e.delete(0, END)
    

def button_div():
    first_number=e.get()
    global f_num
    global math
    math="divide"
    f_num=int(first_number)
    e.delete(0, END)
    
def button_exit():
    exit()
    
def button_equal():
    f_number =e.get()
    second_number=e.get()
    global f_num
    global math
    #e.delete(0, END)
    if math=="addition":
        e.insert(0, f_number + int(second_number))
    if math=="substraction":
        e.insert(0, f_number - int(second_number))
    if math=="multiply":
        e.insert(0,  f_number * int(second_number))
    if math=="divide":
        e.insert(0, f_number/ int(second_number))
        
#create buttons
button_1 = Button(root, text="1", padx=50, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=50, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=50, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=50, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=50, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=50, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=50, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=50, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=50, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=50, pady=20, command=lambda: button_click(0))
button_add= Button(root, text="+", padx=50, pady=20, command=button_add)
button_sub= Button(root, text="-", padx=50, pady=20, command=button_sub)
button_mul= Button(root, text="*", padx=51, pady=20, command=button_mul)
button_div= Button(root, text="/", padx=51, pady=20, command=button_div)
button_equal= Button(root, text="=", padx= 122, pady=20, command=button_equal)
button_clear= Button(root, text="Clear", padx=120, pady=20, command=button_clear)
button_exit= Button(root, text="Exit", padx=50, pady=20, command=button_exit)

#place buttons on screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_sub.grid(row=6, column=0)
button_mul.grid(row=6, column=1)
button_div.grid(row=6, column=2)

button_exit.grid(row=7, column=0)

#event loop
root.mainloop()