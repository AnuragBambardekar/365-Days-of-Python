import matplotlib_venn as vplt
from matplotlib import pyplot as plt

list1 = ["Q","W","E","R","T","Y","U","I","O","P"]
list2 = ["A","S","D","F","G","H","J","K","L"]
list3 = ["Z","X","C","V","B","N","M"]

def make_venn(venn, lst, labels):
    return venn(lst, set_labels=labels)

make_venn(vplt.venn2, [set(list1), set(list2)], ('First Row','Second Row'))
plt.title('Rows of a QWERTY Keyboard')
plt.show()

make_venn(vplt.venn3, [set(list1), set(list2), set(list3)], ('First Row','Second Row','Third Row'))
plt.title('Rows of a QWERTY Keyboard')
plt.show()