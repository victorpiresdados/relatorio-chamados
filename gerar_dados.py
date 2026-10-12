# gerar_dados.py
# Cria um arquivo "chamados.csv" com chamados FICTÍCIOS de help desk.
# Rode uma vez:  python gerar_dados.py

import csv                                 # módulo do Python para ler/escrever CSV
import random                              # para sortear valores
from datetime import datetime, timedelta   # para trabalhar com datas e horas

random.seed(42)  # "semente": faz o sorteio sair sempre igual (resultados reproduzíveis)

# Listas com as opções que serão sorteadas
TECNICOS = ["Ana", "Bruno", "Carla", "Diego", "Elisa"]
CATEGORIAS = ["Rede", "Hardware", "Software", "Acesso/Senha", "Impressora", "E-mail"]
PRIORIDADES = ["Baixa", "Média", "Alta", "Crítica"]

QUANTIDADE = 300                     # quantos chamados vamos criar
INICIO = datetime(2026, 7, 1, 8, 0)  # data do primeiro chamado possível

linhas = []  # lista vazia que vai guardar cada chamado

for numero in range(1, QUANTIDADE + 1):
    # Abertura: um dia aleatório em ~3 meses, num horário entre 8h e 18h
    abertura = INICIO + timedelta(days=random.randint(0, 91),
                                  hours=random.randint(0, 10),
                                  minutes=random.randint(0, 59))

    prioridade = random.choices(PRIORIDADES, weights=[40, 35, 18, 7])[0]

    # 80% dos chamados estão fechados; o resto ainda está aberto ou em andamento
    sorteio = random.random()
    if sorteio < 0.80:
        status = "Fechado"
        # Chamados mais urgentes costumam ser resolvidos mais rápido
        horas_max = {"Crítica": 8, "Alta": 24, "Média": 48, "Baixa": 96}[prioridade]
        fechamento = abertura + timedelta(hours=random.uniform(0.5, horas_max))
        data_fechamento = fechamento.strftime("%Y-%m-%d %H:%M")
    elif sorteio < 0.92:
        status = "Em andamento"
        data_fechamento = ""  # vazio = ainda não fechou
    else:
        status = "Aberto"
        data_fechamento = ""

    linhas.append({
        "id": numero,
        "data_abertura": abertura.strftime("%Y-%m-%d %H:%M"),
        "data_fechamento": data_fechamento,
        "categoria": random.choice(CATEGORIAS),
        "prioridade": prioridade,
        "status": status,
        "tecnico": random.choice(TECNICOS),
    })

# Escreve tudo no arquivo CSV
with open("chamados.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.DictWriter(arquivo, fieldnames=linhas[0].keys())
    escritor.writeheader()     # primeira linha: nomes das colunas
    escritor.writerows(linhas)  # demais linhas: os chamados

print(f"Pronto! {len(linhas)} chamados salvos em chamados.csv")
