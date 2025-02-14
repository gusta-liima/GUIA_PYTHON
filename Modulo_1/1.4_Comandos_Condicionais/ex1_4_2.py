# Notas das provas

p1 = float(input("Digite a sua nota da primeira prova: "))
p2 = float(input("Digite a sua nota da segunda prova: "))

# Notas das atividade

a1 = float(input("Digite a nota da primeira atividade: "))
a2 = float(input("Digite a nota da segunda atividade: "))
a3 = float(input("Digite a nota da terceira atividade: "))

# Média das atividades

Media_Atividade = (a1+a2+a3)/3

# Média final

Media_Final = (p1*0.4)+(p2*0.4)+(Media_Atividade*0.2)

# Status de aprovação

if Media_Final >= 7:
    print("Aluno aprovado.")
elif Media_Final < 7 and Media_Final >= 4:
    print("Aluno de recuperação.")
else:
    print("Aluno reprovado.")
