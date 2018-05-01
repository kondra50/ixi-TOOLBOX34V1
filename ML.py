import pandas as pd
import quandl as q
import math,numpy as np
from sklearn import preprocessing
from sklearn import cross_validation
from sklearn import svm
from sklearn.linear_model import LinearRegression

df=q.get("WIKI/GOOGL")
#df=q.get("FRED/GDP")
df = df[['Adj. Open',  'Adj. High',  'Adj. Low',  'Adj. Close', 'Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Close'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

forecast_col = 'Adj. Close'
df.fillna(value=-99999, inplace=True)
forecast_out = int(math.ceil(0.01 * len(df)))
df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)
print(df.head())

X = np.array(df.drop(['lable'], 1))
Y = np.array(df['lable'])

X = preprocessing.scale(X)
X = X[:- forecast_out+1]
df.dropna(inplace=True)

Y = np.array(df['lable'])
print(len(X),len(Y))