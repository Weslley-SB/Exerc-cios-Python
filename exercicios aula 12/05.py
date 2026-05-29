n1 = int(input("Digite sua nota 1: "))
n2 = int(input("Digite sua nota 2: "))
media = (n1 + n2) / 2

print(f"Sua notas são: 1º:  {n1} e 2º:  {n2}\ne a media é {media}")

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")