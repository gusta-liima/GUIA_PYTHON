try:
    num = int(input("Digite o numerador: "))
    div = int(input("Digite o divisor: "))

    resultado = num/div

    print(f"O resultado da divisão é: {resultado}")

except ValueError:
    print("Erro! Digite apenas números!")
except ZeroDivisionError:
    print("Erro! Divisão por zero!")
