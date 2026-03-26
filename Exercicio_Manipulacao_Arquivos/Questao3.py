arquivo = "dados.txt"

linhas = []

with open(arquivo, "r") as f:
    for linha in f:
        linhas.append(linha.strip())  

print(linhas)
