'''class Lapis:
    def __init__(self,modelo , cor, tamanho,ponta):
        self.modelo = modelo
        self.cor = cor
        self.tamanho = tamanho
        self.ponta = ponta
    def riscar(self):
        print(f"Está Riscando com um lapis do modelo {modelo}")
    def pintar(self):
        print(f'está pitando com um lapis da cor {cor}')
    def escrever(self):
        print(f'Está escrevendo com um lapis do tamanho {tamanho} e ponta {ponta}')

modelo = input('Informe o modelo: ')
cor =input('Informe a cor: ')
tamanho = input("Informe o tamanho do lapis: ")
ponta = input('Informe a ponta: ')
objecto = Lapis(modelo, cor, tamanho, ponta)
objecto.riscar()
objecto.pintar()
objecto.escrever()'''

'''class Carro:
    def __init__(self,marca,ano):
        self.marca=marca
        self.ano=ano
    def mostrar_info(self):
        print(f"Marca: {self.marca} ano: {self.ano}")
carro1= Carro( "Toyata", "2000")
carro1.mostrar_info()'''

'''class Aluno:
    def __init__(self,nota,aluno):
        self.nota=nota
        self.aluno=aluno
    def mostrarDetalhes(self):
        print(f"Nome: {self.aluno}\nNota: {self.nota}")
lucas=Aluno("Lucas","9,5")
lucas.mostrarDetalhes()'''

class Produto:
    def __init__(self,nome,preco):
        self.nome=nome
        self.preco=preco
    def desconto(self):
        descontoo = self.preco * 10/100
        precoFinal = self.preco - descontoo
        print(f"O produto custa: {self.preco} \n e terá um desconto de: {descontoo}\n O valor final é: {precoFinal}")
produto1 = Produto("fabricio", 230)
produto1.desconto()