from tkinter import *
import tkinter as tk
from awesometkinter import *
import awesometkinter as atk
from tkinter import ttk
import sqlite3

class funcoes():
    # Função que limpa as caixas de entrada
    def limpar_caixa(self):
        self.caixa_pesquisa.delete(0, END)

        self.codigo_entry.delete(0, END)

        self.nome_entry.delete(0, END)

        self.primeiro_numero.delete(0, END)

        self.segundo_numero.delete(0, END)

        self.terceiro_numero.delete(0, END)

    # Função que cria e conecta ao banco de dados no computador
    def conectar_ao_bd(self):
            self.conectar = sqlite3.connect('cliente.db')
            self.cursor = self.conectar.cursor()
            print('Conectando ao banco de dados')

    # Função que desconecta o banco de dados depois que cada processo acaba
    def desconectar_ao_bd(self):
            self.conectar.close()
            print('Desconectando ao banco de dados')

    # Criando a tabela de dados no banco de dados
    def criar_tabela(self):
            self.conectar_ao_bd()

            # Essa função so cria uma tabela se ela não existir
            self.cursor.execute("""
                create table if not exists contato (
                        id integer not null primary key,
                        Nome_contato varchar(50) not null,
                        telefone_um int(13) not null,
                        telefone_dois int(13),
                        telefone_tres int(13)
                );
            """)
            self.conectar.commit()
            print('Banco de dados criado')
            self.desconectar_ao_bd()

    # Criando as variaveis que receberão os dados das caixas de texto (entry)
    def variaveis(self):
            self.codigo_id = self.codigo_entry.get()
            self.inserir_nome_ctt = self.nome_entry.get()
            self.inserir_num_um = self.primeiro_numero.get()
            self.inserir_num_dois = self.segundo_numero.get()
            self.inserir_num_tres = self.terceiro_numero.get()

    # Função que cria inseri os dados recebidos das variaveis pelo usuário
    def adicionar_cliente(self):
            self.variaveis()
            self.conectar_ao_bd()

            self.cursor.execute("""
                insert into contato (Nome_contato, telefone_um, telefone_dois, telefone_tres)
                values (?, ?, ?, ?)
                """,
                (
                self.inserir_nome_ctt,
                self.inserir_num_um,
                self.inserir_num_dois,
                self.inserir_num_tres)
                )

            self.conectar.commit()
            self.desconectar_ao_bd()
            self.mostrar_na_tabela()
            self.limpar_caixa()

    # Função que pega os dados no banco de dados e mostra na tabela
    def mostrar_na_tabela(self):
            # Delete os dados da tabela antes para não trazer informação repetida
            self.tabela.delete(*self.tabela.get_children())
            self.conectar_ao_bd()

            # Seleciona os dados no banco
            dados = self.cursor.execute("""
                select id, Nome_contato, telefone_um, telefone_dois, telefone_tres from contato
                order by Nome_contato asc; 
                """)

            # Inseri os daados na tabela
            for i in dados:
                    self.tabela.insert("", END, values=i)

            self.desconectar_ao_bd()

    # 'event' siginifica que ele vai imteragir com outro código no caso da tabela
    def selecionar(self, event):
            self.limpar_caixa()
            self.tabela.selection()

            for t in self.tabela.selection():
                    col1, col2, col3, col4, col5 = self.tabela.item(t, 'values')
                    self.codigo_entry.insert(END, col1)
                    self.nome_entry.insert(END, col2)
                    self.primeiro_numero.insert(END, col3)
                    self.segundo_numero.insert(END, col4)
                    self.terceiro_numero.insert(END, col4)

    # Função que deleta um contato da tabela
    def deletar(self):
        self.variaveis()
        self.conectar_ao_bd()

        self.cursor.execute("""
        delete from contato where id = ?
        """,
        (self.codigo_id))

        self.conectar.commit()
        self.desconectar_ao_bd()
        self.limpar_caixa()
        self.mostrar_na_tabela()

