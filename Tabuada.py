print("Tabuada")

a = int(input("Digite um numero"))
nu = 2

for b in range(11):
        tab = (a * b)%2
        if(tab==0):
            print("Numero é divisivel")
            print(a,"x",b,"=",tab)
        else:
            print("Numero não é divisivel")
            print(a, "x", b, "=", tab)

