import os
import glob
import webbrowser
import time
import re


def clean(raw):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw)
    return cleantext


def removeHTMLTags(filename):
    inFile = filename
    outFile = filename.replace(r"\\Files", r"\\Files\\Clean")

    fileIn = open(inFile, errors='ignore')
    fileOut = open(outFile, "w")
    for line in fileIn:
        line = clean(line)
        fileOut.write(line)
    fileIn.close()
    fileOut.close()


file = open('Fase1Pt2.txt', 'w')
path = r"C:\\Users\\pato_\\Downloads\\HTML\\Files"
filetime = 0

start = time.process_time()
for filename in glob.glob(os.path.join(path, '*.html')):
    print(filename)
    t = time.process_time()
    removeHTMLTags(filename)
    elapsed_time = time.process_time() - t
    filetime = filetime + elapsed_time
    file.write(filename + " tardo " + str(elapsed_time) +
               " segundos en limpiar." + '\n')

end = time.process_time() - start
file.write("tiempo todal en limpiar los archivos: " +
           str(filetime) + " segundos" + '\n')
file.write("tiempo total de ejecucion: " + str(end) + " segundos")
file.close()
