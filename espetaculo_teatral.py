print("Espetaculo pimpas")

v1 = ""

a = input("Digite o Valor do evento: ")
while(a.isdigit() == False or a == v1):
    print("Campo somente numero e não pode ser em branco")
    a = input("Digite o Valor do evento: ")

b = input("Digite o valor por ingresso: ")
while(a.isdigit() == False or b == v1):
    print("Campo somente numero e não pode ser em branco")
    b = input("Digite o valor por ingresso: ")

a1 = float(a)
b1 = float(b)

v = a1 / b1
v1 = (a1 * 0.23) / b1 + v

print("Quantidade de convites vendidos para alcançar o total: ",round(v),
      "\nQuantidade de ingressos para lucro de 23%: ",round(v1))
