import pandas as pd
from nsepy import get_history
from datetime import date
import scipy.stats as st
import datetime as dt
import numpy as np

x=dt.datetime(2020,1,1)
y = dt.datetime(2020, 5, 24)


data_HUL=get_history(symbol="HINDUNILVR",start=x, end=y)
data_BRITANNIA=get_history(symbol="BRITANNIA",start=x, end=y)
data_MARICO=get_history(symbol="MARICO ",start=x, end=y)
data_DABUR=get_history(symbol="DABUR",start=x, end=y)
data_COLGATE=get_history(symbol="COLPAL",start=x, end=y)
data_GILLETTE=get_history(symbol="GILLETTE",start=x, end=y)
data_ZYDUS=get_history(symbol="ZYDUSWELL",start=x, end=y)
data_Proctor_GAMBLE=get_history(symbol="PGHL",start=x, end=y)
data_ITC=  get_history(symbol="ITC",start=x, end=y)
data_NESTLE=get_history(symbol="NESTLEIND",start=x, end=y)
data_Varun_Beverages=get_history(symbol="VBL",start=x, end=y)
data_United_Brewerie=  get_history(symbol="UBL",start=x, end=y)

Avg_HUL=data_HUL['Close'].mean()
data_FMCG=pd.DataFrame()
data_FMCG['BRITANNIA']=data_BRITANNIA['Close']
data_FMCG['COLGATE']=data_COLGATE[['Close']]
data_FMCG['DABUR']=data_DABUR[['Close']]
data_FMCG['GILITTIE']=data_GILLETTE[['Close']]
data_FMCG['HINDUSTAN']=data_HUL['Close']
data_FMCG['ITC']=data_ITC[['Close']]
data_FMCG['MARICO']=data_MARICO[['Close']]
data_FMCG['NESTLE']=data_NESTLE['Close']
data_FMCG['PROCTOR_GAMBLE']=data_Proctor_GAMBLE[['Close']]
data_FMCG['UNITED_BREWERIE']=data_United_Brewerie[['Close']]
data_FMCG['VARUN_BEVERAGES']=data_Varun_Beverages[['Close']]
data_FMCG['ZYDUS']=data_ZYDUS[['Close']]

stock_mean=data_FMCG.mean()
industry_mean=stock_mean.mean()


l_FMCG=['BRITANNIA','COLGATE','DABUR','GILITTIE','HINDUSTAN','ITC','MARICO','NESTLE','PROCTOR_GAMBLE','UNITED_BREWERIE','VARUN_BEVERAGES','ZYDUS']
stock_mean=list(stock_mean)
res=[]
for i in range(0,len(stock_mean)):
    if(stock_mean[i]<industry_mean):
     a='buy'
     res.append(a)
    else:
      a="don't buy"
      res.append(a)

dec = zip(l_FMCG, res)
ldict= dict(dec)
ldict=pd.DataFrame.from_dict(ldict, orient='index')



d_return=[]
for col in data_FMCG[['BRITANNIA','COLGATE','DABUR','GILITTIE','HINDUSTAN','ITC','MARICO','NESTLE',
                      'PROCTOR_GAMBLE','UNITED_BREWERIE','VARUN_BEVERAGES','ZYDUS']]:
   # Select column contents by column name using [] operator
   a=data_FMCG[col].pct_change()
   d_return.append(a)
d_Return=pd.DataFrame(d_return)
d_Return=d_Return.T

d_sd=[]
for col in d_Return[['BRITANNIA','COLGATE','DABUR','GILITTIE','HINDUSTAN','ITC','MARICO','NESTLE',
                     'PROCTOR_GAMBLE','UNITED_BREWERIE','VARUN_BEVERAGES','ZYDUS']]:
 sd =d_Return[col].std()
 d_sd.append(sd)

mean=[]
for col in d_Return[['BRITANNIA','COLGATE','DABUR','GILITTIE','HINDUSTAN','ITC','MARICO','NESTLE',
                     'PROCTOR_GAMBLE','UNITED_BREWERIE','VARUN_BEVERAGES','ZYDUS']]:
  m=d_Return[col].mean()
  mean.append(m)
z=st.norm.ppf(.95)
#z1=st.norm.ppf(.99)
Pre_Close=[]
all_low=[]
all_high=[]
for col in data_FMCG[['BRITANNIA','COLGATE','DABUR','GILITTIE','HINDUSTAN','ITC','MARICO','NESTLE',
                      'PROCTOR_GAMBLE','UNITED_BREWERIE','VARUN_BEVERAGES','ZYDUS']]:
 last_vl=data_FMCG[col].tail(1)
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
