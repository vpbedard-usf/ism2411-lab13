#1. 
#2. 
#3. 
print("exercise 1")
import pandas as pd
df = pd.read_csv('data/retail_sales.csv')
print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)
print("exercise 2")
south = df[df['region'] == 'South']
print(len(south))
print(south.head())
print("exercise 3")
print(df.sort_values('revenue', ascending=False).head(5))
print("exercise 4")
big_south = df[(df['region']=='South') & (df['revenue']>1000)]
print("exercise 5")
print("exercise 6")
print("exercise 7")
print("exercise 8")
