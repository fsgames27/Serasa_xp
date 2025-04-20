'''def soma_numero():
    num1 = float(input("Primeiro numero: "))
    num2 = float(input("segundo numero: "))
    soma = num1 + num2
    print('soma: ', soma)

soma_numero()
'''

'''def recebe_nome(nome):
    print(f'Bem vindo {nome}')

nome = input('Digite seu nome?')
recebe_nome(nome)'''

'''def recebe_num(num1,num2):
    soma = num1 + num2
    return soma
num1 = int(input("Num 1:"))
num2 = int(input("Num 2:"))
print(recebe_num(num1 , num2))'''

'''def soma(n1,n2): return n1+n2
def sub(n1,n2): return n1-n2
n1 = int(input('numero 1: '))
n2 = int(input('numero 2: '))
print(soma(n1,n2))
print(sub(n1,n2))'''
'''
variavel_global = ' '

def funcao1():
    variavel_global = "oi"
    print(variavel_global)

def funcao2():
    variavel_global = "outro lado"
    print(variavel_global)

funcao1()
funcao2()
'''

'''import random
print(random.randint(1,10))'''

'''import tkinter

tkinter.Tk()
tkinter.mainloop()

tkinter = "olá!"
print(tkinter)'''

'''def saudacao(nome="visitante"):
    print(f'Bem vindo {nome}')

saudacao("ANA")
saudacao()'''


'''def soma(Soma = 1 + 5): return Soma
print(soma())
'''

'''def mostrarLocal():
    mensagem = "Essa é ima variavel local"
    print(mensagem)

mostrarLocal()'''
'''contador = 0

def incrementar():
    global contador
    contador += 1
incrementar()
print(contador)'''

'''import random
print(random.randint(1,100))'''

'''def saudacao(nome):
    print(f'Bem vindo {nome}')

nome = input('Digite seu nome?')
saudacao(nome)'''

import random
def adivinhe_numero(r = random.randint(1,10)):
   while r:
    print("tente adivinhar o numero em que estou pensando")
    n = int(input("Qual é o numero??"))
    
    if r == n :
        print("Parabens vc acertou")
        break
    else:
        print("vc errou")
adivinhe_numero()
