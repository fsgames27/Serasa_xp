'''lista = []
for i in range( 2 ):
    nome = str(input('Nome: '))
    idade = int(input('Nome: '))
    prof = input(' yuor jobs? ')
    lista.append(nome)
    lista.append(idade)
    lista.append(prof)
print(lista)
'''
t = ()

for i in range(4):
    lista = list(t)
    n = int(input("Escreva um numero:"))
    lista.append(n)
    t=tuple(lista)

print(t)
print(lista)