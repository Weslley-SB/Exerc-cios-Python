salario = float(input("Digite o seu salário: "))
if salario <= 1250.00:
    aumento = salario * 0.15
else:
    aumento = salario * 0.10

salario += aumento

print(f"Seu aumento é {aumento}, assim ficando com salario de {salario}.")