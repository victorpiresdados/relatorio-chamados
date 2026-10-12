# Relatório de chamados de help desk.
# Lê chamados.csv e mostra os principais indicadores da operação no terminal.

import pandas as pd

# Meta de tempo de resolução (SLA), em horas, por prioridade
SLA_HORAS = {"Crítica": 4, "Alta": 8, "Média": 24, "Baixa": 72}

chamados = pd.read_csv("chamados.csv", parse_dates=["data_abertura", "data_fechamento"])

# Chamados ainda abertos não têm data de fechamento e ficam sem valor nesta coluna
chamados["horas_resolucao"] = (chamados["data_fechamento"] - chamados["data_abertura"]) / pd.Timedelta(hours=1)


def titulo(texto):
    print()
    print("=" * 50)
    print(texto)
    print("=" * 50)


def mostrar_resumo(chamados):
    titulo("RESUMO GERAL")

    total = len(chamados)
    fechados = (chamados["status"] == "Fechado").sum()
    pendentes = total - fechados
    percentual_fechados = (fechados / total) * 100

    print(f"Total de chamados: {total}")
    print(f"Fechados: {fechados}")
    print(f"Pendentes: {pendentes}")
    print(f"Percentual de fechados: {percentual_fechados:.0f}%")
    print(f"Tempo médio p/ resolver: {chamados['horas_resolucao'].mean():.1f} horas")


def mostrar_por_status(chamados):
    titulo("CHAMADOS POR STATUS")
    contagem = chamados["status"].value_counts()
    print(contagem.to_string())


def mostrar_ranking_tecnicos(chamados):
    titulo("RANKING DE TÉCNICOS (chamados fechados)")

    fechados = chamados[chamados["status"] == "Fechado"]
    ranking = fechados.groupby("tecnico")["id"].count()
    ranking = ranking.sort_values(ascending=False)

    print(ranking.to_string())


def mostrar_tempo_por_tecnico(chamados):
    titulo("TEMPO MÉDIO DE RESOLUÇÃO POR TÉCNICO (chamados fechados)")

    fechados = chamados[chamados["status"] == "Fechado"]
    tempo_medio = fechados.groupby("tecnico")["horas_resolucao"].mean()
    tempo_medio = tempo_medio.sort_values(ascending=True).round(1)

    print(tempo_medio.to_string())


def mostrar_sla(chamados):
    titulo("CUMPRIMENTO DE SLA POR PRIORIDADE")

    fechados = chamados[chamados["status"] == "Fechado"]

    for prioridade, meta in SLA_HORAS.items():
        grupo = fechados[fechados["prioridade"] == prioridade]
        # Média de True/False = percentual de chamados resolvidos dentro da meta
        dentro_do_prazo = (grupo["horas_resolucao"] <= meta).mean()

        print(f"{prioridade}: {dentro_do_prazo:.0%} dentro do prazo de {meta}h")


mostrar_resumo(chamados)
mostrar_por_status(chamados)
mostrar_ranking_tecnicos(chamados)
mostrar_tempo_por_tecnico(chamados)
mostrar_sla(chamados)
