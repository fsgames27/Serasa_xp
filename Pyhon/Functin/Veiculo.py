class Veiculo:
    def __init__(self,carro,ano):
        self.carro = carro
        self.ano = ano
        
    def __infor(self):
        print(f"Marca: {self.carro}\n Ano: {self.ano}")
    
    def andar(self):
        print(f"O veiculo está andando")
class carro(Veiculo):
    def __init__(self,carro,ano):
        super.__init__(self,carro,ano)
    
    def carro(self):
        super().andar()
        print(f"O {self.carro} está andado")
    def gasosa(self):
        print(f"O carro {self.carro} está andando")
    def estacionar(self):
        print(f"O carro {self.carro} está estacionado")

objeto = Veiculo("toyota", 2000)
objeto.andar()
objeto.gasosa()
objeto.estacionar()
