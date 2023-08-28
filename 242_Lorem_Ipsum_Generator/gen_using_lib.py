# pip install python-lorem
import lorem

# text = lorem.paragraph(count=2, comma=(0,2), word_range=(4,8), sentence_range=(5,10))

word_list = lorem.get_word(count = (1,5), sep= ' ')
# print(word_list)

sentence_list = lorem.get_sentence(count= (1,5), comma= (1,5), sep= '\n')
# print(sentence_list)

paragraphs = lorem.get_paragraph(count= (1,5), comma= (1,5))
# print(paragraphs)

# Custom Pool of words
_TEXT = ('sed','sint',)
paragraphs = lorem.get_paragraph(count= 1, comma= (1,5), pool=_TEXT)
print(paragraphs)