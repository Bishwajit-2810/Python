import pandas as pd

df=pd.DataFrame([[1,2,3],[4,5,6]])
print(df)

print()

df=pd.DataFrame([[1,2,3],[4,5,6]],columns=["a","b","c"],index=["x","y"])
print(df)

print()

print(df.head(1))
print()
print(df.tail(1))

print()

print(df.columns)
print(df.index.tolist())
print(df.info())
print(df.describe())
print(df.nunique())
print(df['a'].unique())
print(df.shape)
print(df.info())