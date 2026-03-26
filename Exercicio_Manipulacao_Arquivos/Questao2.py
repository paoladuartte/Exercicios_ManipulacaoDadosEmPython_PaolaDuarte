from datetime import datetime

nome = input("Digite o nome: ")
rg = input("Digite o RG: ")
cpf = input("Digite o CPF: ")
ano_nascimento = int(input("Digite o ano de nascimento: "))

ano_atual = datetime.now().year
idade = ano_atual - ano_nascimento

arquivo = "dados_pessoa.txt"

with open(arquivo, "a") as f:  # "a" para adicionar sem apagar os anteriores
    f.write("==== Dados da Pessoa ====\n")
    f.write(f"Nome: {nome}\n")
    f.write(f"RG: {rg}\n")
    f.write(f"CPF: {cpf}\n")
    f.write(f"Ano de Nascimento: {ano_nascimento}\n")
    f.write(f"Idade: {idade} anos\n")
    f.write("---------------------------\n\n")

print("Dados salvos com sucesso!")
