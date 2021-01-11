import pandas as pd
import os 

#know the filepath that it's being sent to or readfrom:
os.getcwd()
xls = pd.ExcelFile('Workbook_Name_Generic.xlsx') 

#read Excel file into python
indata = pd.read_excel( xls
                       ,sheet_name = 'Sheet1'
                       ,header = 0 #row index = 0 indicates that first line is the title of columns
                       ,dtype = str )
                       

#write one sheet only
df1.to_excel(r'Workbook_Name_Generic.xlsx', index = False, sheet_name = 'Sheet1')


#write multiple sheets an an Excel Workbook
with pd.ExcelWriter('Workbook_Name_Generic.xlsx') as writer:
  df1.to_excel(writer, sheet_name='Sheet1', index = False)
  df2.to_excel(writer, sheet_name='Sheet2', index = False) #index False means that index column is not written, keep in mind if data is used as index rather 
  
  

  
  
