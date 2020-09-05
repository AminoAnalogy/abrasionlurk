#!/usr/bin/env python
# coding: utf-8

# In[ ]:


companies = ['ABBV', 'AGN', 'JNJ', 'LLY', 'MRK', 'MYL', 'PRGO', 'PFE', 'ZTS']
assets = []
liabilities = []
equity = []
demo = '31fa1a9122c9b0d18024b5eb2d9ef148'

import requests

for company in companies:
    Balance_Sheet = requests.get(f"https://financialmodelingprep.com/api/v3/financials/balance-sheet-statement/{company}?period=quarter&apikey={demo}")

    Balance_Sheet = Balance_Sheet.json()
    
    asset_i = Balance_Sheet['financials'][0]['Total assets']
    assets.append(asset_i)

    liabilities_i = Balance_Sheet['financials'][0]['Total liabilities']
    liabilities.append(liabilities_i)

    equity_i = Balance_Sheet['financials'][0]['Total shareholders equity']
    equity.append(equity_i)


# In[ ]:


import plotly.graph_objects as go

firms = companies
#companies contains our list of firms e.g. ['ABBV', 'AGN'..]

fig = go.Figure(data=[
    go.Bar(name='Assets', x=companies, y=assets ),
    go.Bar(name='Liabilities', x=companies, y=liabilities),
    go.Bar(name='Equity', x=companies, y=equity)
])

fig.update_layout(barmode='stack',title = 'Balance Sheet Latest Quarter')
fig.show()


# In[ ]:




