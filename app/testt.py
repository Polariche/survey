from os import listdir, getcwd, rename
from os.path import isfile, join
from .models import Photo

def getPath():
    return getcwd()+"/static/"

def getFiles():
    path = getPath()
    onlyfiles = [f[:-4] for f in listdir(path) if isfile(join(path, f))]

    return onlyfiles

def createPhotos(univ, gender):
    onlyfiles = getFiles()

    for file in onlyfiles:
        if not Photo.objects.filter(filename=file):
            Photo(file, univ, gender).save()

def renamePhotos():
    path = getPath()
    files = getFiles()

    for i in range(len(files)):
        file = files[i]
        rename(path+file+'.png', path+str(i)+'.png')

        photo = Photo.objects.filter(filename=file)[0]
        photo.filename = str(i)
        photo.save()

