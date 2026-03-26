arquivo = "texto.txt"

with open(arquivo, "r") as f:
    texto = f.read()

texto_modificado = texto.replace(" ", "_")

print("\n=== TEXTO MODIFICADO ===")
print(texto_modificado)
