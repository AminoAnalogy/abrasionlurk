#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import pandas as pd

demo = '31fa1a9122c9b0d18024b5eb2d9ef148'

CF = requests.get(f'https://financialmodelingprep.com/api/v3/cash-flow-statement/AAPL?apikey={demo}').json()

#Create an empty dictionary 
CF_3Y = {}
IS = requests.get(f'https://financialmodelingprep.com/api/v3/income-statement/AAPL?apikey={demo}').json()


# In[ ]:


print(CF)


# In[ ]:


for item in CF:
    if count < 3:
        date = item['date']
        CF_3Y[date] = item
        #we add revenue as well to the dictionary since we need it to calculate the common-size cash flow
        CF_3Y[date]['Revenue'] = IS[count]['revenue']
        count += 1
print(CF_3Y)


# In[ ]:


CF_Common_Size = pd.DataFrame.from_dict(CF_3Y, orient='index')
CF_Common_Size = CF_Common_Size.T
print(CF_Common_Size)


# In[ ]:


Revenue = CF_Common_Size.iloc[-1]


# In[ ]:


CF_Common_Size = CF_Common_Size.iloc[5:-3,:]


# In[ ]:


CF_Common_Size = (CF_Common_Size/Revenue) * 100

#show as percentage:
pd.options.display.float_format = '{:.2f}%'.format
print(CF_Common_Size)


# In[ ]:




