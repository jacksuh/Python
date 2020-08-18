
class Conta:
    def __init__(self, numero,titular,saldo,limite):#Dessa forma os dados podem ser alterados
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do Titular {}".format(self.__saldo,self.__titular))

    def depositar(self,valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):#declarando a variavel  valor_disponivel_a_sacar
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar
    #metodoprivado undestcor na frente do pode_sacar

    def sacar(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    @property
    def saldo(self): #get traz o resultado
        return self.__saldo

    @property
    def limite(self):  # property é igual a get porém no comando voce nao precisa colocar get_limite, fazendo Conta.limite ele retorna.
        return self.__limite

    @limite.setter
    def limite(self,limite):#Set envia o novo limite, acrescenta.
        self.__limite = limite

    @property
    def titular(self):#difença entre property e get.
        return self.__titular


    #def get_titular(self):#difença entre property e get.
        #return self.__titular

    #Existe duas formas dessa forma e colocando o @limite.Setter
    #def set_limite(self,limite):#Set envia o novo limite, acrescenta.
        #self.__limite = limite


