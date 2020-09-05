#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import pandas as pd

companies = []
demo = '31fa1a9122c9b0d18024b5eb2d9ef148'
exchange = 'nyse'

'''marketCapMoreThan & marketCapLowerThan : Number
betaMoreThan & betaLowerThan : Number
volumeMoreThan & volumeLowerThan : Number
dividendMoreThan & dividendLowerThan : Number
sector : Consumer Cyclical - Energy - Technology - Industrials - Financial Services - Basic Materials - Communication Services - Consumer Defensive - Healthcare - Real Estate - Utilities - Industrial Goods - Financial - Services - Conglomerates
Industry : Autos - Banks - Banks Diversified - Software - Banks Regional - Beverages Alcoholic - Beverages Brewers - Beverages Non-Alcoholic
exchange : nyse - nasdaq - amex - euronex - tsx - etf - mutual_fund
limit : Number'''

marketcap = str(1000000000)

url = (f'https://financialmodelingprep.com/api/v3/stock-screener?marketCapMoreThan={marketcap}&betaMoreThan=1&volumeMoreThan=10000&sector=Technology&exchange={exchange}&dividendMoreThan=0&limit=1000&apikey={demo}')

#get companies based on criteria defined about
screener = requests.get(url).json()


# In[ ]:


print(screener)


# In[ ]:


#add selected companies to a list
for item in screener:
    companies.append(item['symbol'])

#print(companies)

value_ratios ={}
#get the financial ratios
count = 0
for company in companies:
    try:
        if count <30:
            count = count + 1
            fin_ratios = requests.get(f'https://financialmodelingprep.com/api/v3/ratios/{company}?apikey={demo}').json()
            value_ratios[company] = {}
            value_ratios[company]['ROE'] = fin_ratios[0]['returnOnEquity']
            value_ratios[company]['ROA'] = fin_ratios[0]['returnOnAssets']
            value_ratios[company]['Debt_Ratio'] = fin_ratios[0]['debtRatio']
            value_ratios[company]['Interest_Coverage'] = fin_ratios[0]['interestCoverage']
            value_ratios[company]['Payout_Ratio'] = fin_ratios[0]['payoutRatio']
            value_ratios[company]['Dividend_Payout_Ratio'] = fin_ratios[0]['dividendPayoutRatio']
            value_ratios[company]['PB'] = fin_ratios[0]['priceToBookRatio']
            value_ratios[company]['PS'] = fin_ratios[0]['priceToSalesRatio']
            value_ratios[company]['PE'] = fin_ratios[0]['priceEarningsRatio']
            value_ratios[company]['Dividend_Yield'] = fin_ratios[0]['dividendYield']
            value_ratios[company]['Gross_Profit_Margin'] = fin_ratios[0]['grossProfitMargin']
            #more financials on growth:https://financialmodelingprep.com/api/v3/financial-growth/AAPL?apikey=demo
            growth_ratios = requests.get(f'https://financialmodelingprep.com/api/v3/financial-growth/{company}?apikey={demo}').json()
            value_ratios[company]['Revenue_Growth'] = growth_ratios[0]['revenueGrowth']
            value_ratios[company]['NetIncome_Growth'] = growth_ratios[0]['netIncomeGrowth']
            value_ratios[company]['EPS_Growth'] = growth_ratios[0]['epsgrowth']
            value_ratios[company]['RD_Growth'] = growth_ratios[0]['rdexpenseGrowth']

    except:
        pass
print(value_ratios)


# In[ ]:


DF = pd.DataFrame.from_dict(value_ratios,orient='index')
print(DF.head(4))


# In[ ]:


#criteria ranking
ROE = 1.2
ROA = 1.1
Debt_Ratio = -1.1
Interest_Coverage = 1.05
Dividend_Payout_Ratio = 1.01
PB = -1.10
PS = -1.05
Revenue_Growth = 1.25
Net_Income_Growth = 1.10


# In[ ]:


#mean to enable comparison across ratios
ratios_mean = []
for item in DF.columns:
	ratios_mean.append(DF[item].mean())

#divide each value in dataframe by mean to normalize values
DF = DF / ratios_mean


# In[ ]:


DF['ranking'] = DF['NetIncome_Growth']*Net_Income_Growth + DF['Revenue_Growth']*Revenue_Growth  + DF['ROE']*ROE + DF['ROA']*ROA + DF['Debt_Ratio'] * Debt_Ratio + DF['Interest_Coverage'] * Interest_Coverage + DF['Dividend_Payout_Ratio'] * Dividend_Payout_Ratio + DF['PB']*PB + DF['PS']*PS 


# In[ ]:


print(DF.sort_values(by=['ranking'],ascending=False))


# In[ ]:




