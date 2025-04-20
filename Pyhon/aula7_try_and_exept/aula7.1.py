
'''while True:
 try:
    numero = int(input('digite um numero: '))
    print(numero)
 except ValueError as erro:
        print('só aceitamos numeros')
 else:
        print('Executando o else: Não teve erros!!')
'''
'''try:
    n1 = int(input('digite um numero: '))
    n2 = int(input('digite outro numero: '))
    resultado = n1 / n2
except ZeroDivisionError:
    print("Não é possivel dividir por zero")
except ValueError as erro:
        print('só aceitamos numeros')
else:
   print(f' O resultado da divisão {resultado:.2f}')
finally:
    print(' Cabou ')'''
    
'''lista = [ ' 10 ', ' dez ', ' 8 ' , ' nove ', ' 2']
for itens in lista:
    try:
        numero = int(itens)
        print(f"A conversão foi: {numero}")
    except ValueError:
        print(f"Não foi convertido:  {itens}")
print('fim')'''

dic = { 'fabrício' : 9 , 'hosana' : 10, 'ana' : 9}
nome = input("De qual aluno vc quer mudar a nota: ")
try:
    nota = dic[nome]
    print(f"A nota de {nome} é: {nota}")
except KeyError:
        print('Nome não encontrado')

    
    