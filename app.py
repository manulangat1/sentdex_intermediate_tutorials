names = ["Manu","James","John"]
for name in names :
    print(' '.join(['Hello there', name]))

# print(str(names))


import os 
location_of_file = "/home/manulangat/Desktop/mega_p/sentdex"
filename = '.gitignore'

with open(os.path.join(location_of_file,filename)) as f:
    print(f.read())