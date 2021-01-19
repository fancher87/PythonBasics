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

#split data into testing and training set first 
from sklearn.model_selection import train_test_split

train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)


##################
# model options #
fit(X, y[, sample_weight])
#Fit linear model.
get_params([deep])
#Get parameters for this estimator.
predict(X)
#Predict using the linear model.
score(X, y[, sample_weight])
#Return the coefficient of determination  of the prediction.
set_params(**params)
#Set the parameters of this estimator.




#build simple linear regression model and assign stats 
(slope, intercept, rvalue, pvalue, stderr) = linregress(x, y)


#multiple regression 
from sklearn.linear_model import LinearRegression



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


#decision tree additional params
rom sklearn.tree import DecisionTreeClassifier

apply(X[, check_input])
# Return the index of the leaf that each sample is predicted as.
cost_complexity_pruning_path(X, y[, …])
# Compute the pruning path during Minimal Cost-Complexity Pruning.
decision_path(X[, check_input])
# Return the decision path in the tree.
fit(X, y[, sample_weight, check_input, …])
# Build a decision tree classifier from the training set (X, y).
get_depth()
# Return the depth of the decision tree.
get_n_leaves()
# Return the number of leaves of the decision tree.
get_params([deep])
# Get parameters for this estimator.
predict(X[, check_input])
# Predict class or regression value for X.
predict_log_proba(X)
# Predict class log-probabilities of the input samples X.
predict_proba(X[, check_input])
# Predict class probabilities of the input samples X.
score(X, y[, sample_weight])
# Return the mean accuracy on the given test data and labels.
set_params(**params)
# Set the parameters of this estimator.
