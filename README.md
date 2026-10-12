# Relatório de Chamados de Help Desk

Script em Python que lê uma base de chamados de suporte de TI e gera um relatório com os principais indicadores da operação: volume, produtividade da equipe e cumprimento de prazos (SLA).

## O que o relatório mostra

- **Resumo geral:** total de chamados, fechados, pendentes e tempo médio de resolução
- **Chamados por status:** fechados, em andamento e abertos
- **Ranking de técnicos:** quantos chamados cada técnico fechou
- **Tempo médio por técnico:** quem resolve mais rápido
- **Cumprimento de SLA:** percentual de chamados resolvidos dentro da meta de cada prioridade

## Principais conclusões

Com a base de exemplo (300 chamados):

- **Volume e agilidade não andam juntos.** O técnico que mais fechou chamados (57) foi também o mais lento em média (28,5h). A técnica que menos fechou (40) foi a mais rápida (23,5h).
- **Quanto mais urgente o chamado, menos ele cumpre o prazo.** Só 26% dos chamados críticos foram resolvidos dentro da meta de 4h, contra 76% dos de prioridade baixa (meta de 72h).

## Exemplo de saída

```
==================================================
RANKING DE TÉCNICOS (chamados fechados)
==================================================
tecnico
Bruno    57
Diego    50
Ana      48
Carla    46
Elisa    40

==================================================
CUMPRIMENTO DE SLA POR PRIORIDADE
==================================================
Crítica: 26% dentro do prazo de 4h
Alta: 36% dentro do prazo de 8h
Média: 56% dentro do prazo de 24h
Baixa: 76% dentro do prazo de 72h
```

## Como rodar

Pré-requisito: Python 3.10 ou superior.

```bash
pip install -r requirements.txt
python relatorio.py
```

A base `chamados.csv` já vem no repositório. Para gerar uma nova base fictícia:

```bash
python gerar_dados.py
```

## Estrutura

| Arquivo | Função |
|---|---|
| `relatorio.py` | Lê o CSV e calcula os indicadores |
| `gerar_dados.py` | Gera a base fictícia de chamados |
| `chamados.csv` | Base de dados com 300 chamados |
| `requirements.txt` | Bibliotecas necessárias |

## Tecnologias

- Python
- pandas

## O que aprendi

Este foi meu primeiro projeto em Python, construído passo a passo:

- Ler arquivos CSV e converter colunas de texto em datas
- Calcular intervalos de tempo e criar novas colunas
- Filtrar, agrupar e ordenar dados com pandas (`groupby`, `value_counts`, `sort_values`)
- Organizar o código em funções com parâmetros
- Usar dicionários e loops (`for`) para aplicar a mesma regra a várias categorias

> Os dados são fictícios, gerados automaticamente para fins de estudo.
