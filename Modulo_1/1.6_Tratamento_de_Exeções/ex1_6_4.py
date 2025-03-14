try:
    arquivo = open("dados.txt", "r")  # Tenta abrir um arquivo
    conteudo = arquivo.read()
    print(conteudo)
except FileNotFoundError:
    print("Erro! O arquivo não foi encontrado.")
finally:
    print("Finalizando o programa.")  # Sempre será executado