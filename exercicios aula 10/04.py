viagem = int(input("Qual a distancia da viagem? (em KM) "))

if viagem <= 200:
    passagem = viagem * 0.50
    print(f"O preço fica {passagem:.2f}")
else:
    passagem = viagem * 0.45
    print(f"O preço fica {passagem:.2f}")