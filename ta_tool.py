#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json
response_API = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&month=2009-01&outputsize=full&apikey=demo')
print(response_API.status_code)
print(response_API.text)
parse_json = json.loads(response_API.text)
parse_json
timeseriesdata=parse_json["Time Series (5min)"]
#timeseriesdata
import pandas as pd
import numpy as np
from pandas.io.json import json_normalize

date=[]
close=[]
open=[]
high=[]
low=[]
volume=[]

date =timeseriesdata.keys()
for td in timeseriesdata:
    open.append(timeseriesdata[td]["1. open"])
    high.append(timeseriesdata[td]["2. high"])
    low.append(timeseriesdata[td]["3. low"])
    close.append(timeseriesdata[td]["4. close"])
    volume.append(timeseriesdata[td]["5. volume"])

#print(close)
data = pd.DataFrame([date,open,high,low,close,volume]).T
data.rename(columns = {0:'date',1:'open',2:'high',3:'low',4:'close',5:'volume'}, inplace = True)
data['open'] = data['open'].astype(float)
data['high'] = data['high'].astype(float)
data['low'] = data['low'].astype(float)
data['close'] = data['close'].astype(float)
data['volume'] = data['volume'].astype(float)

data.set_index('date', inplace=True)
data.info()

print(data)
df=data[['close']]

sma = df.rolling(window=20).mean().dropna()
rstd = df.rolling(window=20).std().dropna()

upper_band = sma + 2 * rstd
lower_band = sma - 2 * rstd

upper_band = upper_band.rename(columns={'close': 'upper'})
lower_band = lower_band.rename(columns={'close': 'lower'})

bb = df.join(upper_band).join(lower_band)
bb = bb.dropna()

bb.info()

buyers = bb[bb['close'] <= bb['lower']]
sellers = bb[bb['close'] >= bb['upper']]

# Plotting

import plotly.io as pio
import plotly.graph_objects as go

pio.templates.default = "plotly_dark"

fig = go.Figure()
fig.add_trace(go.Scatter(x=lower_band.index, 
                         y=lower_band['lower'], 
                         name='Lower Band', 
                         line_color='rgba(173,204,255,0.2)'
                        ))
fig.add_trace(go.Scatter(x=upper_band.index, 
                         y=upper_band['upper'], 
                         name='Upper Band', 
                         fill='tonexty', 
                         fillcolor='rgba(173,204,255,0.2)', 
                         line_color='rgba(173,204,255,0.2)'
                        ))
fig.add_trace(go.Scatter(x=df.index, 
                         y=df['close'], 
                         name='close', 
                         line_color='#636EFA'
                        ))
fig.add_trace(go.Scatter(x=sma.index, 
                         y=sma['close'], 
                         name='SMA', 
                         line_color='#FECB52'
                        ))
fig.add_trace(go.Scatter(x=buyers.index, 
                         y=buyers['close'], 
                         name='Buyers', 
                         mode='markers',
                         marker=dict(
                             color='#00CC96',
                             size=10,
                             )
                         ))
fig.add_trace(go.Scatter(x=sellers.index, 
                         y=sellers['close'], 
                         name='Sellers', 
                         mode='markers', 
                         marker=dict(
                             color='#EF553B',
                             size=10,
                             )
                         ))
fig.show()

fig = go.Figure(data=[go.Candlestick(x=data.index,
                       open=data['open'], high=data['high'],
                       low=data['low'], close=data['close'])])

fig.show()


# In[ ]:




