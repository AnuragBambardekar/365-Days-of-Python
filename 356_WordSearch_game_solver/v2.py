"""
run extract_text_grid.py to extract the letters from the grid
run extract_text_words_to_find.py to extract the 'words to find'
run this script to find words in grid
"""



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

text = """Y C M O S P Q P T N
J H E Q W M W A F E
U V R C V E A R T H
P E C Q Y F X I Y N
I N U R A N U S N E
T U R E L D C R B P
E S Y S P R U C O T
R J R A O T Q V N U
T A M Q A E I N H N
M D I S D L A H K E"""

# Split the text into lines
lines = text.split('\n')

# Split each line into characters
matrix = [list(line.split()) for line in lines]

# Display the matrix
# for row in matrix:
#     print(row)

# word_to_search = "MERCURY"

# result = search_word_in_2d_list(matrix, word_to_search)
# print(result)

words_to_search = ["MERCURY", "URANUS", "JUPITER", "VENUS", "NEPTUNE", "EARTH", "SATURN", "MARS"]

for word in words_to_search:
    result = search_word_in_2d_list(matrix, word)
    print(f"Word: {word}, Positions: {result}")