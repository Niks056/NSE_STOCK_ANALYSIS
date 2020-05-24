import pandas as pd
from nsepy import get_history
from datetime import date
import scipy.stats as st
import datetime as dt
import numpy as np

x=dt.datetime(2020,1,1)
y = dt.datetime(2020, 4, 12)

#BankingSector
data_ICICI=get_history(symbol='ICICIBANK',start=x, end=y)
data_HDFCBank=get_history(symbol="HDFCBANK",start=x, end=y)
data_SBI =  get_history(symbol="SBIN", start=x, end=y)
data_YES = get_history(symbol="YESBANK", start=x, end=y)
data_INDUSLAND=get_history(symbol="INDUSINDBK",start=x, end=y)
data_BANKBARODA=get_history(symbol="BANKBARODA",start=x, end=y)
data_pnb=get_history(symbol='PNB',start=x, end=y)

data_Banking=pd.DataFrame()
data_Banking['ICICI']=data_ICICI['Close']
data_Banking['SBI']=data_SBI[['Close']]
data_Banking['PNB']=data_pnb[['Close']]
data_Banking['YES_BANK']=data_YES[['Close']]
data_Banking['INDUSLAND']=data_INDUSLAND[['Close']]
data_Banking['BANKBARODA']=data_YES[['Close']]
data_Banking['HDFC']=data_HDFCBank[['Close']]
avg=data_Banking.mean()


d_return=[]
for col in data_Banking[['ICICI','SBI','YES_BANK','PNB','INDUSLAND','BANKBARODA','HDFC']]:
   # Select column contents by column name using [] operator
   a=data_Banking[col].pct_change()
   d_return.append(a)
d_Return=pd.DataFrame(d_return)
d_Return=d_Return.T

d_sd=[]
for col in d_Return[['ICICI','SBI','YES_BANK','PNB','INDUSLAND','BANKBARODA','HDFC']]:
 sd =d_Return[col].std()
 d_sd.append(sd)

mean=[]
for col in d_Return[['ICICI','SBI','YES_BANK','PNB','INDUSLAND','BANKBARODA','HDFC']]:
  m=d_Return[col].mean()
  mean.append(m)
z=st.norm.ppf(.95)
#z1=st.norm.ppf(.99)
Pre_Close=[]
all_low=[]
all_high=[]
for col in data_Banking[['ICICI','SBI','YES_BANK','PNB','INDUSLAND','BANKBARODA','HDFC']]:
 last_vl=data_Banking[col].tail(1)
 per_val=last_vl*z*sd
#per_val=last_vl*z1*sd
 low_value=last_vl-per_val
 High_value=last_vl+per_val
 all_low.append(low_value)
 all_high.append(High_value)

df=pd.DataFrame()
df['Average_price']=avg
df['Low_Price']=pd.DataFrame(all_low)
df['High_price']=pd.DataFrame(all_high)
