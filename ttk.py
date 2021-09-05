from tkinter import ttk
from tkinter import*

def blue(event):
    print('blue')
    c['bg']='blue'

def red(event):
    print('red')
    c['bg']='red'

def yellow(event):
    print('yellow')
    c['bg']='yellow'


def colors(event):
    if comboExample.get()=='Blue':
        blue(event)
    if comboExample.get()=='Red':
        red(event)
    if comboExample.get() == 'Yellow':
        yellow(event)





root = Tk()
c=Canvas()
c.pack()


b=Button


comboExample = ttk.Combobox(root,
                            values=[
                                    "Red",
                                    "Blue",
                                    "Yellow"])




comboExample.current(0)



comboExample.pack()



print(comboExample.current(1), comboExample.get())


comboExample.bind('<<ComboboxSelected>>',colors)

root.mainloop()