print("Peso")

a = input("Digite o Peso: ")
while(a.isdigit() == False):
    a = input("Digite o Peso: ")

a1 = int(a)

b = (a1 * 0.05)+ a1

c = (a1 * 0.10)- a1

print("Se você ganhar 5%: ",b,"Se você perder 10%: ",c)