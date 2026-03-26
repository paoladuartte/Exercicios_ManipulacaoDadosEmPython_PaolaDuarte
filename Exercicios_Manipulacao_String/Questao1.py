arquivo_entrada = "dna.txt"
with open("dna.txt", "r") as f:
    cadeia = f.read().strip()

cadeia_inversa = cadeia[::-1]

with open("dna_resultado.txt", "w") as f:
    f.write(f"Entrada: {cadeia}\n")
    f.write(f"Saída: {cadeia_inversa}\n")

print("Entrada:", cadeia)
print("Saída:", cadeia_inversa)
