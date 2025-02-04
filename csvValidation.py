import pandas as pd

data = pd.read_csv('test_Channel_messages.csv')

print(data.head())

print(data.columns)
#Print number of rows
print(data.shape[0])