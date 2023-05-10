from collections import Counter

# count the number of times each word appears in a string
text = "This is a sample text with some words. This is a sample text with some more words."
word_count = Counter(text.split())
print(word_count)

# count the number of times each word appears in a file
with open("134_Counters/example.txt", "r") as f:
    text = f.read()
    word_count = Counter(text.split())
print(word_count)
