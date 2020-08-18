print("Calculo de Raiz Quadrada")


xa =  int(input("Digite o Valor x1: "))
xb =  int(input("Digite o Segundo valor X2: "))
ya =  int(input("Digite o terceiro Valor y3: "))
yb =  int(input("Digite o quarto valor y4: "))

import math

xa1 = xa - xb

ya1 = ya - yb

valor = xa1 * xa1

valory = ya1 * ya1

valor1 = valor + valory

valor2 = round(math.sqrt(valor1))

print("Raiz Quadrada: ",valor2)
