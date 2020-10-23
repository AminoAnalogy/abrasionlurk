#!/usr/bin/env python
# coding: utf-8

# # Sharpe Ratio and Portfolio Values

# In[8]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from datetime import datetime


# In[11]:


from pandas_datareader import data as pdr


# In[64]:


import yfinance as yf
yf.pdr_override()
#voo,aapl,znga,dis,tsla,brkb,dal,jll,qqq,su,gm,vgt,bio,rya,btc,eth
voo = pdr.get_data_yahoo("VOO", start="2019-01-01", end="2020-10-22")
aapl = pdr.get_data_yahoo("AAPL", start="2019-01-01", end="2020-10-22")
znga = pdr.get_data_yahoo("ZNGA", start="2019-01-01", end="2020-10-22")
dis = pdr.get_data_yahoo("DIS", start="2019-01-01", end="2020-10-22")
tsla = pdr.get_data_yahoo("TSLA", start="2019-01-01", end="2020-10-22")
brkb = pdr.get_data_yahoo("BRK-B", start="2019-01-01", end="2020-10-22")
dal = pdr.get_data_yahoo("DAL", start="2019-01-01", end="2020-10-22")
jll = pdr.get_data_yahoo("JLL", start="2019-01-01", end="2020-10-22")
qqq = pdr.get_data_yahoo("QQQ", start="2019-01-01", end="2020-10-22")
su = pdr.get_data_yahoo("SU", start="2019-01-01", end="2020-10-22")
gm = pdr.get_data_yahoo("GM", start="2019-01-01", end="2020-10-22")
vgt = pdr.get_data_yahoo("VGT", start="2019-01-01", end="2020-10-22")
bio = pdr.get_data_yahoo("BIO", start="2019-01-01", end="2020-10-22")
rya = pdr.get_data_yahoo("RYAAY", start="2019-01-01", end="2020-10-22")
btc = pdr.get_data_yahoo("BTC-USD", start="2019-01-01", end="2020-10-22")
eth = pdr.get_data_yahoo("ETH-USD", start="2019-01-01", end="2020-10-22")


# In[ ]:





# In[ ]:





# In[65]:


voo.to_csv('VOO_CLOSE')
aapl.to_csv('AAPL_CLOSE')
znga.to_csv('ZNGA_CLOSE')
dis.to_csv('DIS_CLOSE')
tsla.to_csv('TSLA_CLOSE')
brkb.to_csv('BRK-B_CLOSE')
dal.to_csv('DAL_CLOSE')
jll.to_csv('JLL_CLOSE')
qqq.to_csv('QQQ_CLOSE')
su.to_csv('SU_CLOSE')
gm.to_csv('GM_CLOSE')
vgt.to_csv('VGT_CLOSE')
bio.to_csv('BIO_CLOSE')
rya.to_csv('RYAAY_CLOSE')
btc.to_csv('BTC-USD_CLOSE')
eth.to_csv('ETH-USD_CLOSE')
#voo,aapl,znga,dis,tsla,brkb,dal,jll,qqq,su,gm,vgt,bio,rya,btc,eth


# In[ ]:


# aapl.columns[5]


# In[66]:


znga


# In[67]:


znga.iloc[0]['Adj Close']


# In[ ]:


znga


# In[68]:


for stock_df in (voo,aapl,znga,dis,tsla,brkb,dal,jll,qqq,su,gm,vgt,bio,rya,btc,eth):
    stock_df['Normed Return'] = stock_df['Adj Close']/stock_df.iloc[0]['Adj Close']


# In[69]:


for stock_df,allo in zip([voo,aapl,znga,dis,tsla,brkb,dal,jll,qqq,su,gm,vgt,bio,rya,btc,eth],[.0625,.0625,.0625,.0625,.0625,.0625,.0625,.0625,.0625,.0625,.0625,.0625,.0625,.0625,.0625,.0625]):
    stock_df['Allocation'] = stock_df['Normed Return']*allo


# In[70]:


znga.tail()


# In[ ]:





# ## Normalize Prices
# 
# This is the same as cumulative daily returns

# In[71]:


for stock_df in [voo,aapl,znga,dis,tsla,brkb,dal,jll,qqq,su,gm,vgt,bio,rya,btc,eth]:
    stock_df['Position Values'] = stock_df['Allocation']*4000


# In[72]:


aapl


# In[ ]:





# In[73]:


portfolio_val = pd.concat([voo['Position Values'],aapl['Position Values'],
                                                  znga['Position Values'],
                                                  dis['Position Values'],
                                                  tsla['Position Values'],
                                                  brkb['Position Values'],
                                                  dal['Position Values'],
                                                  jll['Position Values'], 
                                                  qqq['Position Values'],
                                                  su['Position Values'],
                                                  gm['Position Values'],
                                                  vgt['Position Values'],
                                                  bio['Position Values'],                                                    
                                                  rya['Position Values'],
                                                  btc['Position Values'], 
                                                  eth['Position Values']], axis=1,)

                                                    





# In[74]:


portfolio_val.head()


# In[ ]:


#voo,aapl,znga,dis,tsla,brkb,dal,jll,qqq,su,gm,vgt,bio,rya,btc,eth


