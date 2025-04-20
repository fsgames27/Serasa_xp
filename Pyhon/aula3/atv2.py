n1 = float(input("Digite a sua primeira nota: "))
n2 = float(input("Digite a sua segunda nota: "))
print(f"A primeira é {n1} e a segunda é {n2}")
media = (n1 + n2)/2
print(f"A média do aluno é {media}")

if media >= 7:
    print("Você foi \033[0;30;42mAprovado\033[m")
    
elif media >=5 and media <= 6.9:
    print("Você está em \033[0;30;43mRecuperação\033[m")
    
else:
    print("Você foi \033[0;30;417mReprovado\033[m")