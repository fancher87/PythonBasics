import pandas as pd
import os 

#know the filepath that it's being sent to:
os.getcwd()


#write one sheet only
df1.to_excel(r'Workbook_Name_Generic.xlsx', index = False, sheet_name = 'Sheet1')


#write multiple sheets an an Excel Workbook
with pd.ExcelWriter('Workbook_Name_Generic.xlsx') as writer:
  df1.to_excel(writer, sheet_name='Sheet1', index = False)
  df2.to_excel(writer, sheet_name='Sheet2', index = False) #index False means that index column is not written, keep in mind if data is used as index rather 
  
  
