import yfinance as yf
import pandas as pd
import pyodbc

server = 'DLGO-SQLSERVER\DLGO'
database = 'invetimentos'
username = 'sa'
password = 'Diihmax00!'
# ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
conn = pyodbc.connect(
    'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = conn.cursor()

query = "SELECT S FROM viewDivPy;"
df = pd.read_sql(query, conn)

print(df.columns)
for index, linha in df.iterrows():
    symbol = linha.S
    stock = yf.Ticker(symbol + '.SA')
    stock_df = pd.DataFrame(stock.dividends)
    for index, linha in stock_df.iterrows():
        print(symbol, index, linha.Dividends)
        cursor.execute("INSERT INTO stocks_dividends (symbol, date, Dividends) values (?,?,?)",
                       symbol, index, linha.Dividends)
        cursor.commit()
