import pandas as pd

metric_results = pd.Series([], dtype="float64")
counter = 0

for chunk in pd.read_csv("222_Processing_huge_datasets/companies_sorted.csv", chunksize=1000):
    chunk.columns = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
    metric_results = pd.concat([metric_results, chunk.J/chunk.K])
    counter+=1
    if counter == 20:
        break
print(metric_results)