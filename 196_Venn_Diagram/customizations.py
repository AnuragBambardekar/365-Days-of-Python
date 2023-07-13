from matplotlib_venn import venn3, venn3_circles
from matplotlib import pyplot as plt
  
# depict venn diagram
v = venn3(subsets=(1, 1, 1, 1, 1, 1, 1), 
          set_labels=('A', 'B', 'C'))

"""
Plots a 3-set area-weighted Venn diagram. The subsets parameter can be one of the following:

A list (or a tuple), containing three set objects.
A dict, providing sizes of seven diagram regions. The regions are identified via three-letter binary codes ('100', '010', etc), 
hence a valid set could look like: {'001': 10, '010': 20, '110':30, ...}. Unmentioned codes are considered to map to 0.
A list (or a tuple) with 7 numbers, denoting the sizes of the regions in the following order: (100, 010, 110, 001, 101, 011, 111).
"""

# set color to defined path id
v.get_patch_by_id("100").set_color("white")
# set text to defined label id
v.get_label_by_id("100").set_text("unknown")
# set text to defined label id "A"
v.get_label_by_id('A').set_text('A new')
  
# add outline
venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1), 
              linestyle="dashed", linewidth=2)
  
# assign title
plt.title("Venn Diagram")
plt.show()