from os import listdir, getcwd
from os.path import isfile, join
#from .models import Photo

def CreatePhotos():
    path = "/../static/"
    onlyfiles = [f[:-4] for f in listdir(path) if isfile(join(path, f))]

    print(onlyfiles)
    for file in onlyfiles:
        #Photo.CreatePhoto(file, 'G', 'F')
        path

print([1,2,3]/3)