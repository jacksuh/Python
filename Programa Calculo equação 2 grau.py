print("Programa para calcular o Delta")

tentativas = ""


a = input("Digite o primeiro numero:")
while(a == tentativas):
    a = input("Digite o primeiro numero: ")

b = input("Digite o Segundo numero: ")
while(b == tentativas):
    b = input("Digite o Segundo numero: ")

c = input("Digite o terceiro numero: ")
while(c == tentativas):
    c = input("Digite o terceiro numero: ")

l_a = int(a)
l_b = int(b)
l_c = int(c)

import math

delta = l_b*l_b - (4*l_a*l_c)
print("O numero de Delta é:",delta)

if(delta > 0):
    print("Delta é maior que zero:", delta)
    x = -(l_b + math.sqrt(delta))/(2*l_a)
    y = -(l_b - math.sqrt(delta))/(2*l_a)
    print("Valores Delta: ",x,y)