import pandas as pd
from plotnine import *

# Create a DataFrame with example data
data = pd.DataFrame({
    'X': [1, 2, 3, 4, 5],
    'Y': [10, 8, 6, 4, 2]
})

# Create a scatter plot
gg = ggplot(data, aes(x='X', y='Y')) + geom_point()

# Save as PNG
gg.save(filename='scatter_plot.png', format='png', width=6, height=4, units='in')

# Save as SVG
gg.save(filename='scatter_plot.svg', format='svg', width=6, height=4, units='in')
