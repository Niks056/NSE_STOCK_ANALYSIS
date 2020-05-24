import pandas as pd
from nsepy import get_history
from datetime import date
import scipy.stats as st
import datetime as dt
import numpy as np

x=dt.datetime(2020,1,1)
y = dt.datetime(2020, 4, 12)


#Pharametuical Sector
data_cipla=get_history(symbol='CIPLA',start=x, end=y)
data_sunpharma=get_history(symbol='SUNPHARMA',start=x, end=y)
data_Divis_Laboratories=get_history(symbol='DIVISLAB',start=x, end=y)
data_dRREDDY=get_history(symbol='DRREDDY',start=x, end=y)

avg_SunPharma=data_sunpharma['Close'].mean()
data_Pharma=pd.DataFrame()
data_Pharma['Cipla']=data_cipla['Close']
data_Pharma['Sunpharma']=data_sunpharma[['Close']]
data_Pharma['Divis']=data_Divis_Laboratories[['Close']]
data_Pharma['DRREDDY']=data_dRREDDY[['Close']]
d_return=[]
stock_mean=data_Pharma.mean()
for col in data_Pharma[['Cipla','Sunpharma','Divis','DRREDDY']]:
   # Select column contents by column name using [] operator
   a=data_Pharma[col].pct_change()
   d_return.append(a)
d_Return=pd.DataFrame(d_return)
d_Return=d_Return.T

d_sd=[]
for col in d_Return[['Cipla','Sunpharma','Divis','DRREDDY']]:
 sd =d_Return[col].std()
 d_sd.append(sd)

mean=[]
for col in d_Return[['Cipla','Sunpharma','Divis','DRREDDY']]:
  m=d_Return[col].mean()
  mean.append(m)
z=st.norm.ppf(.95)
#z1=st.norm.ppf(.99)
Pre_Close=[]
all_low=[]
all_high=[]
for col in data_Pharma[['Cipla','Sunpharma','Divis','DRREDDY']]:
 last_vl=data_Pharma[col].tail(1)
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



