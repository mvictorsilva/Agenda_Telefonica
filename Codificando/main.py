from tkinter import *
import tkinter as tk


class Application():
    def __init__(self):
        self.janela_principal = Tk()
        self.imagens()
        self.tela()
        self.labels()
        self.botoes()
        self.janela_principal.mainloop()


    def imagens(self):
        self.lupa = PhotoImage(file="Codificando/imagens/lupa.png")


    def tela(self):
        self.janela_principal.geometry('850x540')
        self.janela_principal.resizable(0, 0)
        self.janela_principal.config(bg='#2F4F4F')
        self.janela_principal.title('Agenda Pessoal de Contatos')
        self.janela_principal.iconbitmap('codificando/imagens/agenda.ico')


    def labels(self):
        def on_click(event):
            self.caixa_pesquisa.configure(state=NORMAL)
            self.caixa_pesquisa.delete(0, END)

            self.caixa_pesquisa.unbind('<Button-1>', on_click)
        
        self.contatos_titulo = Label(self.janela_principal, 
            text='Agenda Telefônica',
            fg='white',
            bg='#2F4F4F',
            font=("Righteous", 20)
            )

        self.caixa_pesquisa = Entry(self.janela_principal,
                font=('Times', 15),
                fg='gray',
                borderwidth=3,
                relief="raised"
                )
        self.caixa_pesquisa.insert(0, "Buscar...")
        self.caixa_pesquisa.configure(state=DISABLED)
        
        on_click_id = self.caixa_pesquisa.bind('<Button-1>', on_click)
        
        self.contatos_titulo.place(x=10,
                                   y=5)
        self.caixa_pesquisa.place(x=600,
                                  y=12)


    def botoes(self):               
        self.pesquisar_button = Button(self.janela_principal,
                image=self.lupa,
                bg='#2F4F4F',
                width=25,
                height=25
                )
        self.contato_button = Button(self.janela_principal,
                text='Adicionar',
                font=('verdana', 10, 'bold'),
                fg='white',
                bg='#2F4F4F'
                )
        self.alterar_button = Button(self.janela_principal,
                text='Alterar',
                font=('verdana', 10, 'bold'),
                fg='white',
                bg='#3F4F4F'
                )
        
        self.pesquisar_button.place(x=806,
                                    y=11)
#        self.contato_button.place(x=200,
#                                  y=60)
#        self.alterar_button.place(x=200,
#                                  y=70)


Application()
