with open("frases.txt", "r") as f:
    texto = f.read()

palavras = texto.split()

palavras_unicas = []
for p in palavras:
    if p not in palavras_unicas:
        palavras_unicas.append(p)

print(palavras_unicas)
