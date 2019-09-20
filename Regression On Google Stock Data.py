import pandas as pd
import math
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import preprocessing, svm
from sklearn.linear_model import LinearRegression

df=pd.read_csv('goog.csv',parse_dates=True,index_col=0)
df=df[['Open','High','Low','Adj Close','Volume']]

df['HL_PCT']=(df['High']-df['Adj Close'])/df['Adj Close']*100
df['PCT_change']=(df['Adj Close']-df['Open'])/df['Open']*100

df=df[['Adj Close','HL_PCT','PCT_change','Volume']]

forecast_co='Adj Close'
df.fillna(-99999,inplace=True)
forecast_out=int(math.ceil(0.01*len(df)))
df['label']=df[forecast_co].shift(-forecast_out)
df.dropna(inplace=True)

X=np.array(df.drop(['label'],1))
y=np.array(df['label'])
X=preprocessing.scale(X)
y=np.array(df['label'])

X_train, X_test, y_train, y_test= train_test_split(X,y,test_size=0.2)
c=LinearRegression()
c.fit(X_train,y_train)
accuracy=c.score(X_test,y_test)
print(accuracy)
