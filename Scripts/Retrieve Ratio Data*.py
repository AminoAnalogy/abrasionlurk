#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

import requests
import json

import datetime as dt


# In[2]:


#quote = 'AAPL'
demo = '31fa1a9122c9b0d18024b5eb2d9ef148'


# In[15]:


def financialratios(quote):
    fr = requests.get(f"https://financialmodelingprep.com/api/v3/ratios/{quote}?apikey={demo}")
    fr = fr.json()
    ratios_df = fr[0]
    df = pd.DataFrame(ratios_df.items(),columns=['Ratio', quote])
    return df


# In[18]:



listofstocks= ['ZNGA','GM','WMT']
x = financialratios ('GOOGL') 

for item in listofstocks:
    y = financialratios(item) 
    x = x.merge(y, on='Ratio')


# In[64]:


x2 = x.drop([0])


# In[67]:


x


# In[ ]:




