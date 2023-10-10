import pandas as pd
from plotnine import *

# Create a DataFrame
data = pd.DataFrame({
    'X': [1, 2, 3, 4, 5],
    'Y': [10, 8, 6, 4, 2]
})

# Create a scatter plot
gg = ggplot(data, aes(x='X', y='Y')) + geom_point()
print(gg)

# Line plot
gg = ggplot(data, aes(x='X', y='Y')) + geom_line()
print(gg)

# Bar plot
data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Value': [15, 30, 10, 25]
})
gg = ggplot(data, aes(x='Category', y='Value')) + geom_bar(stat='identity')
print(gg)

data = pd.DataFrame({'Values': [10, 10, 20, 25, 10, 35, 20, 25, 50]})

# Create a histogram
gg = ggplot(data, aes(x='Values')) + geom_histogram(binwidth=5, fill='blue', color='black')
print(gg)

data = pd.DataFrame({
    'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Value': [10, 15, 20, 25, 30, 35]
})

# Create a box plot
gg = ggplot(data, aes(x='Category', y='Value')) + geom_boxplot()
print(gg)