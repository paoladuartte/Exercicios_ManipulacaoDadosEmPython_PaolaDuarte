arquivo = "calculadora.txt"

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
sub = num1 - num2
mult = num1 * num2
if num2 != 0: 
  div = num1 / num2 
else:
  div = "Erro! (divisão por zero)"

with open(arquivo, "a") as f:
    f.write("\n=== NOVA OPERAÇÃO ===\n")
    f.write(f"Números: {num1} e {num2}\n")
    f.write(f"Soma: {soma}\n")
    f.write(f"Subtração: {sub}\n")
    f.write(f"Multiplicação: {mult}\n")
    f.write(f"Divisão: {div}\n")

print("Resultados salvos com sucesso!")
