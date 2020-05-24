import pandas as pd
from nsepy import get_history
from datetime import date
import scipy.stats as st
import datetime as dt

x=dt.datetime(2020,1,1)
y=dt.datetime(2020,5,24)


data_hindustan=get_history(symbol='HINDUNILVR',start=x,end=y)
data_Reliance=get_history(symbol='RELIANCE',start=x, end=y)
data_Tititan= get_history(symbol="Titan Company ",start=x, end=y)
data_sunpharma=get_history(symbol='SUNPHARMA',start=x, end=y)
data_TCS=get_history(symbol='TCS',start=x, end=y)
data_MindTree=get_history(symbol='MINDTREE',start=x, end=y)
data_PERSISTENT=get_history(symbol="PERSISTENT ",start=x, end=y)
data_ICICI=get_history(symbol='ICICIBANK',start=x, end=y)
data_SBI= get_history(symbol="SBIN", start=x, end=y)
data_TATACOMM=get_history(symbol="TATACOMM",start=x, end=y)
data_cipla=get_history(symbol='CIPLA',start=x, end=y)
data_HDFC=get_history(symbol="HDFC",start=x,end=y)

d=pd.DataFrame()
d['Hindustan']=data_hindustan['Close']
d['Titan']=data_Tititan[['Close']]
d['Reliance']=data_Reliance[['Close']]
d['Mind_Tree']=data_MindTree[['Close']]
d['Tcs']=data_TCS[['Close']]
d['Persistent']=data_PERSISTENT[['Close']]
d['ICICI']=data_ICICI[['Close']]
d['SBI']=data_SBI[['Close']]
d['HDFC']=data_HDFC[['Close']]
d['Cipla']=data_cipla[['Close']]
d['Sunpharma']=data_sunpharma[['Close']]
d['TataComm']=data_TATACOMM[['Close']]
stock_mean=d.mean()
#d['Infosys_close']=data_INFOSYS[['Close']]

d_return=[]
for col in d[['Hindustan','Titan','SBI','Mind_Tree','SunPharma','Cipla','persistent','ICICI','Reliance','Tcs','HDFC','TATACOMM']]:
   # Select column contents by column name using [] operator
   a=d[col].pct_change()
   d_return.append(a)
d_Return=pd.DataFrame(d_return)
d_Return=d_Return.T


d_sd=[]
for col in d_Return[['Hindustan','Titan','SBI','Mind_Tree','SunPharma','Cipla','persistent','ICICI','Reliance','Tcs','HDFC','TATACOMM']]:
 sd =d_Return[col].std()
 d_sd.append(sd)

mean=[]
for col in d_Return[['Hindustan','Titan','SBI','Mind_Tree','SunPharma','Cipla','persistent','ICICI','Reliance','Tcs','HDFC','TATACOMM']]:
  m=d_Return[col].mean()
  mean.append(m)
z=st.norm.ppf(.95)
#z1=st.norm.ppf(.99)
Pre_Close=[]
all_low=[]
all_high=[]
for col in d[['Hindustan','Titan','SBI','Mind_Tree','SunPharma','Cipla','persistent','ICICI','Reliance','Tcs','HDFC','TATACOMM']]:
 last_vl=d[col].tail(1)
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



