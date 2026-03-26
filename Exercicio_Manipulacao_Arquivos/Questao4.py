arquivo = "alunos.txt"

nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2
status = "Aprovado" if media >= 6 else "Reprovado"

with open(arquivo, "a") as f:
    f.write("\n=== NOVO ALUNO ===\n")
    f.write(f"Nome: {nome}\n")
    f.write(f"Média: {media:.2f}\n")
    f.write(f"Status: {status}\n")

print("Dados do aluno salvos com sucesso!")
