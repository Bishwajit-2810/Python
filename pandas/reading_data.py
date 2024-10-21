import pandas as pd

coffee= pd.read_csv("pandas/data/coffee.csv")
print(coffee.head())
print()
results= pd.read_parquet("pandas/data/results.parquet")
print(results.head())
print()
results= pd.read_feather("pandas/data/results.feather")
print(results.head())
print()
olympic= pd.read_excel("pandas/data/olympics-data.xlsx")
print(olympic.head())
print()