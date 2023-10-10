# pip install plotnine

import pandas as pd
import random

# Create a fictional dataset
data = pd.DataFrame({
    'Study_Time_Hours': [random.randint(1, 10) for _ in range(50)],
    'Exam_Score': [random.randint(60, 100) for _ in range(50)]
})

# Import the necessary libraries
from plotnine import *

# Create a ggplot visualization
gg = (
    ggplot(data, aes(x='Study_Time_Hours', y='Exam_Score')) +
    geom_point(color='blue') +
    labs(x="Study Time (Hours)", y="Exam Score", title="Study Time vs. Exam Score")
)

# Display the plot
print(gg)

# Save the plot to a file (optional)
ggsave('study_time_vs_exam_score.png', plot=gg, width=6, height=4)
