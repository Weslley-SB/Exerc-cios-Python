numero = int(input("Digite um numero: "))
escolha = int(input("Quer converter para qual base?\n 1 para binário:\n 2 para octal:\n 3 para hexadecimal:"))

if escolha == 1:
    print("Binário, seu número: ", numero, bin(numero)[2:])
elif  escolha == 2:
    print("Octal, seu número: ", numero, oct(numero)[2:])
elif escolha == 3:
    print("hexadecimal, seu número: ", numero, hex(numero)[2:])
else:
    print("Escolha Inválida.")