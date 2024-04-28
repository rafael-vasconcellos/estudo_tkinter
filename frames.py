from tkinter import *
menu_inicial = Tk() ; menu_inicial.title('Título')


myFrame = Frame(menu_inicial)
message1 = Message(myFrame, text= "nngvn bjdnv fjmkf pkofk pok jfmngv nvj knvjk dnvjk")
t1 = Entry(myFrame)
myFrame2 = Frame(menu_inicial, width=150, height=100, bg='red', padx=5, pady=5)
spinbox1 = Spinbox(myFrame2, values=('a', 'b', 'c', 'd'), wrap=True)

spinbox1.place(x=0, y=0)
message1.grid(row=0, column=0) # label1.grid_forget()
t1.grid(row=1, column=0) ; t1.focus()
# parâmetro sticky= rosa dos ventos
# columnspan= n de colunas a serem ocupadas

myFrame.pack() ; myFrame2.pack()
menu_inicial.mainloop()