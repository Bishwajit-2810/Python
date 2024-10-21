import pandas as pd

coffee= pd.read_csv("pandas/data/coffee.csv")
print(coffee.head(5))
print()
print(coffee.tail(5))
print()
print(coffee.sample(5))
print()
print(coffee.sample(5,random_state=1))
print()
