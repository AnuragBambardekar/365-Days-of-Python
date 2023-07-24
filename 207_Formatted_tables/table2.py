def list_of_lists_to_minimalist_table(data):
    column_widths = [max(len(str(item)) for item in column) for column in zip(*data)]
    for i, row in enumerate(data):
        if i == 0:
            print(" | ".join(f"{item:<{width}}" for item, width in zip(row, column_widths)))
            print("-" * (sum(column_widths) + len(row) * 3 - 1))
        else:
            print(" | ".join(f"{item:<{width}}" for item, width in zip(row, column_widths)))

# Example data as a list of lists
data = [
    ["Name", "Age", "Occupation"],
    ["John", 30, "Engineer"],
    ["Alice", 25, "Doctor"],
    ["Bob", 28, "Teacher"]
]

# Convert list of lists to a minimalist table with proper formatting
list_of_lists_to_minimalist_table(data)
