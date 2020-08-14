#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

import requests
import json

demo = '31fa1a9122c9b0d18024b5eb2d9ef148'
#pass sector and marketcap as arguments to limit the results
companies = requests.get(f'https://financialmodelingprep.com/api/v3/stock-screener?marketCapMoreThan=1000000000&sector=Technology&limit=100&apikey={demo}')
companies = companies.json()

technological_companies = []

for item in companies:
    technological_companies.append(item['symbol'])
print(technological_companies)


# In[ ]:



metrics= {}

for item in technological_companies:
    try:
        balancesheet = requests.get(f'https://financialmodelingprep.com/api/v3/balance-sheet-statement/{item}?apikey={demo}').json()
        incomestatemnt = requests.get(f'https://financialmodelingprep.com/api/v3/income-statement/{item}?&apikey={demo}').json()
        marketcap = requests.get(f'https://financialmodelingprep.com/api/v3/market-capitalization/{item}?apikey={demo}').json()
        marketcap = marketcap[0]['marketCap']
        companydata = requests.get(f'https://financialmodelingprep.com/api/v3/profile/{item}?apikey={demo}').json()
        latest_Annual_Dividend = companydata[0]['lastDiv']
        price = companydata[0]['price']


        balancesheet[0]
        current_ratio = balancesheet[0]['totalCurrentAssets'] / balancesheet[0]['totalCurrentLiabilities']
        debt_to_assets = balancesheet[0]['totalDebt'] / balancesheet[0]['totalAssets']
        debt_to_equity = balancesheet[0]['totalDebt'] / balancesheet[0]['totalStockholdersEquity']
        dividend_yield = latest_Annual_Dividend / price
        interest_coverage = incomestatemnt[0]['operatingIncome'] / incomestatemnt[0]['interestExpense']
        gross_profit_margin = (incomestatemnt[0]['revenue'] - incomestatemnt[0]['costOfRevenue'])/incomestatemnt[0]['revenue']
        #index one in below because we want to have equity at the beginning of the period. *4 if we want to annualize it is quarter revenue
        ROE = (incomestatemnt[0]['netIncome'] / ((balancesheet[0]['totalStockholdersEquity']+ balancesheet[1]['totalStockholdersEquity'])/2))
        price_to_sales = marketcap / (incomestatemnt[0]['revenue'])
        price_to_earnings = marketcap / (incomestatemnt[0]['netIncome']) 
        price_to_book = marketcap / balancesheet[0]['totalStockholdersEquity']
        ROA = (incomestatemnt[0]['netIncome']/balancesheet[0]['totalAssets'])

        metrics[item] = {}
        metrics[item]['ROA'] = ROA

        metrics[item]['ROE'] = ROE
        metrics[item]['Current Ratio'] = current_ratio
        metrics[item]['Debt to Assets'] = debt_to_assets
        metrics[item]['Debt to Equity'] = debt_to_equity
        metrics[item]['Dividend Yield'] = (dividend_yield*100)
        metrics[item]['Interest Coverage'] = interest_coverage
        metrics[item]['Gross Profit Margin'] = gross_profit_margin
        metrics[item]['Price to Sales'] = price_to_sales
        metrics[item]['Price to Earnings'] = price_to_earnings
        metrics[item]['Price to Book'] = price_to_book
    except:
        pass

print(metrics)


# In[ ]:


metrics


# In[ ]:


metrics_df = pd.DataFrame.from_dict(metrics, orient='index')
metrics_df = metrics_df.T
metrics_df['mean'] = metrics_df.mean(axis=1)


# In[ ]:


metrics_df


# In[ ]:


import matplotlib.pyplot as plt

plt.figure(figsize=(20,10))
x1 = metrics_df.columns
#in the 8 row we have Price To Sales data
y1 = metrics_df.iloc[8,]
plt.plot(x1, y1, label = "Price to Sales")

# line 2 points
x2 = metrics_df.columns
#in the 9 row we have Price To Earnings data:
y2 = metrics_df.iloc[9,]
# plotting the line 2 points 
plt.plot(x2, y2, label = "Price to Earnings")

# line 3 points
x3 = metrics_df.columns
#in the 10 row we have Price To Book data:
y3 = metrics_df.iloc[10,]
# plotting the line 2 points 
plt.plot(x3, y3, label = "Price to Book")

plt.xlabel('companies')
# Set the y axis label of the current axis.
plt.ylabel('')
# Set a title of the current axes.
plt.title('Plotting Key financial ratios')
# show a legend on the plot
plt.legend()
# Display a figure.
plt.tight_layout()
plt.show()


# In[ ]:


metrics_filter = metrics_df.T
metrics_filter[(metrics_filter['ROE'] > 0.2) & (metrics_filter['Current Ratio']> 1.09)]
mf1 = metrics_filter[(metrics_filter['ROE'] > 0.2) & (metrics_filter['Current Ratio']> 1.09)]


# In[ ]:


mf1


# In[ ]:



mf1['ROE']
mf1_roe = mf1['ROE']
mf1_roe


# In[ ]:


mf1.sort_values(by='Price to Sales', ascending=False)


# In[ ]:




