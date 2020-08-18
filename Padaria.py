
def padaria():

    print("Programa Padaria")

    v1 = 0.12
    v2 = 1.50

    pao = input("Digite a quantidade de paes: ")
    while pao.isdigit() == False:
        print("Digite apenas numeros")
        pao = input("Digite a quantidade de paes: ")


    broa =  input("Digite a quantidade de Broa: ")
    while broa.isdigit() == False:
        print("Digite apenas numeros")
        broa = input("Digite a quantidade de Broa: ")


    a = float(pao)
    b = float(broa)

    p = a * v1
    b = b * v2
    total = p + b
    inv = total * 0.1

    print("Valor total arrecadado: R${:.2f}".format(total), "\nValor para Investir: R${:.2f}".format(inv))

if (__name__ == "__main__"): #essa variavel permite que o programa seja executado sem precisar ser chamado pela janela (escolha o jogo)
    padaria()