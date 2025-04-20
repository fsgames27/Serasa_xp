'''pessoa = { "nome" : "fabricio", "idade":30, "cidade":"São paulo"}
print(pessoa["nome"])
print(pessoa["idade"])
pessoa["profissão"] = "engenheira"
pessoa["idade"] = 31
del pessoa["cidade"]
print(pessoa)'''

fruta_cores = {
    'maça':'vermelho',
    'banana':'amarelo',
    'laranja':'laranja'
}

cor_maçã =fruta_cores.get('maça')
print(f'cor da maçã: {cor_maçã}')

cor_abacaxi = fruta_cores.get('abacaxi')

cor_uva = fruta_cores.get('uva',  'desconhecido')
print(f'Cor da uva: {cor_uva}')

fruta_cores['banana'] = 'verde'
fruta_cores['morango'] = 'vermelho'

print(fruta_cores)

cor_laranja = fruta_cores.pop('laranja')
print(cor_laranja)

del fruta_cores['maça']
print(fruta_cores)

'''fruta_cores = {
    'maça':'vermelho',
    'banana':'amarelo',
    'laranja':'laranja'
}

for fruta, cor in fruta_cores.items():
    print(f"A {fruta} é {cor}")'''