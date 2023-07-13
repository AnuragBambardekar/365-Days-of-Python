import matplotlib_venn as vplt
from matplotlib import pyplot as plt

marketing = ["partnerships", "design", "product marketing"]
strategy = ["product marketing", "product management", "partnerships"]
product = ["product marketing", "product management", "design"]

def make_venn(venn, lst, labels):
    return venn(lst, set_labels=labels)

make_venn(vplt.venn3, [set(marketing), set(strategy), set(product)], ('marketing','strategy','product'))
plt.show()