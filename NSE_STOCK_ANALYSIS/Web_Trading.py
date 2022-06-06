import pandas as pd
from nsetools import Nse
from pprint import pprint  # just for neatness of display

def day_high_low_open(symbols):
    nse= Nse()
    q=[]
    keys =['dayLow', 'dayHigh', 'open']
    for i in symbols:
        q.append(nse.get_quote(i))
    
    day_H_L_O=[]
    for i in range(0,len(q)):
        day_H_L_O.append(list(map(q[i].get,keys)))
        
    df_info=pd.DataFrame(day_H_L_O,index=symbols,columns=keys)
    return(df_info)
  
symbols=["MindTree","persistent","Cipla","Titan","Sunpharma","HDFC"]
df_info=day_high_low_open(symbols)
df_info


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
