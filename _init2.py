from os import listdir
from os.path import isfile, join

import hashlib

PATH= "/home/dongsub/pk"

# get a list of Files
onlyfiles = [f for f in listdir(PATH) if isfile(join(PATH, f))]

# Hashing md5
HASHING_LIST_MD5= []
for file in onlyfiles:
    file= PATH+"/"+file
    HASHING_LIST_MD5.append(hashlib.md5(open(file,'rb').read()).hexdigest())


# data formatting
FILE_NAMES= ""
for file in onlyfiles:
    FILE_NAMES+= ", "+ file

MD5_HASHINGS= ""
for hashing in HASHING_LIST_MD5:
    MD5_HASHINGS+= ", " + hashing


# save a MD file
file = open('result.md', 'w')

file.write(FILE_NAMES)
file.write(MD5_HASHINGS)

file.close() 



# ref
# 1. https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
# 2. https://stackoverflow.com/questions/16874598/how-to-calculate-the-md5-checksum-of-a-file-in-python
# 3. https://www.geeksforgeeks.org/saving-text-json-and-csv-to-a-file-in-python/