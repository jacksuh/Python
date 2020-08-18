
import Padaria

print("Bem-Vindo")

log = "jackson"
senha = "123456"
loop = ""

a = input("Insira o usuario: ")
while(a != log or a == loop or a.isalpha() == False):
    print("Informações invalidas")
    a = input("Insira o usuario: ")

b = input("Insira a senha: ")
while(b != senha or b == loop or b.isdigit() == False):
    print("Senha Invalida")
    b = input("Insira a senha: ")

if(a == log and b == senha):
    print("Login Autorizado: ")
    Padaria.padaria()

else:
    print("Usuario e senha invalido")