# Criando uma tupla
frutas = ("maçã", "banana", "laranja", "banana", "uva")

# Acessando elementos por índice
print(frutas[1])  # Saída: banana

# Contando quantas vezes "banana" aparece na tupla
quantidade_bananas = frutas.count("banana")
print(f"A fruta 'banana' aparece {quantidade_bananas} vezes.")  # Saída: 2

# Descobrindo o índice da primeira ocorrência de "laranja"
indice_laranja = frutas.index("laranja")
print(f"A fruta 'laranja' está na posição {indice_laranja}.")  # Saída: 2

# Tentando modificar um elemento (gerará erro pois tuplas são imutáveis)
# frutas[0] = "pera"  # TypeError: 'tuple' object does not support item assignment
