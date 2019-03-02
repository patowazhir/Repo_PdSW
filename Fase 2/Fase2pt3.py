import os
import glob
from collections import Counter

file = open('Fase2Pt3.txt', 'w')
path = r"F:\\Dev\\PDSWHTML\\Files\\Clean"

# allwords[word] = (total_count, file_count)
all_words = dict()

for filename in glob.glob(os.path.join(path, '*.html')):
   f = open(filename)
   wordcount = Counter(f.read().split())
   for word, count in wordcount.items():
      original_word = all_words.get(word, (0, 0))
      all_words[word] = (original_word[0] + count, original_word[1] + 1)

for word, properties in all_words.items():
   file.write("{}\t{}\t{}\n".format(word.ljust(20), properties[0], properties[1]))