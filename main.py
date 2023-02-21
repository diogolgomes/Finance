import investpy as inv
import pyodbc
import pandas as pd

server = 'DLGO-SQLSERVER\DLGO'
database = 'invetimentos'
username = 'sa'
password = 'Diihmax00!'
# ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
cursor = conn.cursor()

br = inv.stocks.get_stocks(country='brazil')
teste_df = pd.DataFrame(br)

for index,linha in teste_df.iterrows():
    linha.name = linha[1]
    cursor.execute("INSERT INTO stocks (country, name, full_name, currency, symbol) values (?,?,?,?,?)",
                   linha.country,linha.name,linha.full_name,linha.currency,linha.symbol)
    cursor.commit()

