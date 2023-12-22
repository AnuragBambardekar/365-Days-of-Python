def search_word_in_2d_list(matrix, word):
    rows = len(matrix)
    cols = len(matrix[0])

    for row_index in range(rows):
        for col_index in range(cols):
            # Check horizontally
            if col_index + len(word) <= cols and matrix[row_index][col_index:col_index + len(word)] == list(word):
                return [row_index, col_index]

            # Check vertically
            if row_index + len(word) <= rows:
                column_slice = [matrix[i][col_index] for i in range(row_index, row_index + len(word))]
                if column_slice == list(word):
                    return [row_index, col_index]

            # Check diagonally (top-left to bottom-right)
            if col_index + len(word) <= cols and row_index + len(word) <= rows:
                diagonal_slice = [matrix[row_index + i][col_index + i] for i in range(len(word))]
                if diagonal_slice == list(word):
                    return [row_index, col_index]

            # Check diagonally (top-right to bottom-left)
            if col_index - len(word) >= -1 and row_index + len(word) <= rows:
                diagonal_slice = [matrix[row_index + i][col_index - i] for i in range(len(word))]
                if diagonal_slice == list(word):
                    return [row_index, col_index]

    return None

matrix = [
    ['a', 'b', 'c', 'd'],
    ['e', 'f', 'g', 'h'],
    ['i', 'j', 'k', 'l'],
    ['m', 'n', 'o', 'p']
]

word_to_search = "fgh"

result = search_word_in_2d_list(matrix, word_to_search)
print(result)
