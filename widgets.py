from tkinter import *

menu_inicial = Tk()
menu_inicial.title('Título')
menu_inicial.geometry('500x250+200+200')
menu_inicial.state('zoomed') # iconic
nova_janela = Toplevel()
#menu_inicial.minsize(height=250, width=250)
#menu_inicial.iconbitmap()
#menu_inicial.winfo_width()

Button(menu_inicial, text='Botão').pack()
Checkbutton(menu_inicial, text='Label do input', variable=None).pack()
Spinbox(menu_inicial, from_=0, to=10).pack()
slide = Scale(menu_inicial, from_=0, to=100, orient=HORIZONTAL, resolution=0.5)
slide.pack() ; slide.get()
label1 = Label(menu_inicial, text='Label')
label1['text'] = 'Novo label'
label1.pack() # label1.pack_forget(), label1.destroy()

# command= Função
# fg: cor do texto
# bg: cor de fundo 
# width: em pxs, height: em linhas
# font= 'Arial 20 bold'
# bd= n, relief='solid'
# anchor: Rosa dos ventos: variáveis WENS ou strings 'wens'
# padx: padding
# justify
# image= PhotoImage(file= 'caminho relativo')

menu_inicial.mainloop()