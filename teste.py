import yfinance as yf
from datetime import datetime

symbol = 'TAEE11'
symbol = yf.Ticker(symbol + '.SA')

# GET TODAYS DATE AND CONVERT IT TO A STRING WITH YYYY-MM-DD FORMAT (YFINANCE EXPECTS THAT FORMAT)
end_date = datetime.now().strftime('%Y-%m-%d')
symbol_hist = symbol.history(start='2015-01-01', end=end_date)
print(symbol_hist.columns)