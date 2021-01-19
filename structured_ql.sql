#partition 
# https://www.sqlservertutorial.net/sql-server-window-functions/sql-server-row_number-function/
SELECT 
   first_name, 
   last_name, 
   city,
   ROW_NUMBER() OVER (
      PARTITION BY city
      ORDER BY first_name desc 
   ) as row_num
FROM 
   sales.customers
ORDER BY 
   city;
