# My implementation

import random

class WordSearchGenerator:
    def __init__(self, rows, cols, wordlist):
        self.rows = rows
        self.cols = cols
        self.grid = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.wordlist = wordlist

    def place_word(self, word):
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]  # Horizontal, Vertical, Diagonal, Diagonal (reverse)
        random.shuffle(directions)

        for direction in directions:
            dx, dy = direction
            possible_positions = []

            for i in range(self.rows):
                for j in range(self.cols):
                    end_x, end_y = j + len(word) * dx, i + len(word) * dy

                    if 0 <= end_x < self.cols and 0 <= end_y < self.rows:
                        possible_positions.append((j, i, dx, dy))

            if possible_positions:
                position = random.choice(possible_positions)
                self.fill_word(position, word)
                return True

        return False

    def fill_word(self, position, word):
        col, row, dx, dy = position
        for letter in word:
            self.grid[row][col] = letter
            row, col = row + dy, col + dx

    def fill_empty_spaces(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == ' ':
                    self.grid[i][j] = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    def generate_puzzle(self):
        for word in self.wordlist:
            word = word.upper().replace(' ', '')
            placed = self.place_word(word)
            if not placed:
                print(f"Could not place the word: {word}")

        self.fill_empty_spaces()

    def display_puzzle(self):
        for row in self.grid:
            print(' '.join(row))

if __name__ == "__main__":
    wordlist = ["python", "word", "search", "puzzle", "generator"]
    rows, cols = 10, 10

    generator = WordSearchGenerator(rows, cols, wordlist)
    generator.generate_puzzle()

    print("Word Search Puzzle:")
    generator.display_puzzle()
