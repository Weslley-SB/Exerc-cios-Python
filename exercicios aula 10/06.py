lista = []
n1 = int(input("Digite o primeiro numero para a lista: "))
n2 = int(input("Digite o segundo numero para a lista: "))
n3 = int(input("Digite o terceiro numero para a lista: "))

valores = n1, n2, n3
lista.extend(valores)

lista = sorted(lista)

print (f"O menor numero é o {lista[0]}, o maior é {lista[2]}")
