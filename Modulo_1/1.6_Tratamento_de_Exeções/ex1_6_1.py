try:
    num = int(input("Digite um número: "))
    print(f"Você digitou o numero{num}")
except ValueError:
    print("Digite um valor válido!")
    