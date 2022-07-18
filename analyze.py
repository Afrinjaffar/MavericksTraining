import pandas as pd


data = pd.read_csv(r'C:\Users\mrafi\Downloads\combined_cycle_power_plant (1).csv', sep=';')
#print(data)

print(data.head(4))

print(data.info())

print(data.describe())

print(data.fillna(data.mean(), inplace=True))

print(data.isna().sum())

print(data.replace('[@#&$%+-/*]', ''))

print(data.drop_duplicates(keep='first', inplace=True))

print(data.corr())

print(data[['temperature', 'energy_output']].corr())
#The temeperature vs electrical output has negative correlation.

print(data[['ambient_pressure','energy_output']].corr())
#ambient_pressure vs electrical output has positive correlation.

print(data[['exhaust_vacuum', 'energy_output']].corr())
#Exhaust vacuum vs electrical output has negative correlation.

print(data[['relative_humidity','energy_output']].corr())
#Relative humidity vs electrical output has positive correlation.





