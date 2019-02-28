import os
import glob
from collections import Counter

file = open('Fase2Pt2.txt', 'w')
path = r"D:\\Desktop\\rand\\Files\\Clean"

for filename in glob.glob(os.path.join(path, '*.html')):
   f = open(filename)
   wordcount = Counter(f.read().split())
   file.write(filename + "\n") 
   for item in wordcount.items():
      file.write("{}\t{}".format(*item) + "\n") 

    
