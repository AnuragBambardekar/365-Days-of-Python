# If you have a 50GB dataset you cannot load all of it in a RAM of say, size 32GB

import pandas as pd

# df = pd.read_csv("222_Processing_huge_datasets/companies_sorted.csv") # loading this dataset as a whole consumes a lot of memory

df = pd.read_csv("222_Processing_huge_datasets/companies_sorted.csv", nrows=100)
print(df)

df = pd.read_csv("222_Processing_huge_datasets/companies_sorted.csv", nrows=100, skiprows=500)
print(df)

df.columns = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
print(df)

# print(df.J / df.K)

metric_results = pd.Series([], dtype="float64")
metric_results = pd.concat([metric_results, df.J/df.K])
print(metric_results)