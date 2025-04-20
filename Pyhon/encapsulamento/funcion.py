'''class Funcionario:
    def __init__(self,nome,cargo):
        self.nome = nome
        self.cargo = cargo
        
        self.salario = 0.0
    def mostrar_info(self):
        print(self.nome, self.cargo)
    
    def __mostrar_salario(self):
        print(self.salario)
    
    def mostrarDados(self):
        print(self.salario)
objecto =  Funcionario("Ana","Progamadora")
objecto.mostrarDados()'''
        
'''nome = input('insira o nome: ')
cargo = input('Insira p cargo')
objecto = Funcionario(nome,cargo)
objecto.mostrar_info()
objecto.mostrar_salario()'''


'''class ContaCorrentee:
    def __init__(self,saldo):
        self.__saldo = saldo
   
    def deposito(self,valor):
        self.__saldo += valor
    
    def ver_Saldo(self):
        print(f"Saldo atual: {self.__saldo}")

conta1 = ContaCorrentee(1000)
conta1.deposito(200)
conta1.ver_Saldo()'''

class ContaBancaria:
    def __init__(self,saldo):
        self.__saldo = saldo
        
    def depositar(self,valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('Valo irregular')
    
    def sacar(self,sacar):
        if sacar <= self.__saldo:
            self.__saldo -= sacar
        else:
            print('Valo irregular')
    
    def ver_Saldo(self):
        print(f"Saldo atual: {self.__saldo}")

conta1 = ContaBancaria(1000)
conta1.depositar(200)
conta1.sacar(4000)
conta1.ver_Saldo()

    
        