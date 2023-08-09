import pandas as pd
import numpy as np
import numba

# Create a sample DataFrame
data = {'A': np.random.rand(1000000)}
df = pd.DataFrame(data)

# Define a function that squares each element using numba
# @numba.njit
def square_column(arr):
    result = np.empty_like(arr)
    for i in range(len(arr)):
        result[i] = arr[i] * arr[i]
    return result

# Apply the numba-optimized function to the DataFrame column
df['A_squared'] = square_column(df['A'].to_numpy())

print(df.head())
