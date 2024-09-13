import os

directory='/home/bk'
contents = os.listdir(directory)

for item in contents:
    print(item)