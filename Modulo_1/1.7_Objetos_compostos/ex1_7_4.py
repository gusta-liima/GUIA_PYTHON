# Fatiamento (Slicing)
# Criando uma lista e utilizando fatiamento para acessar uma parte da lista
lista = [10, 20, 30, 40, 50, 60, 70]

# Acessando do índice 2 até o 5 (não inclui o índice 5)
fatiamento_lista = lista[2:5]
print(fatiamento_lista)  
# Saída: [30, 40, 50]

# Operador in
# Verificando se um valor está presente na lista
valor_presente = 30
valor_na_lista = valor_presente in lista
print(valor_na_lista)  
# Saída: True

# Verificando se um valor não está presente na lista
valor_faltante = 100
valor_na_lista = valor_faltante in lista
print(valor_na_lista)  
# Saída: False

# Classe range
# Criando uma sequência de números usando range
sequencia_range = list(range(1, 6))  # de 1 até 5
print(sequencia_range)  
# Saída: [1, 2, 3, 4, 5]

# Operadores de Concatenação e Multiplicação
# Concatenação de listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista_concatenada = lista1 + lista2
print(lista_concatenada)  
# Saída: [1, 2, 3, 4, 5, 6]

# Multiplicação de listas
lista_multiplicada = lista1 * 2
print(lista_multiplicada)  
# Saída: [1, 2, 3, 1, 2, 3]

# Concatenação de strings
str1 = "Python "
str2 = "rocks!"
str_concatenada = str1 + str2
print(str_concatenada)  
# Saída: Python rocks!

# Multiplicação de strings
str_multiplicada = str1 * 3
print(str_multiplicada)  
# Saída: Python Python Python
