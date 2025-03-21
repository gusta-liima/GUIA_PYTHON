frase = "  Aprender Python é divertido!  "

# Removendo espaços extras
frase_limpa = frase.strip()
print(frase_limpa)  # Saída: "Aprender Python é divertido!"

# Convertendo para maiúsculas e minúsculas
print(frase_limpa.upper())  # "APRENDER PYTHON É DIVERTIDO!"
print(frase_limpa.lower())  # "aprender python é divertido!"

# Substituindo palavras
nova_frase = frase_limpa.replace("divertido", "incrível")
print(nova_frase)  # "Aprender Python é incrível!"

# Dividindo em palavras
palavras = frase_limpa.split()
print(palavras)  # ['Aprender', 'Python', 'é', 'divertido!']

# Contando quantas vezes "Python" aparece
print(frase_limpa.count("Python"))  # Saída: 1
