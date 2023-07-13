from matplotlib_venn import venn3, venn3_circles
from matplotlib import pyplot as plt
  
# depict venn diagram
venn3(subsets=(20, 10, 12, 10, 9, 4, 3), 
      set_labels=('Group A', 'Group B', 'Group C'), 
      set_colors=("orange", "blue", "red"), alpha=0.7)
  
# outline of circle line style and width
venn3_circles(subsets=(20, 10, 12, 10, 9, 4, 3),
              linestyle="dashed", linewidth=2)
  
# title of the venn diagram
plt.title("Venn Diagram")
plt.show()