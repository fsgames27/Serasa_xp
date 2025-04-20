'''
soma = 0 
cont = 0

for num in range(1,8):
    valor = int(input('digite o {} valor: '.format(num)))
    if valor % 2 == 0:
        soma += valor # soma = soma + valor
        cont += 1 
print('você informou {} números é a soma é {}'.format(cont,soma))'''

#(strip)Eliminar os espaços antes e depois
#(upper) para converter em maiúsculo
frase = str(input('digite um texto: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1 , -1 , -1):
    inverso += junto[letra]
print(f"O texto fica: {inverso}")
    

