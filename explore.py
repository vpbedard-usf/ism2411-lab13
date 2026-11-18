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
print(len(big_south))
print(big_south.head())
print("exercise 5")
df['per_unit'] = df['revenue'] / df['quantity']
print(df.head())
mean_per_unit = df['per_unit'].mean()
print(mean_per_unit)
print("exercise 6")
print(df['region'].unique())
print(df['region'].value_counts())
print("exercise 7")
df_subset = df[['region', 'revenue', 'quantity']]
print(df_subset.shape)
print("exercise 8")
df.to_csv('data/explored.csv', index=False)
