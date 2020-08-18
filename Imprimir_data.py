print("Imprimir Data")


data = input("A data: ")
while data.isdigit() == False:
    print("Somente numeros inteiros formato ")
    data = input("A data: ")

dia = int(data[6:8])
mes = int(data[4:6])
ano = int(data[:4])

print('{:4d}/{:2d}/{:2d}'.format(dia, mes, ano))
