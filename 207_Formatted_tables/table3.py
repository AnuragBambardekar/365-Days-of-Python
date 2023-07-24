def list_of_lists_to_grid_table(data):
    column_widths = [max(len(str(item)) for item in column) for column in zip(*data)]
    
    def print_row(row):
        print("+".join("-" * width for width in column_widths))
        print("|".join(f"{item:<{width}}" for item, width in zip(row, column_widths)))

    print_row(data[0])
    for row in data[1:]:
        print_row(row)

# Example data as a list of lists
data = [
    ["Name", "Age", "Occupation"],
    ["John", 30, "Engineer"],
    ["Alice", 25, "Doctor"],
    ["Bob", 28, "Teacher"]
]

# Convert list of lists to a grid-style table with proper formatting
list_of_lists_to_grid_table(data)
