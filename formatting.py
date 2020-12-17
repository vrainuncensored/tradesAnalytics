import pandas as pd
import numpy as np
pd.set_option('display.max_rows', 10000)
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)

df=pd.read_csv(r'/Users/rooblebagga/Documents/2020-12-14-AccountStatement.csv')

x=df[df["Account Statement"]=="Cash Balance"].index.values
y=df[df["Account Statement"]=="Futures Statements"].index.values
Cash_Balance = df[x[0]:y[0]]