#!/usr/bin/env python
# coding: utf-8

# In[19]:


import requests
demo = '31fa1a9122c9b0d18024b5eb2d9ef148'
def valuecompany(quote):
    #Latest dividend of the company
    dividend = requests.get(f'https://financialmodelingprep.com/api/v3/financials/income-statement/{quote}?apikey={demo}')
    dividend = dividend.json()
    dividend = dividend['financials']
    Dtoday = float(dividend[0]['Dividend per Share'])
    print(Dtoday)
    metrics = requests.get(f'https://financialmodelingprep.com/api/v3/company-key-metrics/{quote}?apikey={demo}')
    metrics = metrics.json()

    ROE = float(metrics['metrics'][0]['ROE'])
    payout_ratio = float(metrics['metrics'][0]['Payout Ratio'])

    sustgrwothrate = ROE*(1-payout_ratio)
    print(sustgrwothrate)
    
    import pandas as pd
    #if you get an error after executing the code, try adding below:
    pd.core.common.is_list_like = pd.api.types.is_list_like

    import pandas_datareader.data as web
    import datetime

    start = datetime.datetime(2019, 7, 1)
    end = datetime.datetime(2020, 7, 1)

    Treasury = web.DataReader(['TB1YR'], 'fred', start, end)
    RF = float(Treasury.iloc[-1])
    RF = RF/100
     #Beta
    beta = requests.get(f'https://financialmodelingprep.com/api/v3/company/profile/{quote}?apikey={demo}')
    beta = beta.json()
    beta = float(beta['profile']['beta'])
    
    #Market Return
    start = datetime.datetime(2019, 7, 1)
    end = datetime.datetime(2020, 7, 1)

    SP500 = web.DataReader(['sp500'], 'fred', start, end)
    #Drop all Not a number values using drop method.
    SP500.dropna(inplace = True)

    SP500yearlyreturn = (SP500['sp500'].iloc[-1]/ SP500['sp500'].iloc[0])-1
   
    ke = RF+(beta*(SP500yearlyreturn - RF))
    print(ke)
    
    DDM = (Dtoday*(1+sustgrwothrate))/(ke-sustgrwothrate)
    print(DDM)
    return DDM


valuecompany('JNJ')


# In[20]:





# In[ ]:




