print("Programa para encontrar o numero menor")

tentativas = ""

n1 = input("Digite o primeiro numero: ")
while(n1 == tentativas):
    n1 = input("Digite o primeiro numero: ")

n2 = input("Digite o segundo numero: ")
while(n2 == tentativas):
    n2 = input("Digite o segundo numero: ")

n3 = input("Digite o terceiro numero: ")
while(n3 == tentativas):
    n3 = input("Digite o terceiro numero: ")

nu_1 = int(n1)
nu_2 = int(n2)
nu_3 = int(n3)

if(nu_1 < nu_2 and nu_1 < nu_3):
    print("Numero n1 é o menor",nu_1)

elif(nu_2 < nu_1 and nu_2 < nu_3):
    print("Numero n2 é menor",nu_2)

elif(nu_3 < nu_1 and nu_3 < nu_2 ):
    print("Numero n3 é menor",nu_3)

