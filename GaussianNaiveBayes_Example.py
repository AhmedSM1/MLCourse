import numpy as np
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array([1, 1, 1, 2, 2, 2])

from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(X, Y)
GaussianNB()
clf.predict([[-0.8, -1]])
clf_pf = GaussianNB()
clf_pf.partial_fit(X, Y, np.unique(Y))

pred = clf_pf.predict([[-0.8, -1]])

from sklearn.metrics import accuracy_score
accuracy_score(X, pred)

