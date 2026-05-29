from datetime import date

anoAtual = date.today().year

ano = int(input("Digite seu ano de nascimento: "))

idade = anoAtual - ano

if idade <= 9:
    print(f"Voce tem {idade} anos, Classe: MIRIM")
elif idade <= 14:
    print(f"Você tem {idade} anos, Classe: INFANTIL")
elif idade <= 19:
    print(f"Você tem {idade} anos, Classe: JUNIOR")
elif idade <= 20:
    print(f"Você tem {idade} anos, Classe: SÊNIOR")
else:
    print(f"Você tem {idade} anos, Classe: MASTER")
