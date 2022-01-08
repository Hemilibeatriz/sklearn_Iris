# -*- coding: utf-8 -*-
"""Cópia de TreinamentoeTeste.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Sdj1Iq_PSRBMqwjkpvQQNJ-aUeE72AiC
"""

from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.datasets import load_iris

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

X, y = load_iris(return_X_y=True)

print("Quantidade dos dados: ", X.shape)

#Separa os dados em 75% para treino e 25% para teste
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                     random_state=1)
print("Quantidade dos dados de treino: ", X_train.shape)
print("Quantidade dos dados de teste: ", X_test.shape)

clf = MLPClassifier(max_iter=300).fit(X_train, y_train)

clf.predict(X_test)
accuracy_score(clf.predict(X_test), y_test)

import numpy as np
from sklearn.model_selection import cross_val_score

scores = cross_val_score(clf, X, y, cv=5)
print(scores)
print('A média é %0.2f e o desvio é %0.2f' % (np.mean(scores), np.std(scores)))

