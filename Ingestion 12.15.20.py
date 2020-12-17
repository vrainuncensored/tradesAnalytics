#!/usr/bin/env python
# coding: utf-8

# In[135]:


import pandas as pd
import numpy as np
pd.set_option('display.max_rows', 10000)
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)


# In[136]:


df=pd.read_csv(r'/Users/rooblebagga/Documents/2020-12-14-AccountStatement.csv')


# In[138]:


#Cash Balance Data Set 
x=df[df["Account Statement"]=="Cash Balance"].index.values
y=df[df["Account Statement"]=="Futures Statements"].index.values
Cash_Balance = df[x[0]+1:y[0]-1]
Cash_Balance=Cash_Balance.rename(columns=Cash_Balance.iloc[0]).drop(Cash_Balance.index[0]).reset_index()
Cash_Balance = Cash_Balance.loc[:, Cash_Balance.columns.notnull()]
Cash_Balance.drop(['index'],axis=1, inplace=True)


# In[139]:


a=df[df["Account Statement"]=="Account Order History"].index.values
b=df[df["Account Statement"]=="Account Trade History"].index.values
Order_History = df[a[0]+1:b[0]-1]


# In[140]:


c=df[df["Account Statement"]=="Equities"].index.values
d=df[df["Account Statement"]=="Profits and Losses"].index.values
Equities = df[c[0]+1:d[0]-2]
Equities=Equities.rename(columns=Equities.iloc[0]).drop(Equities.index[0]).reset_index()
Equities = Equities.loc[:, Equities.columns.notnull()]
Equities.drop(['index'],axis=1, inplace=True)


# In[141]:


e=df[df["Account Statement"]=="Profits and Losses"].index.values
f=df[df["Account Statement"]=="Account Summary"].index.values
PnL = df[e[0]+1:f[0]-2]
PnL=PnL.rename(columns=PnL.iloc[0]).drop(PnL.index[0]).reset_index()
PnL = PnL.loc[:, PnL.columns.notnull()]
PnL.drop(['index'],axis=1, inplace=True)


# In[142]:


Order_History=Order_History.rename(columns=Order_History.iloc[0]).drop(Order_History.index[0]).reset_index()
Order_History.drop(['Notes', 'T','index'],axis=1, inplace=True)


# In[143]:


Order_History = Order_History.rename(columns={np.nan:'Order Type', 'PRICE':'Price'})
Order_History['Price']=Order_History['Price'].replace({'~':np.nan})
Order_History.drop(['Exp', 'Strike','Type'],axis=1, inplace=True)


# In[210]:


# def applyFunc(s):
#     if s.str.contains('%'):
#         return 'Yes'
#     else:
#         return 'No'
# Order_History['Qty %'] = Order_History['Qty'].apply(applyFunc)


# In[84]:


Equities


# In[196]:


PnL =PnL.replace({'\$':'', '\^':'','%':'',',':''}, regex=True)
PnL['P/L Open'] = PnL['P/L Open'].astype(str).str.replace('\((.*)\)', '-\\1')
PnL['P/L %'] = PnL['P/L %'].astype(str).str.replace('\((.*)\)', '-\\1')
PnL['P/L Day'] = PnL['P/L Day'].astype(str).str.replace('\((.*)\)', '-\\1')
PnL['P/L YTD'] = PnL['P/L YTD'].astype(str).str.replace('\((.*)\)', '-\\1')
PnL['P/L Diff'] = PnL['P/L Diff'].astype(str).str.replace('\((.*)\)', '-\\1')

PnL['P/L Open']=PnL['P/L Open'].astype(float)
PnL['P/L %']=PnL['P/L %'].astype(float)
PnL['P/L Day']=PnL['P/L Day'].astype(float)
PnL['P/L YTD']=PnL['P/L YTD'].astype(float)
PnL['P/L Diff']=PnL['P/L Diff'].astype(float)
PnL['Margin Req']=PnL['Margin Req'].astype(float)
PnL['Mark Value']=PnL['Mark Value'].astype(float)


# In[159]:


df2=Cash_Balance.copy() 


# In[161]:


trades=df2[df2['TYPE']=='TRD']
description=trades['DESCRIPTION'].str.split(expand = True)
description = description.rename(columns={0:'Order Type', 1:'Quantity',2:'Stock',3:'Price'})
description =description.replace({'@':''}, regex=True)
description['Price']=description['Price'].astype(float)
description['Quantity']=description['Quantity'].astype(float)
df_merged = trades.merge(description, how='outer', left_index=True, right_index=True)


# In[209]:


# df_merged.groupby(["DATE", "Stock"])["Quantity"].count()


# In[ ]:




