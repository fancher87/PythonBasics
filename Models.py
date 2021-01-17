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

