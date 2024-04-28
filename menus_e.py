from tkinter import *

menu_inicial = Tk()
menu_inicial.geometry('500x250+200+200')
menu_inicial.title('Título')

meuMenu = Menu(menu_inicial)
fileMenu = Menu(meuMenu, tearoff=0)
fileMenu.add_command(label= 'New')
fileMenu.add_command(label= 'Open')
fileMenu.add_command(label= 'Save')
fileMenu.add_separator()
fileMenu.add_command(label= 'Close')
meuMenu.add_cascade(menu= fileMenu, label='File')
menu_inicial.config(menu= meuMenu)


menu_inicial.mainloop()