class Application(funcoes):
    def __init__(self):
        self.janela_principal = Tk()
        self.imagens()
        self.tela()
        self.frames_da_tela()
        self.labels()
        self.caixas_de_texto()
        self.botoes()
        self.tabela_de_contatos()
        self.criar_tabela()
        self.mostrar_na_tabela()
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
                fg='#FFFFFF',
                bg='#2F4F4F',
                font=("Righteous", 20)
                )

        #Configurando a parte principal da tela
        self.nome_label = Label(self.primeiro_frame,
                text='Nome:',
                font=('Trebuchet', 15, 'bold'),
                fg='#FFFFFF',
                bg='#2F4F4F')

        self.codigo_label = Label(self.primeiro_frame,
                text='Indentificador:',
                font=('Trebuchet', 15, 'bold'),
                fg='#FFFFFF',
                bg='#2F4F4F')

        # Titulo da treeview do segundo frame
        self.todos_contatos_label = Label(self.segundo_frame,
                text='Todos os contatos:',
                font=('Trebuchet', 15, 'bold'),
                fg='#FFFFFF',
                bg='#2F4F4F')

        # Titulos dos entry que recebe os números de telefones
        self.celular_label = Label(self.primeiro_frame,
                text='Celular:',
                font=('Trebuchet', 15, 'bold'),
                fg='#FFFFFF',
                bg='#2F4F4F')

        self.telefone_um_label = Label(self.primeiro_frame,
                text='Telefone:',
                font=('Trebuchet', 15, 'bold'),
                fg='#FFFFFF',
                bg='#2F4F4F')

        self.telefone_dois_label = Label(self.primeiro_frame,
                text='Telefone 2:',
                font=('Trebuchet', 15, 'bold'),
                fg='#FFFFFF',
                bg='#2F4F4F')
        
        # Chamando todas as labels para a janela
        self.contatos_titulo.place(x=10, y=5)
        self.nome_label.place(x=10, y=20)
        self.codigo_label.place(x=450, y=20)
        self.celular_label.place(x=20, y=80)
        self.telefone_um_label.place(x=290, y=80)
        self.telefone_dois_label.place(x=560, y=80)
        self.todos_contatos_label.place(x=10, y=20)


    def caixas_de_texto(self):

        # Caixa de pesquisa da barra de menu
        self.caixa_pesquisa = Entry(self.janela_principal,
                font=('Times', 15),
                fg='#000000',
                borderwidth=2,
                relief="raised"
                )

        # Caixa de texto que recebe o nome
        self.nome_entry = Entry(self.primeiro_frame,
                font=('Times', 15),
                fg='#000000',
                borderwidth=2,
                relief='raised')

        # Caixa que monstra o código do contato
        self.codigo_entry = Entry(self.primeiro_frame,
                font=('Times', 15),
                fg='#000000',
                borderwidth=2,
                relief="raised"
                )

        # Adicionando as três caixas de texto que receberão os números de telefone

        ### RECEBE O PRIMEIRO NUMERO ###
        self.primeiro_numero = Entry(self.primeiro_frame,
                font=('Times', 15),
                fg='#000000',
                borderwidth=2,
                relief='raised')

        ### RECEBE O SEGUNDO NUMERO ###
        self.segundo_numero = Entry(self.primeiro_frame,
                font=('Times', 15),
                fg='#000000',
                borderwidth=2,
                relief='raised')

        ### RECEBE O TERCEIRO NUMERO ###
        self.terceiro_numero = Entry(self.primeiro_frame,
                font=('Times', 15),
                fg='#000000',
                borderwidth=2,
                relief='raised')

        # Chamando as caxas de texto
        self.caixa_pesquisa.place(x=600, y=12)
        self.nome_entry.place(x=80, y=20, width=300)        
        self.codigo_entry.place(x=600, y=20, width=100)
        self.primeiro_numero.place(x=20, y=110, width=250)
        self.segundo_numero.place(x=290, y=110, width=250)
        self.terceiro_numero.place(x=560, y=110, width=250)


    def botoes(self):
        # Botão da lupa na barra de menu    
        self.pesquisar_button = Button(self.janela_principal,
                image=self.lupa,
                bg='#2F4F4F',
                width=25,
                height=25)

        # Botão de adiconar novo contato
        self.salvar_button = Button(self.primeiro_frame,
                command=self.adicionar_cliente,
                text='Salvar',
                font=('verdana', 10, 'bold'),
                fg='#FFFFFF',
                bg='#5271FF')

        # Botão de editar contato
        self.editar_button = Button(self.primeiro_frame,
                text='Editar',
                font=('verdana', 10, 'bold'),
                fg='#FFFFFF',
                bg='#5271FF')

        # Botão remover contatos
        self.remover_button = Button(self.segundo_frame,
                command=self.deletar,
                text='Remover',
                font=('verdana', 10, 'bold'),
                fg='#FFFFFF',
                bg='#FF5757')

        # Botão para sair da janela
        self.sair_button = Button(self.primeiro_frame,
                command=quit,
                text='Sair',
                font=('verdana', 10, 'bold'),
                fg='#FFFFFF',
                bg='#FF5757')

        # Botão para limpar as caixas de texto
        self.limpar_button = Button(self.primeiro_frame,
                command=self.limpar_caixa,
                text='Limpar',
                font=('verdana', 10, 'bold'),
                fg='#FFFFFF',
                bg='#FF5757')
        
        # Chamando os botões na tela
        self.pesquisar_button.place(x=805, y=11)
        self.salvar_button.place(x=330, y=170)
        self.editar_button.place(x=440, y=170)
        self.remover_button.place(x=735, y=15)
        self.sair_button.place(x=770, y=190)
        self.limpar_button.place(x=750, y=20)


    def tabela_de_contatos(self):
        # Criando a treeview
        self.tabela = ttk.Treeview(self.segundo_frame,
                height=3,
                columns=('col1', 'col2', 'col3', 'col4', 'col5'))
        
        # Nomeando a tabela
        self.tabela.heading('#0', text='')
        self.tabela.heading('#1', text='ID')
        self.tabela.heading('#2', text='Nome')
        self.tabela.heading('#3', text='Número 1')
        self.tabela.heading('#4', text='Número 2')
        self.tabela.heading('#5', text='Número 3')
        
        # Especificando a tabela
        self.tabela.column('#0', width=1)
        self.tabela.column('#1', width=70, minwidth=70)
        self.tabela.column('#2', width=180, minwidth=180)
        self.tabela.column('#3', width=180, minwidth=180)
        self.tabela.column('#4', width=180, minwidth=180)
        self.tabela.column('#5', width=180, minwidth=180)

        # Criando a função que selecionar a coluna na tabela ('.bind' é a que faz interação com a tabela)
        self.tabela.bind("<Double-1>", self.selecionar)

        # Especificando o tamanho no frame
        self.tabela.place(x=15, y=50, width=800, height=180)

Application()
