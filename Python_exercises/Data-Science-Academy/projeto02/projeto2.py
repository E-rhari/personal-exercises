import pandas
import csv
import datetime


df = pandas.read_csv("./projeto02/bunda.csv")

# Cidade com Maior Valor de Venda de Produtos da Categoria 'Office Supplies'?
cidadeComMaiorVenda = df[df["Categoria"] == "Office Supplies"].groupby("Cidade")["Valor_Venda"].sum().sort_values(ascending=False).head(1)
print(cidadeComMaiorVenda)
print()

# Total de Vendas Por Data do Pedido?
totalVendasPorData = df[["Data_Pedido", "Valor_Venda"]].groupby("Data_Pedido").sum()
print(totalVendasPorData)
print()

# Total de Vendas por Estado?
totalVendasPorEstado = df[["Estado", "Valor_Venda"]].groupby("Estado").sum()
print(totalVendasPorEstado)
print()

# 10 Cidade com Maior Total de Vendas
cidadesComMaisVenda = df[["Cidade", "Valor_Venda"]].groupby("Cidade").sum("Valor_Venda").sort_values(ascending=False, by="Valor_Venda").head(10)
print(cidadesComMaisVenda)
print()

# Segmento Com o Maior Total de Vendas
segmentoComMaisVendas = df[["Segmento", "Valor_Venda"]].groupby("Segmento").sum("Valor_Venda").sort_values(ascending=False, by="Valor_Venda").head(1)
print(segmentoComMaisVendas)

# Total de Vendas por Segmento e por Ano
df["Data_Pedido"] = df["Data_Pedido"].str.split("/")
df["Ano"] = df["Data_Pedido"].str[2]
chirashisushi = df.groupby(["Ano", "Segmento"])["Valor_Venda"].sum()
print(chirashisushi)
print()

# Questão 07 (Ver Prova)
valoresMaioresQueMil = df[df["Valor_Venda"] >= 1000]
print(valoresMaioresQueMil)

# Questão 08 (Ver Prova)
print(df["Valor_Venda"])
df["Valor_Venda"] = df["Valor_Venda"].apply(lambda x: x * 0.85 if x >= 1000 else x)
print(df["Valor_Venda"][10])

# Média de Vendas Por Segmento, Por Ano e Por Mês?
# mediaDoida = df[["Segmento", ""]]

# Questão 10 (Ver Prova)
