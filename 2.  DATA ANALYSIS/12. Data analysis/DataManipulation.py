import pandas as pd
import random as rn

df = pd.read_csv('orders.csv')
print(df.head(5)) # prints the first 5 rows of the DataFrame
print(df.info()) # gives the information about the DataFrame such as number of rows, columns, data types, etc.
print(df.describe()) # gives the statistical summary of the DataFrame such as count, mean, std, min, max, etc.
print(df.tail(5)) # prints the last 5 rows of the DataFrame

missing = df.isnull()
print(missing) # gives a DataFrame of the same shape as df with True for missing values and False for non-missing values
print(df.isnull().sum()) # gives the count of missing values in each column of the DataFrame

# Filling missing values in the DataFrame:

# filling the missing values in the 'Quantity' column with the mean of the 'Quantity' column
df['Filled_Quantity'] = df['Quantity'].fillna(df['Quantity'].mean()) 
df['Filled_Price'] = df['Price'].fillna(df['Price'].mean())
df['Filled_PaymentMethod'] = df['PaymentMethod'].fillna(df['PaymentMethod'].mode()[0])
df['Filled_Rating'] = df['Rating'].fillna(df['Rating'].median())
print(df)

df = df.rename(columns={'Filled_Quantity':'New Quantity','Filled_Price':'New Price','Filled_PaymentMethod':'New PaymentMethod','Filled_Rating':'New Rating'})
df['New Price'] = df['New Price']*1.1 # increasing the price by 10%
print(df)

## Data Aggregating and grouping in Pandas:
grouped1 = df.groupby('Product').agg({'New Price':'mean','New Quantity':'size'})
print(grouped1) # gives the mean price of each product
grouped2 = df.groupby(['Product','PaymentMethod']).agg({'New Price':'mean','New Quantity':'size'})
print(grouped2) # gives the mean price and size of each product and payment method combination


