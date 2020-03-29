#program to display most common words in the dictionary
words = ['red', 'green', 'black', 'pink', 'black','white','black', 
          'eyes', 'white', 'black', 'orange','white','black',
          'pink', 'green','pink', 'green', 'red']
from collections import Counter
word_count = Counter(words)
top_four = word_count.most_common(4)
print(top_four)           