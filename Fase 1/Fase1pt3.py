import os
import glob
import webbrowser
import time
import re
from itertools import chain


def uniqueWords(lineas):
   return set(chain(*(line.split() for line in lineas if line)))


def cleanLine(line):
    cleanString = line.upper()
    cleanString = re.sub('[^A-Za-z0-9 ]+', '', cleanString)
    return cleanString


def getUniqueWords(filename):
    inFile = filename
    outFile = filename.replace(r"\\Clean", r"\\Unique")

    fileIn = open(inFile)
    fileOut = open(outFile, "w")
    temp = open(outFile + '.tmp', "w")

    # Identify unique words

    for line in fileIn:
        temp.write(cleanLine(line))

    temp.close()
    temp = open(outFile + '.tmp')

    wordSet = sorted(uniqueWords(temp))
    for word in wordSet:
        fileOut.write(word + '\n')

    fileIn.close()
    fileOut.close()
    temp.close()
    os.remove(outFile + '.tmp')


file = open('Fase1pt3.txt', 'w')
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
