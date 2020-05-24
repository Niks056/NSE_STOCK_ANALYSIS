import pandas as pd
from nsetools import Nse
from pprint import pprint  # just for neatness of display

nse= Nse()
print(nse)
q= nse.get_quote('MindTree')
# it's ok to use both upper or lower case for codes.
q1 = nse.get_quote('persistent')
q2= nse.get_quote('Cipla')
q3= nse.get_quote('Titan')
q4= nse.get_quote('Sunpharma')
q5= nse.get_quote('HDFC')
pprint(q)
keys =['dayLow', 'dayHigh', 'open']
MindTree = list( map(q.get, keys) )
Persistent=list(map(q1.get,keys))
Cipla = list( map(q2.get, keys) )
Titan=list(map(q3.get,keys))
sunpharma = list( map(q4.get, keys) )
Hdfc=list(map(q5.get,keys))
df_info=pd.DataFrame()
df_info['MindTree']=MindTree
df_info['Persistent']=Persistent
df_info['Cipla']=Cipla
df_info['Titan']=Titan
df_info['Sunpharma']=sunpharma
df_info['Hdfc']=Hdfc
df_info.rename(index={0:'dayLow',1:'dayHigh',2:'Open'}, inplace=True)
df_info=df_info.T
"""""
df_info['open']=q['open']
df_info['dayHigh']=q['dayHigh']
df_info['dayLow']=q['dayLow']
df_info['close']= q['closePrice']
"""


nse.is_valid_code('infy') # this should return True True
nse.is_valid_code('innnfy') # should return False False

nse.is_valid_index('cnx nifty') # should return True True
nse.is_valid_index('cnxnifty') # should return False False


nse.get_index_list()
nse.get_index_quote("nifty bank")
all_stock_codes = nse.get_stock_codes()
df_stock_codes=pd.DataFrame(all_stock_codes.items(), columns=['SYMBOL', 'NAME OF COMPANY'])

index_codes = nse.get_index_list()
pprint(index_codes)
df_index_codes=pd.DataFrame(index_codes)

adv_dec = nse.get_advances_declines()
pprint(adv_dec)

top_gainers = nse.get_top_gainers()
df_topgainers=pd.DataFrame(top_gainers)
df_topgainers_info=df_topgainers.loc[:,['symbol','openPrice','highPrice','ltp']]

top_losers = nse.get_top_losers()
df_toplosers=pd.DataFrame(top_losers)
df_toplosers_info=df_toplosers.loc[:,['symbol','openPrice','highPrice','ltp']]


a=nse.get_fno_lot_sizes()   #To get the lot size for future and option market
df_lot_size=pd.DataFrame(a.items(),columns=['fstock','Lot_size'])


""""
url = 'https://www.nseindia.com/content/indices/ind_nifty50list.csv'
s = requests.get(url).content
#df1= pd.read_csv(io.StringIO(s.decode('utf-8')))

#d=get_history(df1.INFY ,start=date(2020,1,1), end=date(2020,3,20))
#a= nse.get_quote(‘infy’ , as_json=True)

"""