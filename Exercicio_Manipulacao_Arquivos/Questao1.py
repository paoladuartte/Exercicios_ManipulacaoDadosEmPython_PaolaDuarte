arquivo = "tabuada_9.txt"

with open(arquivo, "w") as f:
    f.write("=== TABUADA DO 9 ===\n")
    f.write("---------------------\n")

    for i in range(1, 11):
        resultado = 9 * i 
        linha = f"9 x {i} = {resultado}\n"
        f.write(linha)

print("Tabuada salva com sucesso!")