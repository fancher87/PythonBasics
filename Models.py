import numpy as np
from sklearn import datasets
import pandas as pd
from matplotlib import pyplot as plt
from scipy.stats import linregress



#plot x by y 
x = df['col1']
y = df['col2']
plt.scatter(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.show

#build simple linear regression model and assign stats 
(slope, intercept, rvalue, pvalue, stderr) = linregress(x, y)



#classification
import sklearn as sk
from sklearn.linear_model import LogisticRegression

LR = LogisticRegression(random_state=0, solver='lbfgs', multi_class='ovr').fit(X, y)


#support vector machines -- for classification with AND non-linear functions
import sklearn as sk
from sklearn import svm


#random forests 
import sklearn as sk
from sklearn.ensemble import RandomForestClassifier

RF = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)
RF.fit(X, y)
RF.predict(X.iloc[460:,:])
round(RF.score(X,y), 4)



#neural networks
import sklearn as sk
from sklearn.neural_network import MLPClassifier

NN = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
NN.fit(X, y)
NN.predict(X.iloc[460:,:])
round(NN.score(X,y), 4)
