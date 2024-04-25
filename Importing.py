import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"

df = pd.read_csv(url, header = None)

print(df.head(4))
print(df.tail(4))
print(df.dtypes)
print(df.describe(include = "all"))
print(df.info())