try:
    num = int(input("Digite um número: "))
except ValueError:
    print("Erro! Apenas números inteiros são permitidos.")
else:
    print(f"Você digitou o número {num}.")  # Só será executado se não houver erro