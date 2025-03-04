saldo = 1000

while True:
    print ("\n---Opções---")
    print("1 - Saldo")
    print("2 - Saque")
    print("3 - Deposito")
    print("4 - Sair")

    option = int(input("Escolha uma opição: "))

    if option == 1:
        print(f"O saldo é de R${saldo} ")

    if option == 2:
        saque = float(input("Digite o valor que deseja retirar: "))
        if saldo >= saque:
            saldo = saldo - saque
            print(f"O saldo atual é de R${saldo} ")
        else:
            print("Saldo insuficiente.")

    if option == 3:
        deposito = float(input("Digite o valor do depósito: "))
        saldo = saldo + deposito
        print(f"O saldo atual é de R${saldo} ")

    if option == 4:
        print("Programa encerrado.")
        break
