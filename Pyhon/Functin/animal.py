class Animal:
    def __init__(self, nome_animal, idade_animal):
        self.nome = nome_animal
        self.idade = idade_animal
    
    def __info(self):
        print(f'Nome: {self.nome}\nIdade: {self.idade} ano(s)')
    
    def dormir(self):
        print("Animal que gosta muito de dormir")
        
class TesteSuper(Animal):
    def __init__(self, nome_animal, idade_animal, nome):
        super().__init__(nome_animal, idade_animal)
        self.nome = nome
    
    def __info(self):
        print(f'Nome: {self.nome}\nIdade: {self.idade} ano(s)\nTipo: {self.nome}')
    
    def mostrar(self):
        self.__info()

# Criação do objeto
objecto = TesteSuper('animal 1', 2, 'gatinho')
objecto.mostrar()