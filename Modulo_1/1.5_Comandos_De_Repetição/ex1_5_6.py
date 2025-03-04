usuario_correto = "admin"
senha_correta = "1234"
tentativas = 3

while tentativas>0:
    usuario = input("Digite o usuario: ")
    senha = input("Digite a senha: ")

    if usuario == "sair" or senha == "sair":
        print("Encerrando o programa.")
        break

    if usuario == "admin" and senha == "1234":
        print("Login efetuado com sucesso!")
        break

    if usuario != usuario_correto or senha != senha_correta:
        tentativas -= 1

        if tentativas == 0:
            print("Ultrapassou o limite de tentativas.")
            break

        print(f"Usaário ou senha incorreto, te resta {tentativas} tentativas.")
