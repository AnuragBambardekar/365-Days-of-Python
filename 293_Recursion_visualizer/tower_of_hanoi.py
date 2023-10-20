from visualiser.visualiser import Visualiser as vs

@vs(node_properties_kwargs={"shape":"record", "color":"#f57542", "style":"filled", "fillcolor":"grey"})
def towers_of_hanoi(n, source_peg, auxiliary_peg, target_peg):
    if n == 1:
        print(f"Move disk 1 from {source_peg} to {target_peg}")
        return
    towers_of_hanoi(n - 1, source_peg, target_peg, auxiliary_peg)
    print(f"Move disk {n} from {source_peg} to {target_peg}")
    towers_of_hanoi(n - 1, auxiliary_peg, source_peg, target_peg)

def main():
    n = 3  # You can change 'n' to the number of disks you want to solve the Towers of Hanoi for.
    towers_of_hanoi(n, 'A', 'B', 'C')
    vs.make_animation("towerOfHanoi.gif", delay=2)

if __name__ == "__main__":
    main()
