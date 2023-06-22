import difflib
import sys

file1 = open("175_Diff_checker/my_shopping_list.txt").readlines()
file2 = open("175_Diff_checker/friends_shopping_list.txt").readlines()

# delta = difflib.unified_diff(file1, file2)
delta = difflib.unified_diff(file1, file2, "my_shopping_list.txt", "friends_shopping_list.txt")

sys.stdout.writelines(delta)

