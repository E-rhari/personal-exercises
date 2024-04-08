import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm


def spacedPrint(string:str):
    print(string, end="\n\n")


def thematicBreakPrint(string:str, topRule:bool=False, bottomRule:bool=True, breaker="\n-------------------------\n"):
    if(topRule):
        print(breaker)
 
    print(string)

    if(bottomRule):
        print(breaker)


df_dsa = pd.read_csv('modulo14/dataset.csv')

thematicBreakPrint(df_dsa.shape)
thematicBreakPrint(df_dsa.columns)
thematicBreakPrint(df_dsa.info())

thematicBreakPrint(df_dsa.describe())

# valor_aluguel será nossa variável alvo
# area_m2 será nossa variável explicativa

thematicBreakPrint(df_dsa["valor_aluguel"].describe())
sns.histplot(data=df_dsa, x="valor_aluguel", kde=True)

thematicBreakPrint(df_dsa.corr()) # correlação pearson

plt.figure()
sns.scatterplot(data=df_dsa, x="area_m2", y="valor_aluguel")


# ### Regressão Linear (simples) ### #

y = df_dsa["valor_aluguel"]
x = df_dsa["area_m2"]

x = sm.add_constant(x) # adiciona uma coluna de 1s
modelo = sm.OLS(y, x) # Ordinary Least Squares
resultado = modelo.fit()
print(resultado.summary())

plt.figure()
plt.xlabel("area_m2", size=16)
plt.ylabel("valor_aluguel", size=16)
plt.plot(x["area_m2"], y, "o", label="Dados Reais")
plt.plot(x['area_m2'], resultado.fittedvalues, "r-", label="Linha de Regressão (Previsão do Modelo)")
plt.legend(loc="best")

plt.show()