from collections import defaultdict

words = ["apple", "banana", "carrot", "avocado", "broccoli", "orange"]
grouped_words = defaultdict(list)

for word in words:
    grouped_words[word[0]].append(word)

print(grouped_words)