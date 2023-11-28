def edit_distance(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if str1[i - 1] == str2[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost)

    return dp[m][n]

def autocorrect(input_word, vocabulary):
    min_distance = float('inf')
    corrected_word = input_word

    for word in vocabulary:
        distance = edit_distance(input_word, word)
        if distance < min_distance:
            min_distance = distance
            corrected_word = word

    return corrected_word

if __name__ == "__main__":
    # Example vocabulary
    vocabulary = ["apple", "banana", "orange", "grape", "kiwi"]

    # Example misspelled word
    misspelled_word = "applle"

    # Perform autocorrection
    corrected_word = autocorrect(misspelled_word, vocabulary)

    print(f"Original word: {misspelled_word}")
    print(f"Corrected word: {corrected_word}")
