import pandas as pd
from nsepy import get_history
from datetime import date
import scipy.stats as st
import datetime as dt
import numpy as np

x=dt.datetime(2019,1,1)
y = dt.datetime(2020,5,8)


#It Sector
data_TCS=get_history(symbol='TCS',start=x, end=y)
data_MindTree=get_history(symbol='MINDTREE',start=x, end=y)
data_WIPRO=get_history(symbol="WIPRO",start=x, end=y)
data_INFOSYS=get_history(symbol="INFY",start=x, end=y)
data_PERSISTENT=get_history(symbol="PERSISTENT",start=x, end=y)
data_HCL=get_history(symbol="HCLTECH",start=x, end=y)

Avg_MindTree=data_MindTree['Close'].mean()
Avg_Persistent=data_PERSISTENT['Close'].mean()
data_IT=pd.DataFrame()
data_IT['TCS']=data_TCS['Close']
data_IT['MindTree']=data_MindTree[['Close']]
data_IT['Presistent']=data_PERSISTENT[['Close']]
data_IT['Wipro']=data_WIPRO[['Close']]
data_IT['INFOSYS']=data_PERSISTENT[['Close']]
data_HCL['HCL']=data_HCL[['Close']]
stock_mean=data_IT.mean()

d_return=[]
for col in data_IT[['TCS','MindTree','Presistent','Wipro','INFOSYS','HCL']]:
   # Select column contents by column name using [] operator
   a=data_IT[col].pct_change()
   d_return.append(a)
d_Return=pd.DataFrame(d_return)
d_Return=d_Return.T

d_sd=[]
for col in d_Return[['TCS','MindTree','Presistent','Wipro','INFOSYS','HCL']]:
 sd =d_Return[col].std()
 d_sd.append(sd)

mean=[]
for col in d_Return[['TCS','MindTree','Presistent','Wipro','INFOSYS','HCL']]:
  m=d_Return[col].mean()
  mean.append(m)
z=st.norm.ppf(.95)
#z1=st.norm.ppf(.99)
Pre_Close=[]
all_low=[]
all_high=[]
for col in data_IT[['TCS','MindTree','Presistent','Wipro','INFOSYS','HCL']]:
 last_vl=data_IT[col].tail(1)
 per_val=last_vl*z*sd
#per_val=last_vl*z1*sd
 low_value=last_vl-per_val
 High_value=last_vl+per_val
 all_low.append(low_value)
 all_high.append(High_value)

df=pd.DataFrame()
df['Average_price']=stock_mean
df['Low_Price']=pd.DataFrame(all_low)
df['High_price']=pd.DataFrame(all_high)
