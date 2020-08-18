print("Programa Estoque")

n1 = "sul"
n2 = "norte"
n3 = "leste"
n4 = "oeste"
n5 = "noroeste"
n6 = "sudeste"
n7 = "centro_oeste"
n8 = "nordeste"
tentativas = ""

codigo = str(input("Digite o código da região: "))
while(codigo == tentativas):
    codigo = str(input("Digite o código da região: "))

cliente = str(input("Digite o nome do cliente: "))
while(cliente == tentativas):
    cliente = str(input("Digite o nome do cliente: "))

vende =  str(input("Informe o vendedor: "))
while(vende == tentativas):
    vende = str(input("Informe o vendedor: "))


valorprod = int(input("Valor do produto: "))

valorquant = int(input("Quantidade de peças: "))




#sul
s = (valorprod * valorquant)
s1 = s * 1
s2 = s + s1
s3 = s2 * 0.065

#norte
nn = valorprod * valorquant
nn1 = nn * 1.10
nn2 = nn + nn1
nn3 = nn2 * 0.08

#leste
les = valorprod * valorquant
les1 = les * 1.15
les2 = les + les1
les3 = les2 * 0.07

#oeste
oes = valorprod * valorquant
oes1 = oes * 1.20
oes2 = oes + oes1
oes3 = oes2 * 0.11

#noroeste
nor = valorprod * valorquant
nor1 = nor * 1.25
nor2 = nor + nor1
nor3 = nor2 * 0.15

#sudeste
sud = valorprod * valorquant
sud1 = sud * 1.30
sud2 = sud + sud1
sud3 = sud2 * 0.12

#centro-oeste
coes = valorprod * valorquant
coes1 = coes * 1.30
coes2 = coes + coes1
coes3 = coes2 * 0.12

#nordeste
nord = valorprod * valorquant
nord1 = nord * 1.30
nord2 = nord + nord1
nord3 = nord2 * 0.12

#sul
if(codigo == "n1" and valorquant >= 1000):
    print("Zona: ",n1,"\nNome Cliente: ",cliente,"\nValor da peça: ",valorprod, "\nValor Total: ", s,
          "\nValor do frete 1 real por peça: R$ {:.2f}".format(s2),
          "\nQuantidade de peças: ",valorquant,"\nNome Vendedor",vende,"\nComissão Vendedor: R$ {:.2f}".format(s3))
#R$ {:f} com o :f estamos dizendo para o sistema que o campo é float.
#R$ {:.2f} dizemos quantos pontos numeros queremos depois do ponto.

#norte
elif(codigo == "n2" and valorquant >= 1000):
    print("Zona: ",n2,"\nNome Cliente: ", cliente, "\nValor da peça: ", valorprod, "\nValor Total: ", nn,
          "\nValor do frete 1 real por peça: ", nn2,
          "\nQuantidade de peças: ", valorquant, "\nNome Vendedor", vende, "\nComissão Vendedor: ", nn3)

#leste
elif(codigo == "n3" and valorquant >= 1000):
    print("Zona: ",n3,"\nNome Cliente: ", cliente, "\nValor da peça: ", valorprod, "\nValor Total: ",les,
          "\nValor do frete 1 real por peça: ",round(les2),
          "\nQuantidade de peças: ", valorquant, "\nNome Vendedor", vende, "\nComissão Vendedor: ", les3)

#oeste
elif(codigo == "n4" and valorquant >= 1000):
    print("Zona: ", n4, "\nNome Cliente: ", cliente, "\nValor da peça: ", valorprod, "\nValor Total: ", oes,
          "\nValor do frete 1 real por peça: ", round(oes2),
          "\nQuantidade de peças: ", valorquant, "\nNome Vendedor", vende, "\nComissão Vendedor: ", oes3)

#noroeste
elif(codigo == "n5" and valorquant >= 1000):
    print("Zona: ", n5, "\nNome Cliente: ", cliente, "\nValor da peça: ", valorprod, "\nValor Total: ", nor,
          "\nValor do frete 1 real por peça: ", round(nor2),
          "\nQuantidade de peças: ", valorquant, "\nNome Vendedor", vende, "\nComissão Vendedor: ", nor3)

#Sudeste
elif(codigo == "n6" and valorquant >= 1000):
    print("Zona: ", n6, "\nNome Cliente: ", cliente, "\nValor da peça: ", valorprod, "\nValor Total: ", sud,
          "\nValor do frete 1 real por peça: ", round(sud2),
          "\nQuantidade de peças: ", valorquant, "\nNome Vendedor", vende, "\nComissão Vendedor: ", sud3)

#Centro-oeste
elif(codigo == "n7" and valorquant >= 1000):
    print("Zona: ", n6, "\nNome Cliente: ", cliente, "\nValor da peça: ", valorprod, "\nValor Total: ", coes,
          "\nValor do frete 1 real por peça: ", round(coes2),
          "\nQuantidade de peças: ", valorquant, "\nNome Vendedor", vende, "\nComissão Vendedor: ", coes3)

#nordeste
elif(codigo == "n8" and valorquant >= 1000):
    print("Zona: ", n6, "\nNome Cliente: ", cliente, "\nValor da peça: ", valorprod, "\nValor Total: ", nord,
          "\nValor do frete 1 real por peça: ", round(nord2),
          "\nQuantidade de peças: ", valorquant, "\nNome Vendedor", vende, "\nComissão Vendedor: ", nord3)