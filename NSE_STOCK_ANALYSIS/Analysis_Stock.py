import pandas as pd
from nsepy import get_history
from datetime import date
import scipy.stats as st
import datetime as dt

def industry_symbols_history(symbols,x,y):
    valid_symbols=[]
    try:
        df_names=[]
        symbol=[]
        for i in symbols:
            df_names.append('data_'+i)

        for s in symbols:
            symbol.append(get_history(symbol=s,start=x,end=y))
            valid_symbols.append(s)
            
    except:
        print("Not Valid Symbol")

    dict_symbols=dict(zip(valid_symbols,symbol))
    
    return(dict_symbols)


def calculate_symbols_mean(dict_symbols):
    d=pd.DataFrame()
    for i in list(dict_symbols.keys()):
        d[i]=dict_symbols[i]["Close"]
    stock_mean=d.mean()
    return(d,stock_mean)
 
def calculate_AP_LP_HP(d,stock_mean):
    d_return,d_sd,mean,Pre_Close,all_low,all_high=[],[],[],[],[],[]
    
    for col in d:
        a=d[col].pct_change()
        d_return.append(a)
        d_Return=pd.DataFrame(d_return)
        d_Return=d_Return.T
        
    for col in d_Return:
        sd =d_Return[col].std()
        m=d_Return[col].mean()
        d_sd.append(sd)
        mean.append(m)

    z=st.norm.ppf(.95)
    #z1=st.norm.ppf(.99)
    
    for col in d:
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

    return(df)

symbols=['HINDUNILVR','RELIANCE','Titan Company','SUNPHARMA','TCS','MINDTREE','PERSISTENT','ICICIBANK','SBIN',
        'TATACOMM','CIPLA','HDFC']
Bank_symbols=["ICICIBANK","HDFCBANK","SBIN","YESBANK","INDUSINDBK","BANKBARODA","PNB"]
FMCG_symbols=["HINDUNILVR","BRITANNIA","MARICO","DABUR","COLPAL","GILLETTE","ZYDUSWELL","PGHL","ITC","NESTLEIND","VBL","UBL"]
IT_symbols=["TCS","MINDTREE","WIPRO","INFY","PERSISTENT","HCLTECH"]
Pharma_symbols=["CIPLA","SUNPHARMA","DIVISLAB","DRREDDY"]

dict_symbols=industry_symbols_history(Bank_symbols,x=dt.datetime(2021,1,1),y=dt.datetime(2022,5,31))
d,stock_mean= calculate_symbols_mean(dict_symbols)
df_AP_LP_HP=calculate_AP_LP_HP(d,stock_mean)
df_AP_LP_HP
