print("Conta do restaurante")

vld = ""
#Validacao simples com o isdigit para validar campo numero:

v1 = input("Qual o valor a ser pago: ")
while v1.isdigit() == False:
    print("Digite novamente")
    v1 = input("Qual o valor a ser pago: ")

#Validacao do campo com while true:
#while True: # Outra forma de validação

    #try:
        #v2 = float(input("Ira dividir a conta em quantos?: "))
        #break
    #except ValueError:
        #print("Valor invalido")

v2 = input("Ira dividir a conta em quantos?: ")
while v2.isdigit() == False:
    print("Digite novamente")
    v2 = input("Ira dividir a conta em quantos?: ")


vv1 = float(v1)
vv2 = float(v2)

soma = vv1 / vv2
print("Valor dividido: R${:.2f} ".format(soma))

