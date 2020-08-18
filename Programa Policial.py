print("Programa Policial")

count = 0
tentativas = ""
pergunta1 = str(input("Telefonou para a vítima? s or n: "))
while(pergunta1 == tentativas):
    pergunta1 = str(input("Telefonou para a vítima? s or n: "))

pergunta2 = str(input("Esteve no local do crime? s or n: "))
while(pergunta2 == tentativas):
    pergunta2 = str(input("Esteve no local do crime? s or n: "))

pergunta3 = str(input("Mora perto da vítima? s or n: "))
while(pergunta3 == tentativas):
    pergunta3 = str(input("Mora perto da vítima? s or n: "))

pergunta4 = str(input("Devia para a vítima? s or n: "))
while(pergunta4 == tentativas):
    pergunta4 = str(input("Devia para a vítima? s or n: "))

pergunta5 = str(input("Já trabalhou com a vítima? s or n: "))
while(pergunta5 == tentativas):
    pergunta5 = str(input("Já trabalhou com a vítima? s or n: "))


if(pergunta1 == "s"):
    count = count + 1

if(pergunta2 == "s"):
    count = count + 1

if(pergunta3 == "s"):
    count = count + 1

if(pergunta4 == "s"):
    count = count + 1

if(pergunta5 == "s"):
    count = count + 1


if(count == 2 ):
    print("Suspeita")

if(count == 3 or count == 4):
    print("Cumplice")

if(count == 5):
    print("Assassino")

else:
    if(count < 2):
        print("Inocente")




