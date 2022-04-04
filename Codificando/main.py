from tkinter import *
import tkinter as tk


class Application():
    def __init__(self):
        self.janela_principal = Tk()
        self.tela()
        self.funcionais()
        self.janela_principal.mainloop()


    def tela(self):
        self.janela_principal.geometry('850x540')
        self.janela_principal.resizable(0, 0)
        self.janela_principal.config(bg='black')
        self.janela_principal.title('Agenda Agora')
        self.janela_principal.iconbitmap('codificando/imagens/agenda.ico')

    def funcionais(self):
        ###### Importando imagens e apagando o fundo ######
        self.contato = PhotoImage(file="Codificando/imagens/adicionar_usuario.png")
        self.lupa = PhotoImage(file="Codificando/imagens/pesquisa.png")

        ###### Labels ######
        self.contatos_titulo = Label(self.janela_principal, 
                text='Agenda Pessoal de Contatos',
                fg='white',
                bg='black',
                font=("Righteous", 20)
                )

        ###### Caixa de pesquisa ######
        self.caixa_pesquisa = Entry(self.janela_principal,
                font=('Times', 15),
                fg='gray',
                borderwidth=3,
                relief="raised"
                )
        self.caixa_pesquisa.insert(0, "Buscar...")
        self.caixa_pesquisa.configure(state=DISABLED)

        def on_click(event):
            self.caixa_pesquisa.configure(state=NORMAL)
            self.caixa_pesquisa.delete(0, END)

            self.caixa_pesquisa.unbind('<Button-1>', on_click)
        
        on_click_id = self.caixa_pesquisa.bind('<Button-1>', on_click)

        ###### Botões ######
        self.contato_button = Button(self.janela_principal,
                text='Adicionar',
                image=self.contato,
                bg='black',
                height=25
                )               
        self.pesquisar_button = Button(self.janela_principal,
                image=self.lupa,
                bg='black',
                width=25,
                height=25
                )

        ###### Rodando ######
        self.contatos_titulo.place(x=10,
                                   y=5
                                   )
        self.caixa_pesquisa.place(x=600,
                                  y=12
                                  )
        self.pesquisar_button.place(x=806,
                                    y=11
                                    )
        self.contato_button.place(x=200,
                                  y=60
                                  )


Application()
