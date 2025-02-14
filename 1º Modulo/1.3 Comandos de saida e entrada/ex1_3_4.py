# Exemplo_04) Crie um programa em Python que solicite três números inteiros ao usuário. Em seguida, exiba esses números na tela separados por um traço (-). Além disso, o programa deve calcular e exibir: O maior número, O menor número e a média destes números.

# Entrada de dados
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

# Saída de dados
print("\nNúmeros digitados: ")
print(n1, n2, n3, sep = '-')

# Maior e menor
print(f"\nO maior número é: {max(n1, n2, n3)}")
print(f"O menor número é: {min(n1, n2, n3)}")

# Calculo e apresentação da média
med = (n1 + n2 + n3)/3
print(f"\nA média dos 3 números é: {med:.2f}")

# Note que as funções max() e min(), que aqui foram apresentadas, são funções embutidas (built-in) do Python que servem para encontrar, respectivamente, o maior e o menor valor dentro de uma sequência de dados, como listas, tuplas ou múltiplos argumentos passados diretamente.