import tkinter as tk
from tkinter import *

# Especificações da janela
janela_principal = tk.Tk()
janela_principal.geometry('960x540')
janela_principal.resizable(0, 0)
janela_principal.config(bg='black')
janela_principal.title('Agenda Agora')
janela_principal.iconbitmap('codificando/imagens/agenda.ico')

# Importando imagens e apagando o fundo
contato = PhotoImage(file="Codificando/imagens/adicionar_usuario.png")


# Labels
contatos_titulo = Label(janela_principal, text='Contatos',
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

# Botões
contato_button = Button(janela_principal,
                        image=contato,
                        bg='black',
                        width=25,
                        height=25
                        )

# Rodando
contatos_titulo.place(x=10,
                      y=5
                      )
caixa_pesquisa.place(x=600,
                     y=12
                     )
contato_button.place(x=900,
                     y=5
                     )
janela_principal.mainloop()
