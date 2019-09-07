import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import preprocessing,svm
import pandas as pd

df=pd.read_csv('breast-cancer-wisconsin.csv')
df.replace('?',-99999,inplace=True)

df.drop(['id'],1,inplace=True)
X=np.array(df.drop('class',1))
y=np.array(df['class'])

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
c=svm.SVC()
c.fit(X_train,y_train)
accuracy=c.score(X_test,y_test)
print(accuracy)

