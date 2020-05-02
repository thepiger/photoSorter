import glob
import os
from shutil import copyfile
import exifread
from datetime import datetime

files = glob.glob("source/*.JPG")

listDated = []


for el in files:
    print( el )

    with open(el, 'rb') as fh:
        tags = exifread.process_file(fh, stop_tag="EXIF DateTimeOriginal")
        dateTaken = tags["EXIF DateTimeOriginal"]
        
        datetime_object = int( datetime.strptime(str(dateTaken), '%Y:%m:%d %H:%M:%S').timestamp())
        listDated.append( (el, datetime_object ,str(dateTaken) ))

listDated.sort( key=lambda x: x[1])

n = 0
for el in listDated:
    ordinalNumber=("000000"+str(n))[-6:]
    destName = "dest/DSC{number}.JPG".format(number=ordinalNumber)
    copyfile(el[0], destName)

    print(el)
    n += 1
