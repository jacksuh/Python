import random

def jogar():#para declarar uma funcao utilizamos o def:

    print("*******************")
    print("Jogo de Adivinhação")
    print("*******************")



    numero = random.randrange(1,101) #ira gerar numeros aleatorios de 1 a 100
    total_de_tentativas = 0
    pontos = 1000

    #Definir o nivel de dificuldade do jogo.
    print("Qual o Nivel de Difículdade: ",numero)
    print("(1) Facil (2) Médio (3) Dificil")

    nivel = int(input("Defina o Nivel: "))

    if(nivel == 1 ):
        total_de_tentativas = 20

    elif(nivel == 2 ):
        total_de_tentativas = 10

    else:
        total_de_tentativas = 5

    for rodada in range (1,total_de_tentativas + 1): #acrescentar o +1 para ir ate a terceira tentativa
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = int( input("Digite um numero: "))
        print("Você Digitou: ",chute)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        Acertou = numero == chute
        Acima   = chute > numero
        Abaixo  = chute < numero

        if(Acertou):
            print("Você acertou e fez {} pontos".format(pontos))
            break #caso o usuario acerte ira sair do laço
        else:
            if(Acima):
                print("O seu numero esta acima do correto")
            elif(Abaixo):
                print("O seu numero esta abaixo do correto")
            pontos_perdidos = abs(numero - chute)  #pontos perdidos da rodada
            pontos = round(pontos - pontos_perdidos) #subtraindo os pontos perdidos da pontuação total
        print("Fim do Jogo")

if (__name__ == "__main__"): #essa variavel permite que o programa seja executado sem precisar ser chamado pela janela (escolha o jogo)
    jogar()