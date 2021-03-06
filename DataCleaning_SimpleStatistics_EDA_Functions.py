#get columns from pandas dataframe
df.columns 


#get unique values of one columns, by their frequency (omits nulls)
df['col1'].value_counts()


#two-way frequency table  / crosstab
pd.crosstab(index=df['col1'], columns=df['c2'])
#https://www.statology.org/frequency-tables-python/


#count null values for each column 
df.isnull().sum()


#shows non-null values, indices, and data types
df.info()


#similar to dplyr in R or SQL syntax, group by
s = df['col1'].groupby(df['col2']).value_counts().reset_index(name='counts') # name of the frequencies/counts is the string after 'name='


#create binary variable from other variables 
df['bin'] = np.where(df['col1'] > 14, 1, 0)



#multiple conditions 
def f(row):
    if row['col1'] == row['col2']:
        val = 0
    elif row['col1'] > row['col2']:
        val = 1
    else:
        val = -1
    return val

df['multiple_conditions'] = df.apply(f, axis=1)
