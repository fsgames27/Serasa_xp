print(('{:=^65}'.format('\033[7:0:45mLOJA C&A\033[m')))

preco = float(input("Valor das compras: R$ "))

print( ''' \033[31mFormas de Pagamentos\033[m
\033[7;31m[ 1 ]\033[m á vista dinheiro/pix \033[32m(10% de desconto)\033[m
\033[7;31m[ 2 ]\033[m á vista Cartão \033[32m(5% de desconto)\033[m
\033[7;31m[ 3 ]\033[m 2x no cartão \033[32m(5% de acrécimo)\033[m
\033[7;31m[ 4 ]\033[m 3x até 10x no cartão \033[32m(10% de acrécimo)\033[m''')

opcao = int(input('\033[mQual a forma de pagamento?100\033[m'))
if opcao == 1:
    valor = preco - (preco * 10/100)
elif opcao == 2:
    valor = preco - (preco * 5/100)
elif opcao ==3:
    valor = preco + (preco * 5/100)
    parcela = valor / 2
    print('O valor da parcela será 2x de R$ \033[31m{:.2f}\033[m com juros'.format(parcela))
elif opcao == 4:
    valor = preco + (preco * 10 /100)
    qualparcela = int(input('em quantas parcelas (de 3x até 10x)? '))
    parcela = valor / qualparcela
    print("O valor da parcela será {}x de R$ \033[31m{:.2f}\033[m com juros".format(qualparcela, parcela))
else:
    valor = preco
    print('\033[7;31mERRO\033[m\033[31m: Opção invalido!! tente novamente\033[m')
print('O total da compra será de \033[7;32mR$ {:.2f}\033[m.'.format(valor))