nome_1 = "Gustavo"
idade_1 = 21

mensagem = "Meu nome é {} e eu tenho {} anos.".format(nome_1, idade_1)
print(mensagem)  

# Tambem é possível utilizar indices para definir a posição dos valores

mensagem = "Meu nome é {1} e eu tenho {0} anos.".format(idade_1, nome_1)
print(mensagem) 

# Ou ainda, usar nomes de variáveis dentro das chaves para maior legibilidade:

mensagem = "Meu nome é {nome_2} e eu tenho {idade_2} anos.".format(nome_2 = "José", idade_2 = 25)
print(mensagem)