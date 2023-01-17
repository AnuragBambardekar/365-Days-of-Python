#ANSI Foreground
""" for n in range(1,257):
    print(f"\x1b[38;5;{n}mhello, I am Anurag") """

#ANSI Background
""" for n in range(1,256):
    print(f"\x1b[48;5;{n}mhello, I am Anurag")
    print("") """

#256-color mode
""" for r in range(1,256):
    for g in range(1,256):
        for b in range(1,256):
            print(f"\x1b[38;2;{r};{g};{b}mhello, I am Anurag") """


#====================Do Not Run This========================#
from concurrent.futures import ProcessPoolExecutor

def print_color(r,g,b):
    print(f"\x1b[38;2;{r};{g};{b}mhello, I am Anurag")

if __name__ == "__main__":
    with ProcessPoolExecutor() as executor:
        for r in range(1,256):
            for g in range(1,256):
                for b in range(1,256):
                    executor.submit(print_color, r,g,b)
#===========================================================#