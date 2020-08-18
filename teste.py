

def cria_conta(numero,titular,saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def deposita(conta, valor):
    conta["Saldo"] += valor

def sacar(conta,valor):
    conta["Saldo"] -= valor

def extrato(conta):
    print("Saldo é {}".format(conta["Saldo"]))

