# Solicitação de um número até que ele seja maior ou igual a 10

num = int(input("Digite um numero maior ou igual a 10: "))

while num<10:
    print(f"O numero {num} é menor do que 10.")
    num = int(input("Digite um número maior ou igual a 10: "))

print(f"O numero {num} é maior ou igual a 10.")