'''import calculadora
r1 = float(input("Digite o primeiro numero: "))
r2 = float(input("Digite o segundo numero: "))
print(f"O resultado é: {calculadora.soma(r1 , r2)}")
'''
'''
class cachorro:
    espicie = 'canina'
    
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        
    def latir(self):
        return f"{self.nome} está Latindo e tem {self.idade} anos"
    
meu_cachorro = cachorro("Rex", 5)

print(meu_cachorro)
print(meu_cachorro.latir())
'''

class Lapis:
    def __init__(self,modelo , cor, tamanho,ponta):
        self.modelo = modelo
        self.cor = cor
        self.tamanho = tamanho
        self.ponta = ponta
    def riscar(self):
        print("Está Riscando")
    def pintar(self):
        print('está pitando')
    def escrever(self):
        print('Está escrevendo')
        