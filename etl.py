import csv

usuarios = []

# EXTRAÇÃO
with open("usuarios.csv", mode="r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        usuarios.append(linha)

# TRANSFORMAÇÃO
mensagens = []

for usuario in usuarios:
    mensagem = f"""
Olá, {usuario['nome']}!

Temos novidades exclusivas para sua conta {usuario['conta']}.
Aproveite benefícios especiais preparados para você 💙
"""
    mensagens.append(mensagem)

# CARREGAMENTO
with open("mensagens.txt", "w", encoding="utf-8") as arquivo:
    for msg in mensagens:
        arquivo.write(msg + "\n" + "-"*40 + "\n")

print("Arquivo mensagens.txt criado com sucesso!")
