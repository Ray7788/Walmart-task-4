import pandas as pd
import sqlite3
import glob

file_ext

# read raw material
df1 = pd.read_csv('shipping_data_0.csv')
df2 = pd.read_csv('shipping_data_1.csv')
df3 = pd.read_csv('shipping_data_2.csv')

df1.head()
df2.head()
df3.head()

# merge 3 parts
df23 = pd.merge(df2,df3, how = 'inner', on= 'shipment_identifier')
print(df23)

df123 = pd.merge(df1,df23, how= 'outer')
df123

# to create a connection to the database & set the cursor
con = sqlite3.connect('shipment_database.db')
cur = con.cursor()

# create table
cur.execute('''CREATE TABLE shipment(origin_warehouse text, destination_store
text, product text, on_time boolean, product_qty real, driver_identifier text,
shipment_identifier text)''')

for row in df_final.itertuples():
    insert_sql = f"INSERT INTO shipment (origin_warehouse, destination_store,product, on_time, product_qty, driver_identifier, shipment_identifier) 
    VALUES('{row[1]}', '{row[2]}', '{row[3]}', '{row[4]}', '{row[5]}', '{row[6]}','{row[7]}')"

cur.execute(insert_sql)

#  needs to be committed before changes are saved in the database
con.commit()
