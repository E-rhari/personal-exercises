from pandas import DataFrame

def doubleLineBreakPrint(text:str):
    print(text)
    print()


dic = {"Nome":    ["Kumiko Oumae", "Reina", "Hazuki Katou", "Saphire Kawashima", "Kaori"],
       "Idade":   [15, 15, 15, 15, 17],
       "Gayness": [10, 6, 1, 2, 5]}

indexes = [f"Girl {x+1}" for x in range(len(dic["Nome"]))]
df = DataFrame(dic, columns = ["Nome", "Idade", "Gayness", "Favorites"], index = indexes)

doubleLineBreakPrint(df)
doubleLineBreakPrint(df.describe())
doubleLineBreakPrint(df[ df["Idade"] >= 2])
doubleLineBreakPrint(df["Nome"])
doubleLineBreakPrint(df[["Nome", "Idade"]])

doubleLineBreakPrint(df.isna().sum())

# df.astype({"Favorites": "float"})
df = df.infer_objects(copy=True).fillna(value={"Favorites": 4})
doubleLineBreakPrint(df)

doubleLineBreakPrint(df["Idade"].describe())
doubleLineBreakPrint(df.query('Idade == 15'))
doubleLineBreakPrint(df.query('5 < Gayness <= 8'))

doubleLineBreakPrint(df[df["Nome"] == "Kumiko"])

doubleLineBreakPrint(df[["Gayness", "Idade", "Nome"]].groupby(["Idade", "Nome"]).mean())
doubleLineBreakPrint(df[["Gayness", "Idade"]].groupby(["Idade"]).mean())

doubleLineBreakPrint(df[["Gayness", "Idade", "Nome"]].groupby(["Idade", "Nome"]).agg({"mean", "std", "count"}))
doubleLineBreakPrint(df[["Gayness", "Idade"]].groupby(["Idade"]).agg(["mean", "std", "count"]))

doubleLineBreakPrint(df[df.Nome.str.startswith("K")].sample())
doubleLineBreakPrint(df[df.Nome.str.endswith("i")].head())

