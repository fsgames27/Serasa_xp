'''nome = str(input("nome: ").strip().upper())
print(len(nome))'''

'''frase = 'Curso de progamador de sistemas'
print(frase.replace('progamador de sistemas', 'python'))'''

'''frase = 'Curso de progamador de sistemas'
print(frase.count('a'))
print(frase.count('A'))
print(frase.upper().count("C"))'''

'''a = 'menino'
b = 'menina'
print('O sexo é \033[32m{}\033[m ou \033[35m{}\033[m?').__format__(a,b)
print('O sexo é {}{}{}')'''

n = int(input("Digite um numero: "))
resultado = n % 2
if resultado == 0 :
    print("Esse numero é par")
else:
    print(" Esse numero é impar")    