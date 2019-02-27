import os
import glob
import webbrowser
import time

file = open('Fase1Pt1.txt', 'w')
path = r"C:\\Users\\pato_\\Downloads\\HTML\\Files"
filetime = 0

start = time.process_time()
for filename in glob.glob(os.path.join(path, '*.html')):
    print(filename)
    t = time.process_time()
    webbrowser.open(filename)
    elapsed_time = time.process_time() - t
    filetime = filetime + elapsed_time
    file.write(filename + " tardo " + str(elapsed_time) +
               " segundos en abrir." + '\n')
    os.system("taskkill /im chrome.exe /f")


end = time.process_time() - start
file.write("tiempo todal en abrir los archivos: " +
           str(filetime) + " segundos.")
file.write("tiempo total de ejecucion: " + str(end) + " segundos.")
file.close()
