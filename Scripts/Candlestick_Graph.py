#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import requests
import json
from datetime import datetime


# In[6]:


demo = '31fa1a9122c9b0d18024b5eb2d9ef148'
quote = 'AAPL'
days = '20'

def candlestick(quote, days):
    r= requests.get(f"https://financialmodelingprep.com/api/v3/historical-price-full/{quote}?timeseries={days}&apikey={demo}")
    r = r.json()

    ourdata = r['historical']
    df = pd.DataFrame.from_dict(ourdata)
    
    fig = go.Figure(data=[go.Candlestick(x=df['date'],
        open = df['open'],
        high = df['high'],
        low = df['low'],
        close = df['close'])])
    #below only needed if layout required
    fig.update_layout(
    title = quote + ' stock price for the last '+ str(days) +'days',
    yaxis_title= quote +'price',
    )
    fig.show()
                                       
                                      
candlestick(quote,days)


# In[ ]:



d = d[0]

incomeinitial = pd.DataFrame(list(d.items()),columns=['items','value'])
incomeinitial 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




