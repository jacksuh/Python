print("Programa para exibir quantidade de notas")

a = input("Digite o valor: ")
while (a.isdigit() == False):
    a = input("Digite o valor: ")

a1 = int(a)

v1 = a1 / 100
v2 = a1 / 50
v3 = a1 / 20
v4 = a1 / 10
v5 = a1 / 5
v6 = a1 / 2
v7 = a1 / 1

print("Quantidade de notas divididas por 100: ",round(v1),
      "\nQuantidade de notas divididas por 50: ",round(v2),
      "\nQuantidade de notas divididas por 20: ",round(v3),
      "\nQuantidade de notas divididas por 10: ",round(v4),
      "\nQuantidade de notas divididas por 5: ",round(v5),
      "\nQuantidade de notas divididas por 2: ",round(v6),
      "\nQuantidade de notas divididas por 1: ",round(v7))
