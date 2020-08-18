def jogar():
    print("Jogo de Forca")

    palavra = "gato".upper()#manter maisculo
    lista = ["_"for letra in palavra] #Também podemos acrescentar dessa forma para sempre acrescentar "_" junto com a frase.

    #lista = ["_","_","_"]#lista
    #Podemos coloar um for para que sempre que o nome da palavra mudar não precise colocar "_" como na lista anterior.
    #for letra in palavra:
        #lista.append("_")

    erros = 0
    acertou = False
    errou = False

    while (not errou and not acertou):  # Enquanto for falso faça de novo.
        chute = input("Digite uma letra: ")
        chute = chute.strip().upper()
        while chute.isalpha() == False:  # .isalpha valida o campo para aceitar somente letras.
            chute = input("Campo aceita somente letra ")
            chute = chute.strip().upper()

        if (chute in palavra):#se chute existe dentro da palavra
            index = 0
            for letra in palavra:#se letra existe dentro da palavra
                if (chute == letra):
                    lista[index] = letra#posicao na lista para a palavra
                index = index + 1  # contagem e armazenamento de letras digitadas.
            acertou = "_" not in lista  # Quando a lista for preenchida ele da como acertou
            print(lista)#imprimindo lista e palavra digitada
        else:
            print("Voce errou")
            erros = erros + 1  # contabiliza quantidade de tentativas
            errou = erros == 6  # Quantidade de tentativas para o errou ate 6

        if (acertou):  # impressão do acertou.
            print("Voce ganhou")

        else:
            if (errou):
                print("Voce errou")


if(__name__ == "__main__"):
    jogar()

