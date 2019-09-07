import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn import svm

digits=datasets.load_digits()
c=svm.SVC(gamma=0.01,C=100)
print(len(digits.data))

x,y = digits.data[:-10],digits.target[:-10]
c.fit(x,y)
print(c.predict(digits.data[-1:]))
plt.imshow(digits.images[-1],cmap=plt.cm.gray_r,interpolation='nearest')
plt.show()
