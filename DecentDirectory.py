# Python File I/O
#Python open() function  - returns a file object
#  can specify the mode
# r 
# w
# a 

import os


# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk("/home/abhis/Documents/Test_Directory"):
    path = root.split(os.sep)
    print((len(path) - 1) * '---', os.path.basename(root))
    for file in files:
        print(len(path) * '---', file)