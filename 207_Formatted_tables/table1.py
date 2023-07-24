def list_of_lists_to_table(data):
    # Find the maximum width for each column
    column_widths = [max(len(str(item)) for item in column) for column in zip(*data)]

    # Print the table with appropriate formatting
    for row in data:
        print("| " + " | ".join(f"{item:<{width}}" for item, width in zip(row, column_widths)) + " |")

# Example data as a list of lists
data = [
    ["Name", "Age", "Occupation"],
    ["John", 30, "Engineer"],
    ["Alice", 25, "Doctor"],
    ["Bob", 28, "Teacher"]
]

# Convert list of lists to a formatted table
list_of_lists_to_table(data)
