import tkinter as tk
from tkinter import *

# Especificações da janela
janela_principal = tk.Tk()
janela_principal.geometry('960x540')
janela_principal.resizable(0, 0)
janela_principal.config(bg='black')
janela_principal.title('Agenda Agora')
janela_principal.iconbitmap('codificando/imagens/agenda.ico')

# Labels
contatos = Label(janela_principal, text='Contatos',
                 fg='white',
                 bg='black',
                 font=("Righteous", 20)
                 )

# Caixa de pesquisa
caixa_pesquisa = Entry(janela_principal, font=('Times', 15),
                       fg='gray',
                       borderwidth=3,
                       relief="raised")
caixa_pesquisa.insert(0, "Buscar...")

# Rodando
contatos.place(x=10,
               y=5
               )
caixa_pesquisa.place(x=150,
                     y=12
                     )
janela_principal.mainloop()
