from tkinter import *
import tkinter as tk
from awesometkinter import *
import awesometkinter as atk
from tkinter import ttk


class Application():
    def __init__(self):
        self.janela_principal = Tk()
        self.imagens()
        self.tela()
        self.frames_da_tela()
        self.labels()
        self.caixas_de_texto()
        self.botoes()
        self.tabela_de_contatos()
        self.janela_principal.mainloop()


    def imagens(self):
        # Importando imagens
        self.lupa = PhotoImage(file="Codificando/imagens/lupa.png")


    def tela(self):
        # Conffigurações da janela
        self.janela_principal.geometry('850x540')
        self.janela_principal.resizable(0, 0)
        self.janela_principal.config(bg='#2F4F4F')
        self.janela_principal.title('Agenda Pessoal de Contatos')
        self.janela_principal.iconbitmap('codificando/imagens/agenda.ico')


    def frames_da_tela(self):
        # Criação dos frames
        self.primeiro_frame = atk.Frame3d(self.janela_principal,
                bg='#2F4F4F')
        self.segundo_frame = atk.Frame3d(self.janela_principal,
                bg='#2F4F4F')

        # Posição dos frames
        self.primeiro_frame.place(x=10, y=60, width=830, height=230)
        self.segundo_frame.place(x=10, y=295, width=830, height=240)


    def labels(self):
        # Titulo da janela na barra de menu
        self.contatos_titulo = Label(self.janela_principal, 
                text='Agenda Telefônica',
                fg='white',
                bg='#2F4F4F',
                font=("Righteous", 20)
                )

        #Configurando a parte principal da tela
        self.nome_label = Label(self.primeiro_frame,
                text='Nome:',
                font=('Trebuchet', 15, 'bold'),
                fg='white',
                bg='#2F4F4F')

        # Titulo da treeview do segundo frame
        self.todos_contatos_label = Label(self.segundo_frame,
                text='Todos os contatos:',
                font=('trebuchet', 15, 'bold'),
                fg='white',
                bg='#2F4F4F')

        # Titulo dos entry que recebe os números de telefones
        self.telefones_label = Label(self.primeiro_frame,
                text='Telefones',
                font=('trebuched', 15, 'bold'),
                fg='white',
                bg='#2F4F4F')
        
        # Chamando todas as labels para a janela
        self.contatos_titulo.place(x=10, y=5)
        self.nome_label.place(x=10, y=20)
        self.telefones_label.place(x=370, y=70)
        self.todos_contatos_label.place(x=10, y=20)


    def caixas_de_texto(self):
        # Função que apaga a mensagem de dita da caixa de texto
        def on_click(event):
            self.caixa_pesquisa.configure(state=NORMAL)
            self.caixa_pesquisa.delete(0, END)

            self.caixa_pesquisa.unbind('<Button-1>', on_click)

        # Caixa de pesquisa da barra de menu
        self.caixa_pesquisa = Entry(self.janela_principal,
                font=('Times', 15),
                fg='gray',
                borderwidth=3,
                relief="raised"
                )
        self.caixa_pesquisa.insert(0, "Buscar...")
        self.caixa_pesquisa.configure(state=DISABLED)
        on_click_id = self.caixa_pesquisa.bind('<Button-1>', on_click)

        # Caixa de texto que recebe o nome
        self.nome_entry = Entry(self.primeiro_frame,
                font=('Times', 15),
                fg='gray',
                borderwidth=2,
                relief='raised')

        # Adicionando as três caixas de texto que receberão os números de telefone
        self.primeiro_numero = Entry(self.primeiro_frame,
                font=('Times', 15),
                fg='gray',
                borderwidth=2,
                relief='raised')
        self.segundo_numero = Entry(self.primeiro_frame,
                font=('Times', 15),
                fg='gray',
                borderwidth=2,
                relief='raised')
        self.terceiro_numero = Entry(self.primeiro_frame,
                font=('Times', 15),
                fg='gray',
                borderwidth=2,
                relief='raised')

        # Chamando as caxas de texto
        self.caixa_pesquisa.place(x=600, y=12)
        self.nome_entry.place(x=80, y=20, width=300)
        self.primeiro_numero.place(x=20, y=110, width=250)
        self.segundo_numero.place(x=290, y=110, width=250)
        self.terceiro_numero.place(x=560, y=110, width=250)


    def botoes(self):
        # Botão da lupa na barra de menu    
        self.pesquisar_button = Button(self.janela_principal,
                image=self.lupa,
                bg='#2F4F4F',
                width=25,
                height=25
                )

        # Botão de adiconar novo contato
        self.adicionar_button = Button(self.primeiro_frame,
                text='Salvar',
                font=('verdana', 10, 'bold'),
                fg='white',
                bg='#5271FF'
                )

        # Botão de editar contato
        self.alterar_button = Button(self.primeiro_frame,
                text='Editar',
                font=('verdana', 10, 'bold'),
                fg='white',
                bg='#5271FF'
                )

        # Botão remover contatos
        self.remover_button = Button(self.segundo_frame,
                text='Remover',
                font=('verdana', 10, 'bold'),
                fg='white',
                bg='#FF5757')
        
        # Chamando os botões na tela
        self.pesquisar_button.place(x=805, y=11)
        self.adicionar_button.place(x=330, y=170)
        self.alterar_button.place(x=440, y=170)
        self.remover_button.place(x=730, y=15)


    def tabela_de_contatos(self):
        # Criando a treeview
        self.tabela = ttk.Treeview(self.segundo_frame,
                height=3,
                columns=('col1', 'col2', 'col3', 'col4'))
        
        # Nomeando a tabela
        self.tabela.heading('#0', text='Nome')
        self.tabela.heading('#1', text='Número 1')
        self.tabela.heading('#2', text='Número 2')
        self.tabela.heading('#3', text='Número 3')
        
        # Especificando a tabela
        self.tabela.column('#0', width=200)
        self.tabela.column('#1', width=205)
        self.tabela.column('#2', width=205)
        self.tabela.column('#3', width=205)

        # Especificando o tamanho no frame
        self.tabela.place(x=10, y=50, width=810, height=180)
        

Application()
