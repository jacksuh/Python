print("Validação")


a =  input("Digite seu nome:")
while a.isalpha() == False:
    a = input("Digite seu nome:")

print(a)


v1 = input("Qual o valor a ser pago: ")
while v1.isdigit() == False:
    v1 = input("Qual o valor a ser pago: ")

print(v1)