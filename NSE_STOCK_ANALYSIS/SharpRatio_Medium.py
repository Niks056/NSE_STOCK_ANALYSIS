import pandas as pd
from nsepy import get_history
from datetime import date
import matplotlib.pyplot as plt
import datetime as dt


x=dt.datetime(2018,1,1)
y = dt.datetime(2020, 5, 8)

data_SBI =  get_history(symbol="SBIN", start=x, end=y)
data_ICICI=get_history(symbol='WIPRO',start=x,end=y)
data_Hdfc=get_history(symbol="TVSMOTOR",start=x, end=y)
data_YES = get_history(symbol="ITC", start=x, end=y)

data_SBI['SBI_Return']=data_SBI['Close'].pct_change()
data_ICICI['ICICI_Return']=data_ICICI['Close'].pct_change()
data_Hdfc['HDFC_Return']=data_Hdfc['Close'].pct_change()
data_YES['YES_Return']=data_YES['Close'].pct_change()

c=pd.DataFrame()
c['SBI_Close']=data_SBI['Close']
c['ICICI_Close']=data_ICICI['Close']
c['HDFC_Close']=data_Hdfc['Close']
c['YES_Close']=data_YES['Close']
co1=c[['SBI_Close','ICICI_Close']].corr()
co2=c[['SBI_Close','HDFC_Close']].corr()
co3=c[['SBI_Close','YES_Close']].corr()
co4=c[['ICICI_Close','HDFC_Close']].corr()
co5=c[['YES_Close','HDFC_Close']].corr()
co6=c[['ICICI_Close','YES_Close']].corr()




for data_SBI in (data_SBI, data_ICICI, data_Hdfc, data_YES):
  data_SBI['Norm return'] = data_SBI['Close'] / data_SBI.iloc[0]['Close']


for data_SBI, allocation in zip((data_SBI, data_ICICI, data_Hdfc, data_YES),[.35,.25,.2,.2]):
  data_SBI['Allocation'] = data_SBI['Norm return'] * allocation


for data_SBI in (data_SBI, data_ICICI,data_Hdfc, data_YES):
   data_SBI['Position'] = data_SBI['Allocation']*10000


column_names = ["a", "b", "c","d"]
portf_val=pd.DataFrame(columns=column_names)
all_pos = [data_SBI['Position'], data_ICICI['Position'], data_Hdfc['Position'], data_YES['Position']]
portf_val = pd.concat(all_pos, axis=1)
portf_val.columns =['SBI Pos','ICICI Pos','HDFC Pos','YES Pos']
portf_val['Total Pos'] = portf_val.sum(axis=1)
portf_val.head()

#To plot Graph
plt.style.use('fivethirtyeight')
portf_val['Total Pos'].plot(figsize=(10,8))
portf_val.drop('Total Pos', axis=1).plot(figsize=(10,8))


cumulative_return = 100 * ( portf_val [ 'Total Pos' ] [-1 ] / portf_val [ 'Total Pos'] [ 0 ] -1)
print('Your cumulative return was {:.2f}% '.format(cumulative_return))

portf_val['Daily Return'] = portf_val['Total Pos'].pct_change(1)
Sharpe_Ratio = portf_val['Daily Return'].mean() / portf_val['Daily Return'].std()

A_Sharp_Ratio= (252**0.5)*Sharpe_Ratio