## Pandas are very crucial for data analysis in Python. They provide powerful data structures and functions
# to manipulate and analyze data efficiently. Here are some key features of Pandas:

# 1. Series: A Series is a one-dimensional labeled array that can hold data of any type 
# (e.g., integers, strings, etc.)

import pandas as pd
print("Series in Pandas:")
s = pd.Series([1, 2, 3, 4, 5])
print(s)
print(type(s))

# 2. DataFrame: A DataFrame is a 2-dimensional labeled data structure that can hold data of different types
# (e.g., integers, strings, etc.). It is similar to a table in a relational database or an Excel spreadsheet.
print("DataFrame in Pandas:")
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'City': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data,index=['emp01','emp02','emp03'])
print(df)
print(type(df))
print(df['Name']) # Accessing a column in the DataFrame
print(df[['Name', 'Age']]) # Accessing multiple columns in the DataFrame
print(df.loc['emp01'])
## print(df.iloc[0][0]) # Accessing a specific value in the DataFrame using iloc
print(df.loc['emp02']['Name']) # Accessing a specific value in the DataFrame using loc
df.drop('City',axis=1,inplace=True) # Dropping a column from the DataFrame
print(df)
## axis = 1 means we want to drop a column, inplace = True means we want to modify the original DataFrame 
# instead of creating a new one
## if axis = 0 then we want to drop a row from the DataFrame, else if axis = any number other than 0 or 1 
# then it will give an error
df['Age'] = df['Age'] + 2 # Modifying a column in the DataFrame
df['Salary'] = [50000, 60000, 70000] # Adding a new column to the DataFrame
sum = df.describe() # gives the statistical summary of the DataFrame
print(sum)
print(df)
