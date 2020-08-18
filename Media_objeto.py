
class Media:
    def __init__(self,n1,n2,n3):
        self.__n1 = n1
        self.__n2 = n2
        self.__n3 = n3

    def Calculo(self):
        self.divisao = (self.__n1 + self.__n2 + self.__n3)/3
        print("Media é: ",self.divisao)