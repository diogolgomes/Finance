import yfinance as yf
import pandas as pd
import pyodbc
from datetime import datetime

server = 'DLGO-SQLSERVER\DLGO'
database = 'invetimentos'
username = 'sa'
password = 'Diihmax00!'
# ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
conn = pyodbc.connect(
    'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = conn.cursor()

query = "SELECT S FROM viewHistPy;"
df = pd.read_sql(query, conn)

print(df)
for index, linha in df.iterrows():
    symbol = linha.S
    stock = yf.Ticker(symbol + '.SA')
    end_date = datetime.now().strftime('%Y-%m-%d')
    stock_hist = stock.history(start='2015-01-01', end=end_date)
    stock_hist = pd.DataFrame(stock_hist)
    for index, linha in stock_hist.iterrows():
        print(symbol, index, linha.Open, linha.High, linha.Low, linha.Close, linha.Volume)
        cursor.execute("INSERT INTO stocks_history (symbol, date, [Open], High, Low, [Close], Volume) values (?,?,?,?,?,?,?)",
                       symbol, index, linha.Open, linha.High, linha.Low, linha.Close, linha.Volume)
        cursor.commit()