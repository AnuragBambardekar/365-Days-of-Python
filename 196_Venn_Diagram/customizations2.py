from matplotlib_venn import venn3, venn3_circles
from matplotlib import pyplot as plt
  
# depict venn diagram
"""
Plots a 3-set area-weighted Venn diagram. The subsets parameter can be one of the following:

A list (or a tuple), containing three set objects.
A dict, providing sizes of seven diagram regions. The regions are identified via three-letter binary codes ('100', '010', etc), 
hence a valid set could look like: {'001': 10, '010': 20, '110':30, ...}. Unmentioned codes are considered to map to 0.
A list (or a tuple) with 7 numbers, denoting the sizes of the regions in the following order: (100, 010, 110, 001, 101, 011, 111).
"""
venn3(subsets=(20, 10, 12, 10, 9, 4, 3), 
      set_labels=('Group A', 'Group B', 'Group C'), 
      set_colors=("orange", "blue", "red"), alpha=0.7)
  
# outline of circle line style and width
venn3_circles(subsets=(20, 10, 12, 10, 9, 4, 3),
              linestyle="dashed", linewidth=2)
  
# title of the venn diagram
plt.title("Venn Diagram")
plt.show()