import pandas as pd
from io import StringIO

# Example 1: Reading a CSV file
csv_data ="Name, Age, City\nAlice, 30, New York\nBob, 25, Los Angeles\nCharlie, 35, Chicago"
df = pd.read_csv(StringIO(csv_data))
print("CSV Data:")
print(df)
# Example 2: Reading an Excel file

df = pd.read_excel('data.xlsx',engine='openpyxl')
print("\nExcel Data:")
print(df)


# Example 3: Reading a JSON file
json_data = '{"Name": ["Alice", "Bob", "Charlie"], "Age": [30, 25, 35], "City": ["New York", "Los Angeles", "Chicago"]}'
df = pd.read_json(StringIO(json_data))

print("\nJSON Data:")
print(df)

# Example 4: Reading a text file
text_data = """Name\tAge\tCity
Alice\t30\tNew York
Bob\t25\tLos Angeles
Charlie\t35\tChicago"""
df = pd.read_csv(StringIO(text_data), sep='\t')
print("\nText Data:")
print(df)

## pickling a file
# Example 5: Pickling a DataFrame
df.to_pickle('data.pkl')
# Example 6: Unpickling a DataFrame
df_unpickled = pd.read_pickle('data.pkl')
print("\nUnpickled Data:")
print(df_unpickled)