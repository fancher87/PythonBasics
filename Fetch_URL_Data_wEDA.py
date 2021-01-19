import os
import tarfile
from six.moves import urllib

DOWNLOAD_ROOT = "https://domain" #this would normally be a git or other site 
DATA_PATH = os.path.join("dir", "subdir")
DATA_URL = DOWNLOAD_ROOT + "dir/subdir/file.tgz"

def fetch_data(data_url=DATA_URL, data_path=DATA_PATH):
    os.makedirs(data_path, exist_ok=True)
    tgz_path = os.path.join(data_path, "file.tgz")
    urllib.request.urlretrieve(data_url, tgz_path)
    data_tgz = tarfile.open(tgz_path)
    data_tgz.extractall(path=data_path)
    data_tgz.close()
    
    
fetch_data()



import pandas as pd 

def load_data(data_path=DATA_PATH):
  csv_path = os.path.join(data_path, "file.csv")
  return pd.read_csv(csv_path)
  
  
  
df = load_data() #load file pulled from inter
df.head() # look at first five rows make sure it popualtes as expected

#inspect data 
df.info()


#get values for one column of interest
df['col1'].value_counts()

#Counts, mean, sd, five number summary
df.describe()


#get plots of quantiative variables 
%matplotlib inline
import matplotlib.pyplot as plt
df.hist(bins=50, figsize=(20,15))
save_fig("attribute_histogram_plots")
plt.show()


#  make this notebook output identical at every run
np.random.seed(33)

#split into test/training data 
from sklearn.model_selection import train_test_split

train_set, test_set = train_test_split(df, test_size=0.2, random_state=33)



#create historgram of target variable only
df["target"].hist()


#get correlations
corr_matrix = df.corr()
corr_matrix["col1"].sort_values(ascending=False) #get the correlations of all variables on the target variable, and sort in order of highest corr



# get scatter plot matrix for selected variables -- nice correlation graphs 
from pandas.plotting import scatter_matrix

attributes = ["col1", "col2", "col3",
              "col4"]
scatter_matrix(df[attributes], figsize=(12, 8))
#diagonal is just histogram of the variable itself , others are x,y 




