import os
import glob
import webbrowser
import time
import re
from itertools import chain


def splitWords(fileIn):
        words = []
        for line in fileIn:
            line = cleanLine(line)
            if line.strip() != ' ':
                words.extend(line.strip().split())
        return words

def cleanLine(line):
    cleanString = line.upper()
    cleanString = re.sub('[^A-Za-z0-9 ]+', '', cleanString)
    return cleanString

def getUniqueWords(filename):
    inFile = filename
    outFile = filename.replace(r"\\Clean", r"\\Unique")

    fileIn = open(inFile)
    fileOut = open(outFile, "w")

    words = sorted(splitWords(fileIn))

    for word in words:
        fileOut.write(word + '\n')

    fileIn.close()
    fileOut.close()


file = open('Fase2pt1.txt', 'w')
path = r"C:\\Users\\pato_\\Downloads\\HTML\\Files\\Clean"
filetime = 0

start = time.process_time()
for filename in glob.glob(os.path.join(path, '*.html')):
    print(filename)
    t = time.process_time()
    getUniqueWords(filename)
    elapsed_time = time.process_time() - t
    filetime = filetime + elapsed_time
    file.write(filename + " tardo " + str(elapsed_time) +
               " segundos en limpiar." + '\n')

end = time.process_time() - start
file.write("tiempo todal en limpiar los archivos: " +
           str(filetime) + " segundos." + '\n')
file.write("tiempo total de ejecucion: " + str(end) + " segundos.")
file.close()
