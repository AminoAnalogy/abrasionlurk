import numpy as np  # array operations
import pandas as pd  # time series management
import matplotlib.pyplot as plt  # standard plotting library
from pylab import plt
plt.style.use('ggplot')
# put all plots in the notebook itself

# symbol = 'AAPL.O'
# symbol = 'MSFT.O'
symbol = '.SPX'

sma_list = range(1,253)
max_arets=None
max_astds=None
best_short_SMA = None
best_long_SMA = None

file_data = pd.read_csv('http://hilpisch.com/tr_eikon_eod_data.csv',
                           index_col=0, parse_dates=True)[symbol].dropna()
count = 0
for short_SMA in sma_list:
    short_SMA_str = 'SMA'+str(short_SMA)
    for long_SMA in sma_list:
        if short_SMA >= long_SMA:
            continue
        count += 1
        long_SMA_str = 'SMA'+str(long_SMA)
        
        data = pd.DataFrame(file_data)

        # data.tail()  # the final five rows

        data[short_SMA_str] = data[symbol].rolling(window=short_SMA).mean()
        data[long_SMA_str] = data[symbol].rolling(window=long_SMA).mean()
        data.dropna(inplace=True)  # drop rows with NaN values

        # data[[symbol, 'SMA42', 'SMA252']].plot(figsize=(10, 6));

        # vectorized evaluation of the trading condition/signal generation
        data['position'] = np.where(data[short_SMA_str] > data[long_SMA_str], 1, -1)

        # data[[symbol, 'position']].plot(subplots=True, figsize=(10, 6))
        # plt.ylim(-1.1, 1.1)  # adjust y-axis limits

        # vectorized calculation of log returns
        data['market'] = np.log(data[symbol] / data[symbol].shift(1))

        # vectorized calculation of strategy returns
        
        strategy_str = "strategy_"+str(short_SMA)+"_"+str(long_SMA)
        data[strategy_str] = data['position'].shift(1) * data['market']

        # data[['market', 'strategy']].cumsum().apply(np.exp).tail()

        # data[['market', 'strategy']].cumsum().apply(np.exp).plot(figsize=(10, 6));

        arets = data[['market', strategy_str]].mean() * 252  # annualized returns
        # arets

        astds = data[['market', strategy_str]].std() * 252 ** 0.5  # annualized volatility
        # astds
        
        if max_arets is None or arets[strategy_str] > max_arets:
            max_arets = arets[strategy_str]
            max_astds = astds[strategy_str]
            best_short_SMA = short_SMA
            best_long_SMA = long_SMA
            print("Best SMA Pair : {} {}".format(best_short_SMA,best_long_SMA))

print("Tested {} combinations".format(count))

data = pd.DataFrame(file_data)

data['SMAshort'] = data[symbol].rolling(window=best_short_SMA).mean()
data['SMAlong'] = data[symbol].rolling(window=best_long_SMA).mean()
data.dropna(inplace=True)  # drop rows with NaN values

# data[[symbol, 'SMA42', 'SMA252']].plot(figsize=(10, 6));

# vectorized evaluation of the trading condition/signal generation
data['position'] = np.where(data['SMAshort'] > data['SMAlong'], 1, -1)

# data[[symbol, 'position']].plot(subplots=True, figsize=(10, 6))
# plt.ylim(-1.1, 1.1)  # adjust y-axis limits

# vectorized calculation of log returns
data['market'] = np.log(data[symbol] / data[symbol].shift(1))

# vectorized calculation of strategy returns

strategy_str = 'strategy'+'[,'+str(best_short_SMA)+','+str(best_long_SMA)+']'
data[strategy_str] = data['position'].shift(1) * data['market']

# data[['market', 'strategy']].cumsum().apply(np.exp).tail()

data[['market', strategy_str]].cumsum().apply(np.exp).plot(figsize=(10, 6));