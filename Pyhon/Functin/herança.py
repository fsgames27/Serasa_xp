class Animal:
    def __init__(self, nome_animal,idade_animal):
        self.nome = nome_animal
        self.idade = idade_animal
        
    def __info(self):
        print(f'nome:{self.nome}\nIdade:{self.idade} Ano(s)')
    
    def dormir(self):
        print("Animal que gosta muito de dormir")
    def passear(self):
        print(f"{self.nome} Está passeando")
    
class gato(Animal):
    def __init__(self, nome_animal, idade_animal,dono_animal):
        super().__init__(nome_animal, idade_animal)
        self.dono = dono_animal
    
    def __info(self):
        print(f'Nome: {self.nome}\nIdade: {self.idade} ano(s)\nDono: {self.dono}')
    def dormir(self):
        print(f"{self.nome} que gosta muito de dormir")
    def passear(self):
        print(f"{self.nome} Está passeando com {self.dono}")
    def comer(self):
        print(f"O gato: {self.nome} Está comendo")
    def mostrar(self):
        self.__info()

class coelho(Animal):
    def __init__(self, nome_animal, idade_animal,sexo_animal):
        super().__init__(nome_animal, idade_animal)
        self.sexo = sexo_animal
    
    def __info(self):
        print(f'Nome: {self.nome}\nIdade: {self.idade} ano(s)\nSexo do Animal: {self.sexo}')
    def dormir(self):
        print(f"{self.nome} que gosta muito de dormir")
    def passear(self):
        print(f"{self.nome} Está passeando")
    def tirarFoto(self):
        print(f"O coelho: {self.nome} , está tirando foto")
    def mostrar(self):
        self.__info()

class cachorro(Animal):
    def __init__(self, nome_animal, idade_animal,racao_animal):
        super().__init__(nome_animal, idade_animal)
        self.racao = racao_animal
    
    def __info(self):
        print(f'Nome: {self.nome}\nIdade: {self.idade} ano(s)\nRção favorita: {self.racao}')
    def dormir(self):
        print(f"{self.nome} que gosta muito de dormir")
    def passear(self):
        print(f"{self.nome} Esta passeando")
    def petshop(self):
        print(f"Fomos ao petshop comprar {self.racao}")
    def mostrar(self):
        self.__info()
        
animal1 = gato('frajora', 2, 'Fabrício')
animal1.mostrar()
animal1.passear()
animal1.comer()

animal2 = coelho('lunny', 3, 'masculino')
animal2.mostrar()
animal2.passear()
animal2.tirarFoto()

animal3 = cachorro('rex', 2, 'benegri')
animal3.mostrar()
animal3.passear()
animal3.petshop()
    
    
        