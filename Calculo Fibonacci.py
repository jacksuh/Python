#Calculo Fibonacci

print("Calculo Fibonacci")

fibo = int(input("Quantos fibonacci: "))
while(fibo <= 0):
    print("Digite um numero maior que zero")
    fibo = int(input("Quantos fibonacci: "))

n1 = 0
n2 = 1
n3 = ""

print(n1,n2,end=",")
for n in range(0,fibo):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3,end=",")

#Calculo fibonacci 2

print("\nCalculo Fibonacci")

fibo = int(input("Quantos fibonacci: "))
while(fibo <= 0):
    print("Digite um numero maior que zero")
    fibo = int(input("Quantos fibonacci: "))

n1 = 0
n2 = 1
n3 = ""

print(n1,end=",")

for n in range(0,fibo):
    fib = n1, n2 = n2, n1 + n2
    print(fib,end=",")

