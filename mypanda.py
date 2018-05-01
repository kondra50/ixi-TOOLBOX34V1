import pandas as pd
import datetime
# import pandas.io.data as web
import pandas_datareader as dr

import matplotlib.pyplot as plt
from matplotlib import style

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2015, 8, 22)
df = dr.DataReader("XOM", "yahoo", start, end)
print(df.head())
style.use('fivethirtyeight')
df['Volume'].plot()
plt.legend()
plt.show()