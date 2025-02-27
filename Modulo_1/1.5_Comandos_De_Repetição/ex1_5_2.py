# Atraves de n tentativas o usuário deve tentar acertar um número

num = 7
tentativas = 1

while tentativas <= 5:
    palpite = int(input(f"Essa é sua {tentativas}° tentativa, advinhe o número: "))
    if palpite == num:
        print("Parabéns você acertou o número!!!")
        break
    tentativas += 1
else:
    print("Você utilizou todas as tentativas.")