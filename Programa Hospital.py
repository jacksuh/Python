print("Programa para o Hospital")
pt= 360
sep = 210
ct  = 185
wi = 3
cabo = 4
tentativas = ""

dias = input("Digite quantidade de dias de hospedagem: ")
while(dias == tentativas):
    dias = input("Digite quantidade de dias de hospedagem: ")

tipo = input("Digite o tipo de convênio Particular, semi-particular, coletivo: ")
while(tipo == tentativas):
    tipo = input("Digite o tipo de convênio Particular, semi-particular, coletivo: ")

wifi = input("Digite se usou a internet sim ou não: ")
while(wifi == tentativas):
    wifi = input("Digite se usou a internet sim ou não: ")

tv_cabo = input("Digite se utilizou a tv sim ou não: ")
while(tv_cabo == tentativas):
    tv_cabo = input("Digite se utilizou a tv sim ou não: ")

di = int(dias)
ti = str(tipo)
wif = str(wifi)
cb = str(tv_cabo)

total_particular = di * pt
total_particularwifi = di * pt + wi + cabo
total_particularwifi2 = di * pt + wi
total_particularwifi3 = di * pt + cabo

total_sep = di * sep
total_sep1 = di * sep + wi + cabo
total_sep2 = di * sep + wi
total_sep3 = di * sep + cabo

total_ct = di * ct
total_ct1 = di * ct + wi + cabo
total_ct2 = di * ct + wi
total_ct3 = di * ct + cabo

#PARTICULAR
if(tipo == "particular" and wifi == "s" and tv_cabo == "s"):
    print("Hospital Comunitario ", "\nTipo de Quarto: ",tipo, "\nDiarias: ", dias,"\nValor da diaria: ",pt,"\nValor Wifi: ",wi,
          "\nValor Tv a cabo: ",cabo,"\n Total: ", total_particularwifi)

elif(tipo == "particular" and wifi == "n" and tv_cabo == "n"):
    print("Hospital Comunitario ", "\nTipo de Quarto: ",tipo, "\n Diarias: ", dias,"\nValor da diaria: R$ {:.2f} ".format(pt),
          "\n Total: R${:.2f}".format(total_particular))

elif(tipo == "particular" and wifi == "s" and tv_cabo == "n"):
    print("Hospital Comunitario ", "\nTipo de Quarto:", tipo, "\n Diarias: ", dias, "\nValor da diaria",
          pt,"\nValor Wifi: ",wi,"\n Total: ", total_particularwifi2)

elif(tipo == "particular" and wifi == "n" and tv_cabo == "s"):
    print("Hospital Comunitario ", "\nTipo de Quarto:", tipo, "\n Diarias: ", dias, "\nValor da diaria",
          pt, "\nValor Tv a Cabo: ", cabo, "\n Total: ", total_particularwifi3)

#SEMI-PARTICULAR
elif(tipo == "semi-particular" and wifi == "s" and tv_cabo == "s" ):
    print("Hospital Comunitario ", "\nTipo de Quarto:", tipo, "\nDiarias: ", dias, "\nValor da diaria", sep,
          "\nValor Wifi: ", wi, "\nValor Tv a cabo: ", cabo, "\nTotal: ", total_sep1)

elif(tipo == "semi-particular" and wifi == "n" and tv_cabo == "n"):
    print("Hospital Comunitario ", "\nTipo de Quarto:", tipo, "\n Diarias: ", dias, "\nValor da diaria", sep,
          "\n Total: ", total_sep)

elif(tipo == "semi-particular" and wifi == "s" and tv_cabo == "n"):
    print("Hospital Comunitario ", "\nTipo de Quarto:", tipo, "\n Diarias: ", dias, "\nValor da diaria",
          sep, "\nValor Wifi: ", wi, "\n Total: ", total_sep2)

elif(tipo == "semi-particular" and wifi == "n" and tv_cabo == "s"):
    print("Hospital Comunitario ", "\nTipo de Quarto:", tipo, "\n Diarias: ", dias, "\nValor da diaria",
          pt, "\nValor Tv a Cabo: ", cabo, "\n Total: ", total_sep3)

#COLETIVO
elif(tipo == "coletivo" and wifi == "s" and tv_cabo == "s" ):
    print("Valor coletivo: ",total_ct1)
    print("Hospital Comunitario ", "\nTipo de Quarto:", tipo, "\nDiarias: ", dias, "\nValor da diaria", ct,
          "\nValor Wifi: ", wi, "\nValor Tv a cabo: ", cabo, "\nTotal: ", total_ct1)

elif(tipo == "coletivo" and wifi == "n" and tv_cabo == "n"):
    print("Hospital Comunitario ", "\nTipo de Quarto:", tipo, "\nDiarias: ", dias, "\nValor da diaria", ct,
          "\n Total: ", total_ct)

elif(tipo == "coletivo" and wifi == "s" and tv_cabo == "n"):
    print("Hospital Comunitario ", "\nTipo de Quarto:", tipo, "\n Diarias: ", dias, "\nValor da diaria",
          ct, "\nValor Wifi: ", wi, "\n Total: ", total_ct2)

elif(tipo == "coletivo" and wifi == "n" and tv_cabo == "s"):
    print("Valor coletivo: ", total_ct3)
    print("Hospital Comunitario ", "\nTipo de Quarto:", tipo, "\n Diarias: ", dias, "\nValor da diaria",
          ct, "\nValor Tv a Cabo: ", cabo, "\n Total: ", total_ct3)
else:
    print("Nada foi digitado")

