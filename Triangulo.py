print("Calculo do Triangulo")

tentativas = ""

a = input("Digite o Primeiro numero")
while(a == tentativas):
    a = input("Digite o Primeiro numero")

b = input("Digite o Segundo numero ")
while(b == tentativas):
    b = input("Digite o Segundo numero ")

c = input("Digite o terceiro numero")
while(c == tentativas):
    c = input("Digite o terceiro numero")

la = int(a)
lb = int(b)
lc = int(c)

triangulo = (lb - lc) < la < lb + lc and la - lc < lb < la + lc and la - lb  < lc < la + lb
print("Forma um triangulo")

if (lb == la and lc == lb):
    print("Triangulo Equilatero")

elif(la == lb or lb == lc or lc == la):
    print("isósceles,")

elif(la != lc and lc != lb):
    print("Triangulo Escaleno")

else:
    print("Não forma um triangulo")
