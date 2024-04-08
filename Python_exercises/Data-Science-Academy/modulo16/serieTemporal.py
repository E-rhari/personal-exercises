import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.holtwinters import SimpleExpSmoothing

import os
caminhoAtual = os.getcwd()
import sys
sys.path.append(f'{caminhoAtual}')

from lib.printers import *


df = pd.read_csv("modulo16/dataset.csv")
thematicBreakPrint(df.shape, topRule=True)
thematicBreakPrint(df.columns)
thematicBreakPrint(df.head())

# pré-processamento
thematicBreakPrint(df["Data"].min())
thematicBreakPrint(df["Data"].max())

thematicBreakPrint(df.info())
df["Data"] = pd.to_datetime(df["Data"])
thematicBreakPrint(df.info())

serieTemporal = df.set_index("Data")["Total_Vendas"]
thematicBreakPrint(serieTemporal)
serieTemporal = serieTemporal.asfreq("D")
thematicBreakPrint(serieTemporal)

plt.figure(figsize=(12, 6))
plt.plot(serieTemporal)
plt.xlabel("Data")
plt.ylabel("Vendas")
plt.title("Série Temporal de Vendas")
plt.grid(True)

plt.figure(figsize=(24, 6))
plt.plot(serieTemporal, color="w", linewidth=1.25)
plt.xlabel("Data")
plt.ylabel("Vendas")
plt.title("Série Temporal de Vendas")

plt.grid(True, color="k", linewidth=0.5, linestyle=":")
plt.gca().set_xticks(pd.date_range('2023-01-01', periods=12, freq="MS"))
plt.gca().set_facecolor("blue") # Get Current Axis (Eu acho?)

modelo = SimpleExpSmoothing(serieTemporal)
modelo_ajustado = modelo.fit(smoothing_level = 0.2)

suavizacao_exponencial = modelo_ajustado.fittedvalues

plt.figure(figsize=(12, 6))
plt.plot(serieTemporal, label="Valores Reais")
plt.plot(suavizacao_exponencial, label="Valores Previstos", linestyle='--')
plt.xlabel("Data")
plt.ylabel("Vendas")
plt.title("Modelo de Suavização Exponencial")
plt.legend()

numPrevisoes = 1
previsoes = modelo_ajustado.forecast(steps = numPrevisoes)
thematicBreakPrint(previsoes)

# plt.hist(df["Total_Vendas"], df["Data"], histtype="bar", rwidth=0.8)
plt.show()