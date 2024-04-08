import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sea
from pandas import DataFrame 

import random
import warnings

warnings.filterwarnings("ignore") # ayo that seems no good


dados = sea.load_dataset("tips")

print(dados.head())

sea.jointplot(data=dados, x="total_bill", y="tip", kind="reg")
sea.lmplot(data=dados, x="total_bill", y="tip", col="smoker")


df = DataFrame()
df['idade'] = random.sample(range(20, 100), 30)
df['peso']  = random.sample(range(55, 150), 30)

sea.lmplot(data=df, x="idade", y="peso", fit_reg=True)
sea.kdeplot(df.idade)
# sea.distplot(df.peso)
plt.figure()
plt.hist(df.idade, alpha=.3)
plt.figure()
sea.rugplot(df.idade)
plt.figure()
sea.boxplot(df.idade, color='m')
plt.figure()
sea.violinplot(df.idade, color='g')
plt.figure()
sea.clustermap(df)


plt.show()