import sqlite3 as sql
import pandas as pd


weather = pd.read_csv('https://github.com/alanjones2/dataviz/raw/master/londonweather.csv')

conn = sql.connect('weather.db')
# weather.to_sql('weather', conn)

weather = pd.read_sql('SELECT * FROM weather', conn)
print(weather.head())

y2010 = pd.read_sql('SELECT * FROM weather WHERE Year == 2010', conn)
# print(y2010)

y1960 = pd.read_sql('SELECT * FROM weather WHERE Year == 1960', conn)
# print(y1960)


high = pd.read_sql('SELECT Year,Month,Tmax FROM weather WHERE Tmax > 25 ORDER BY Tmax DESC', conn)
print(high.head())

july = pd.read_sql('SELECT Year,Month,Tmax FROM weather WHERE month == 6', conn)
print(july)
