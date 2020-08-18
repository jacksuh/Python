from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["padx"] = 20
        self.quartoContainer.pack()

        self.nuLabel = Label(self.primeiroContainer, text="Digite o primeiro numero", font=self.fontePadrao)
        self.nuLabel.pack(side=LEFT)

        self.nu = Entry(self.primeiroContainer)
        self.nu["width"] = 20
        self.nu["font"] = self.fontePadrao
        self.nu.pack(side=LEFT)

        self.nu2Label = Label(self.segundoContainer, text="Digite o Segundo numero", font=self.fontePadrao)
        self.nu2Label.pack(side=LEFT)

        self.nu2 = Entry(self.segundoContainer)
        self.nu2 ["width"] = 20
        self.nu2 ["font"] = self.fontePadrao
        self.nu2["font"] = "*"
        self.nu2.pack(side=LEFT)

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Calculo"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 20
        self.autenticar["command"] = self.calculo
        self.autenticar.pack()

        self.mensagem = Label(self.terceiroContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()#ira imprimir ao lado da label segundo numero.

    def calculo(self):

        a = self.nu.get()
        b = self.nu2.get()

        a1 = int (a)
        b1 = int (b)

        soma = a1 + b1

        self.mensagem["text"] = (soma)


root = Tk()
Application(root)
root.mainloop()