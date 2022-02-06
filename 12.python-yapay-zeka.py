from sklearn import datasets
"""
iris = datasets.load_iris()

giris = iris.feature_names
cikislar = iris.target_names

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size = 0.4)

from sklearn.naive_bayes import GaussianNB

bayes = GaussianNB()

bayes.fit(x_train, y_train)

y_tahmin = bayes.predict(x_test)

print("Olması gereken:", y_test)
print("Tahmin edilen:", y_tahmin)

from sklearn import metrics

print("Doğruluk / Başarı:", metrics.accuracy_score(y_test, y_tahmin))
"""
bc = datasets.load_breast_cancer()

from sklearn.model_selection import train_test_split
import numpy as np

x_train, x_test, y_train, y_test = train_test_split(bc.data, bc.target, test_size = 0.4)

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=5, metric='euclidean')

knn.fit(x_train, np.ravel(y_train))

y_tahmin = knn.predict(x_test)

print("Olması gereken:", y_test)
print("Tahmin edilen:", y_tahmin)

from sklearn.metrics import confusion_matrix
from sklearn import metrics

matris = confusion_matrix(y_test, y_tahmin)
dogruluk = metrics.accuracy_score(y_test, y_tahmin)
