import os
import time
import shutil

path = './'

def getDate(file):
    stamp = os.path.getmtime(file)
    
    a = time.ctime(stamp)

    converterEmTempo = time.strptime(a)

    return time.strftime("%d-%m-%Y", converterEmTempo)
    
    


os.chdir(path)
for files in os.listdir():
    
    if files == 'ORGANIZAR.py' or os.path.isdir(files) or files == 'Thumbs.db':
        pass
    else:
        date = getDate(files)
        try:
            os.mkdir(path+date+'/')
            shutil.move(path+files, path+date+'/'+files)
        except FileExistsError:
            shutil.move(path+files, path+date+'/'+files)
            

        


