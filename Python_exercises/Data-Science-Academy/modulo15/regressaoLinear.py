import numpy as np
from pandas import read_csv
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model    import LinearRegression
from sklearn.model_selection import train_test_split

import os
caminhoAtual = os.getcwd()
import sys
sys.path.append(f'{caminhoAtual}')

from lib.printers import *



df = read_csv('modulo15/dataset.csv')

thematicBreakPrint(df.shape)
thematicBreakPrint(df.columns)
thematicBreakPrint(df.head())
thematicBreakPrint(df.info())

thematicBreakPrint(df.isnull().sum())
thematicBreakPrint(df.corr()) # correlação forte!

thematicBreakPrint(df['horas_estudo_mes'].describe())
sns.histplot(data = df, x="horas_estudo_mes", kde=True)

x = np.array(df['horas_estudo_mes'])
thematicBreakPrint(type(x))
x = x.reshape(-1, 1)
thematicBreakPrint(type(x))

y = df["salario"]

plt.figure()
plt.scatter(x, y, color="blue", label="Dados Reais Históricos")
plt.xlabel("Horas de Estudo")
plt.ylabel("Salário")
plt.legend()

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.2, random_state=42)

modelo = LinearRegression()
modelo.fit(x_treino, y_treino)

plt.figure()
plt.scatter(x, y, color = "blue", label="Dados Históricos")
plt.plot(x, modelo.predict(x), color="red", label="Reta de Regressão com as Previsões do Modelo")
plt.xlabel("Horas de Estudo")
plt.ylabel("Salário")
plt.legend()

score = modelo.score(x_teste, y_teste)
print(score)



plt.show()