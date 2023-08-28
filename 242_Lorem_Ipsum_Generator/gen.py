"""
In publishing and graphic design, lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a 
typeface without relying on meaningful content.

Lorem Ipsum is dummy text developed by Richard McClintock in 1982. He took the text from Cicero’s book named 
De finibus bonorum et malorum.
"""

import random

# Define a list of common Latin words used in Lorem Ipsum
latin_words = [
    "Lorem", "ipsum", "dolor", "sit", "amet", "consectetur",
    "adipiscing", "elit", "sed", "non", "risus", "suspendisse",
    "lectus", "tortor", "dignissim", "nec", "ultricies", "maecenas",
    "ligula", "massa", "varius", "a", "mi", "proin", "orci", "enim",
    "est", "eleifend", "fermentum", "duis", "arcu", "vitae", "congue",
    "euismod", "in", "pretium", "pellentesque", "ut", "pharetra",
    "tempor", "vestibulum", "augue", "praesent", "egestas", "leo",
    "blandit", "odio", "sed", "dui", "ut", "sodales", "ante", "in",
    "cubilia", "Curae", "aliquam", "nibh", "mauris", "ac", "pede"
]

# Function to generate Lorem Ipsum-like text
def generate_lorem_ipsum_paragraph(sentence_count=5, sentence_length_range=(5, 15)):
    lorem_ipsum = []
    
    for _ in range(sentence_count):
        sentence_length = random.randint(*sentence_length_range)
        sentence = ' '.join(random.choices(latin_words, k=sentence_length))
        sentence = sentence.capitalize() + '.'
        lorem_ipsum.append(sentence)
    
    return ' '.join(lorem_ipsum)

paragraph_count = int(input("Enter the number of paragraphs: "))
sentence_count = int(input("Enter the number of sentences per paragraph: "))

# Generate and print the Lorem Ipsum-like text
for _ in range(paragraph_count):
    lorem_ipsum_text = generate_lorem_ipsum_paragraph(sentence_count)
    print(lorem_ipsum_text)
