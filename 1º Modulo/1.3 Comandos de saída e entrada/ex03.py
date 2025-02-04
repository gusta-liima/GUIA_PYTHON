# Tipo de apresentação
num = 1234.56789
print(f"Formato decimal: {num:.2f}")  # Saída: Formato decimal: 1234.57
print("Formato exponencial: {:.3e}".format(num))  # Saída: Formato exponencial: 1.235e+03

# Tamanho da apresentação (definindo largura mínima)
print(f"Texto com largura mínima: {'Python':>10}")  # Saída: "    Python"
print("Número com largura mínima: {:8.2f}".format(num))  # Saída: " 1234.57"

# Alinhamento da apresentação
print(f"Alinhado à esquerda: {'Python':<10}")  # Saída: "Python    "
print(f"Centralizado: {'Python':^10}")  # Saída: "  Python  "
print(f"Alinhado à direita: {'Python':>10}")  # Saída: "    Python"
