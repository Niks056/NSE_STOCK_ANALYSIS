import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import cmath


data =pd.read_csv("Spread_Analytics.csv")
data2=data
data2['Spread']=data2['Far Month']-data2['Near Month']
data2['m']=data2['Spread'].mean()
data2['avg_sd']=data2['Spread'].std()
data2['HR']=data2['m']+data2['avg_sd']
data2['LR']=data2['m']-data2['avg_sd']


plt.plot(data2['Spread'])
plt.plot(data2['m'])
plt.plot(data2['HR'])
plt.plot(data2['LR'])
data2.plot(x="Date",y=["Spread","HR","LR","m"])
