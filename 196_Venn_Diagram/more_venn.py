from matplotlib_venn import venn2_unweighted 
from matplotlib import pyplot as plt
  
# depict venn diagram
venn2_unweighted(subsets = (50, 10, 7),
                 set_labels = ('Group A', 
                               'Group B'),
                 set_colors=("orange",
                             "blue"),alpha=0.7)
plt.show()