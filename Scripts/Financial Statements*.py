#!/usr/bin/env python
# coding: utf-8

# In[1]:


#https://www.youtube.com/watch?v=1Idq74JZQts&t=780s
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import requests
import json


# In[2]:


#used the old url that includes /financials/
quote = 'AAPL'
period = ''
def getfinancials(quote):
    r= requests.get(f"https://financialmodelingprep.com/api/v3/financials/income-statement/{quote}?period=quarter&apikey=31fa1a9122c9b0d18024b5eb2d9ef148")
    r = r.json()
    d = r['financials']
    count = 0
    for item in d:
        if count == 0:
            d = r['financials']
            d = d[0]
            incomeinitial = pd.DataFrame(list(d.items()),columns=['item','value'])
        count = count + 1
        if count > 5:  
            continue
        d = r['financials']
        d = d[count]   

        incomeinitial2 = pd.DataFrame(list(d.items()),columns=['item','value'])
        incomeinitial = incomeinitial.merge(incomeinitial2, on="item", how= 'left')

    incomeinitial.columns = incomeinitial.iloc[0]
    incomeinitial= incomeinitial[1:]
    incomeinitial
    cols = incomeinitial.columns
    cols = cols[1:]

    incomeinitial[cols]=incomeinitial[cols].apply(pd.to_numeric, errors='coerce')
    return incomeinitial
    
incomeinitial = getfinancials(quote)


# In[12]:


incomeinitial:[2]


# In[5]:


incomeinitial.info


# In[ ]:





# In[6]:


REV = incomeinitial[incomeinitial['date'] == 'Revenue'].iloc[0][1]
COGs = incomeinitial[incomeinitial['date'] == 'Cost of Revenue'].iloc[0][1]*-1
GrossProfit = incomeinitial[incomeinitial['date'] == 'Gross Profit'].iloc[0][1]
RD = incomeinitial[incomeinitial['date'] == 'R&D Expenses'].iloc[0][1]*-1
GA = incomeinitial[incomeinitial['date'] == 'SG&A Expense'].iloc[0][1]*-1
OperExp = incomeinitial[incomeinitial['date'] == 'Operating Expenses'].iloc[0][1]*-1
INT = incomeinitial[incomeinitial['date'] == 'Interest Expense'].iloc[0][1]*-1
EBT = incomeinitial[incomeinitial['date'] == 'Earnings before Tax'].iloc[0][1]
IncTax = incomeinitial[incomeinitial['date'] == 'Income Tax Expense'].iloc[0][1]*-1
NetInc = incomeinitial[incomeinitial['date'] == 'Net Income Com'].iloc[0][1]


# In[7]:


import plotly.graph_objects as go

fig = go.Figure(go.Waterfall(
    name = "20", orientation = "v",
    measure = ["relative", "relative", "total", "relative", "relative", "total", "relative", "total"],
    x = ["Revenue", "Cost of Revenue", "Gross Profit", "R&D Expenses", "SG&A Expense", "Operating Expenses", "Interest Expense", "Earnings before Tax", "Income Tax Expense", "Net Income Com"],
    textposition = "outside",
    text = [REV/1000, COGs/1000, GrossProfit/1000, RD/1000, GA/1000, OperExp/1000, INT/1000, EBT/1000, IncTax/1000, NetInc/1000],
    y = [REV, COGs, GrossProfit, RD, GA, OperExp, INT, EBT, IncTax, NetInc],
    connector = {"line":{"color":"rgba(63, 63, 63, 0.7)"}},
    decreasing = {"marker":{"color":"rgba(219, 64, 82, 0.7)"}},
    increasing = {"marker":{"color":"rgba(50, 171, 96, 0.7)"}},
    totals = {"marker":{"color":"rgba(55, 128, 192, 0.7)"}},
            
      
))

fig.update_layout(
        title = "Income Statement – Last Quarter",
        showlegend = False
)

fig.show()

    


# Just Playing After this

# In[15]:


import plotly.io as pio
pio.renderers


# In[16]:


import plotly.graph_objects as go
fig = go.Figure(
    data=[go.Bar(y=[2, 1, 3])],
    layout_title_text="A Figure Displayed with the 'svg' Renderer"
)
fig.show(renderer="svg")


# In[17]:



import plotly.graph_objects as go
import numpy as np
np.random.seed(1)

N = 100
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
sz = np.random.rand(N) * 30

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=x,
    y=y,
    mode="markers",
    marker=go.scatter.Marker(
        size=sz,
        color=colors,
        opacity=0.6,
        colorscale="Viridis"
    )
))

fig.show(renderer="svg")


# In[ ]:




