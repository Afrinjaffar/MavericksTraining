import pandas as pd
import sqlalchemy
import pyodbc
import urllib


params = urllib.parse.quote_plus("Driver={SQL SERVER};"
                      "Server=DESKTOP-NLNS7S5;"
                      "Database=bank;"
                      "Trusted_Connection=yes"
                      )

engine = sqlalchemy.create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))

data = pd.read_sql_table('Bank_churn_modelling', engine)
print(data.head())
