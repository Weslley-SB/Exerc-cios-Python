velocidade = int(input("Qual a velocidade do carro? "))
multa = (velocidade - 80) * 7

if velocidade > 80:
    print("O carro foi multado.")
    print(f"O valor da multa é {multa}.")
else:
    print("O carro está dentro da lei.")