# In[ ]:


portfolio_val.head()


# In[76]:


portfolio_val.columns = ['VOO Pos','AAPL Pos','ZNGA Pos','DIS Pos','TSLA Pos','BRK-B Pos'
                         ,'DAL Pos','JLL Pos','QQQ Pos','SU Pos','GM Pos','VGT Pos',
                         'BIO Pos','RYAAY Pos','BTC-USD Pos','ETH-USD Pos']


# In[ ]:


'''brkb.to_csv('BRK-B_CLOSE')
dal.to_csv('DAL_CLOSE')
jll.to_csv('JLL_CLOSE')
qqq.to_csv('QQQ_CLOSE')
su.to_csv('SU_CLOSE')
gm.to_csv('GM_CLOSE')
vgt.to_csv('VGT_CLOSE')
bio.to_csv('BIO_CLOSE')
rya.to_csv('RYAAY_CLOSE')
btc.to_csv('BTC-USD_CLOSE')
eth.to_csv('ETH-USD_CLOSE')
'''


# In[77]:


portfolio_val.head()


# In[78]:


portfolio_val['Total Pos'] = portfolio_val.sum(axis=1)


# In[79]:


portfolio_val.tail()


# In[80]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[81]:


portfolio_val['Total Pos'].plot(figsize=(10,8))
plt.title('Total Portfolio Value')


# In[82]:


portfolio_val.drop('Total Pos',axis=1).plot(kind='line')


# In[83]:


portfolio_val.tail()


# ## Total Portfolio Value

# # Portfolio Statistics
# ### Daily Returns

# In[84]:


portfolio_val['Daily Return'] = portfolio_val['Total Pos'].pct_change(1)


# In[ ]:


### Cumulative Return


# In[86]:


cum_ret = 100 * (portfolio_val['Total Pos'][-1]/portfolio_val['Total Pos'][0] -1 )
print('Our return was {} percent!'.format(cum_ret))


# ### Avg Daily Return

# In[87]:


portfolio_val['Daily Return'].mean()


# ### Std Daily Return

# In[88]:


portfolio_val['Daily Return'].std()


# In[89]:


portfolio_val['Daily Return'].plot(kind='hist', bins=20, figsize=(10,8))


# # Sharpe Ratio
# 
# The Sharpe Ratio is a measure for calculating risk-adjusted return, and this ratio has become the industry standard for such calculations. 
# 
# Sharpe ratio = (Mean portfolio return − Risk-free rate)/Standard deviation of portfolio return
# 
# The original Sharpe Ratio
# 
# Annualized Sharpe Ratio = K-value * SR
# 
# K-values for various sampling rates:
# 
# * Daily = sqrt(252)
# * Weekly = sqrt(52)
# * Monthly = sqrt(12)
# 
# Since I'm based in the USA, I will use a very low risk-free rate (the rate you would get if you just put your money in a bank, its currently very low in the USA, let's just say its ~0% return). If you are in a different country with higher rates for your trading currency, you can use this trick to convert a yearly rate with a daily rate:
# 
# daily_rate = ((1.0 + yearly_rate)**(1/252))-1
# 
# Other values people use are things like the 3-month treasury bill or [LIBOR](http://www.investopedia.com/terms/l/libor.asp).
# 
# Read more: Sharpe Ratio http://www.investopedia.com/terms/s/sharperatio

# In[90]:


SR = portfolio_val['Daily Return'].mean()/portfolio_val['Daily Return'].std()


# In[91]:


SR


# In[92]:


ASR = (252**0.5)*SR


# In[93]:


ASR


# In[94]:


portfolio_val['Daily Return'].std()


# In[95]:


portfolio_val['Daily Return'].mean()


# In[96]:


portfolio_val['Daily Return'].plot(kind='kde')


# In[97]:


#voo,aapl,znga,dis,tsla,brkb,dal,jll,qqq,su,gm,vgt,bio,rya,btc,eth

voo['Adj Close'].pct_change(1).plot(kind='kde')
aapl['Adj Close'].pct_change(1).plot(kind='kde')
znga['Adj Close'].pct_change(1).plot(kind='kde')
dis['Adj Close'].pct_change(1).plot(kind='kde')
tsla['Adj Close'].pct_change(1).plot(kind='kde')
brkb['Adj Close'].pct_change(1).plot(kind='kde')
dal['Adj Close'].pct_change(1).plot(kind='kde')
jll['Adj Close'].pct_change(1).plot(kind='kde')
qqq['Adj Close'].pct_change(1).plot(kind='kde')
su['Adj Close'].pct_change(1).plot(kind='kde')
gm['Adj Close'].pct_change(1).plot(kind='kde')
vgt['Adj Close'].pct_change(1).plot(kind='kde')
bio['Adj Close'].pct_change(1).plot(kind='kde')
rya['Adj Close'].pct_change(1).plot(kind='kde')
btc['Adj Close'].pct_change(1).plot(kind='kde')
eth['Adj Close'].pct_change(1).plot(kind='kde')



# In[98]:


import numpy as np
np.sqrt(252)* (np.mean(.001-0.0002)/.001)


# # Great Job!
