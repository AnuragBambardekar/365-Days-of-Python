import pandas as pd
from plotnine import *

# Create a DataFrame with example data
data = pd.DataFrame({
    'X': [1, 2, 3, 4, 5],
    'Y': [10, 8, 6, 4, 2]
})

# Create a scatter plot
gg = ggplot(data, aes(x='X', y='Y')) + geom_point()

# Define a custom function to add a text watermark
def add_text_watermark(plot, watermark_text):
    return plot + annotate(
        'text',
        x=0.5,
        y=0.5,
        label=watermark_text,
        size=10,
        alpha=0.5,
        color='gray',
        angle=45  # You can adjust the angle of the text
    )

# Call the custom function to add a text watermark to the plot
gg_with_text_watermark = add_text_watermark(gg, 'Watermark Text')

# Save the plot with the text watermark as a PNG
gg_with_text_watermark.save(filename='plot_with_text_watermark.png', width=6, height=4, units='in')
