#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import bs4 as bs
import requests
import pandas as pd
 

resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
soup = bs.BeautifulSoup(resp.text, 'lxml')
table = soup.find('table', {'class': 'wikitable sortable'})

print(table.findAll('tr')[1:])


# In[ ]:


tickers = []
industries = []

for row in table.findAll('tr')[1:]:
    ticker = row.findAll('td')[0].text
    #fourth element is the sector
    industry = row.findAll('td')[4].text

    tickers.append(ticker)
    industries.append(industry)

tickers = list(map(lambda s: s.strip(), tickers))
industries = list(map(lambda s: s.strip(), industries))

print(tickers)


# In[ ]:


tickerdf = pd.DataFrame(tickers,columns=['ticker'])
sectordf = pd.DataFrame(industries,columns=['industry'])

tickerdf.dtypes


# In[ ]:


tickerandsector = pd.concat([tickerdf, sectordf], axis=1,)
print(tickerandsector)


# In[ ]:


filtersector = tickerandsector.loc[tickerandsector['industry'] == 'Pharmaceuticals']

listoftickers =  filtersector['ticker'].tolist()
print(listoftickers)

