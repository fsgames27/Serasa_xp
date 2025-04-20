print("Vamos calcular seu IMC?")
nome = input("Qual é o seu nome? ")
altura = float(input("Qual é a sua altua?"))
peso = float(input("Qual é o seu peso?"))

alturaFinal = altura ** 2

imc = peso/alturaFinal

print(f"Olá maria \n Sua altura é de: {altura}\n Seu peso: {peso}\n IMC: {imc}")