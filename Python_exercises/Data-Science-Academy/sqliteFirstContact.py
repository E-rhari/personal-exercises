import sqlite3
from pandas import DataFrame

# conect to database
con = sqlite3.connect("cap12_dsa.db")

# Open a cursor to go trough the db
cursor = con.cursor()

# SQL QUERY to extract names from columns in db
sql_query = """SELECT name FROM sqlite_master WHERE type = 'table';""" # fetchs the name of all tables in db
                                                                       # sqlite_master is a metadata table
# execute query
cursor.execute(sql_query)
print(cursor.fetchall()[0]) # prints values in stream

queryAllVendas = "SELECT * FROM tb_vendas_dsa"
cursor.execute(queryAllVendas)
colNames = [description[0].replace("_", " ") for description in cursor.description]      # .description is a metadata properity that 
print(colNames)                                                        # should list the name of every column and row
                                                                       # but rows have no names so those are all None


query2 = "SELECT AVG(Unidades_Vendidas) from tb_vendas_dsa"
cursor.execute(query2)
print(cursor.fetchall()[0][0])

query3 = "SELECT Nome_Produto, AVG(Unidades_Vendidas) FROM tb_vendas_dsa GROUP BY Nome_Produto"
cursor.execute(query3)
print(cursor.fetchall())

query4 = """SELECT Nome_Produto, AVG(Unidades_Vendidas)
            FROM tb_vendas_dsa
            WHERE Valor_Unitario > 199
            GROUP BY Nome_Produto"""
cursor.execute(query4)
print(cursor.fetchall())

query5 = """SELECT Nome_Produto, AVG(Unidades_Vendidas)
            FROM tb_vendas_dsa
            WHERE Valor_Unitario > 199
            GROUP BY Nome_Produto
            HAVING AVG(Unidades_Vendidas) > 10"""


cursor.execute(queryAllVendas)
df = DataFrame(cursor.fetchall(), columns=colNames)
print(df)

mediaUnidadesVendidas = df['Unidades Vendidas'].mean()

print(df.groupby("Nome Produto")['Unidades Vendidas'].mean())

print(df[df["Valor Unitario"] > 19].groupby("Nome Produto")["Unidades Vendidas"].mean())

print(df[df["Valor Unitario"] > 199].groupby("Nome Produto").filter(lambda x: float(x["Unidades Vendidas"].mean()) > 10))
print(df[df['Valor Unitario'] > 199].groupby("Nome Produto")\
                                    .filter(lambda x: float(x["Unidades Vendidas"].mean()) > 10)\
                                    .groupby("Nome Produto")["Unidades Vendidas"].mean())


cursor.close()
con.close()