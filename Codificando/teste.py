from tkinter import *
import tkinter as tk

class Application():
    def __init__(self):
        self.janela_principal = Tk()
        self.tela()
        self.labels()

        self.janela_principal.mainloop()

    def tela(self):
        self.janela_principal.geometry('850x540')
        self.janela_principal.resizable(0, 0)
        self.janela_principal.config(bg='#CDB7B5')
        self.janela_principal.overrideredirect(True)


    def labels(self):
        
        self.icone = PhotoImage(file='Codificando/imagens de teste/agenda.png')
        self.icone_label = Label(self.janela_principal,
                image=self.icone,
                bg='#CDB7B5')
        self.icone_label.place(x=4, y=5)

        self.contatos_titulo = Label(self.janela_principal, 
                text='Agenda Telefônica',
                fg='#000000',
                bg='#CDB7B5',
                font=("Righteous", 20)
                )
        self.contatos_titulo.place(x=60, y=10)

Application()