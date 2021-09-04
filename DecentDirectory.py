

# operating system interfaces
# OS Module -  os depenedednt funcanality 

# CWD - current working directoryu 
# python assumes - whenever a files is called by name it is in cwd


# open() function  - returns a file object
# can specify the mode
# r 
# w
# a 
import os

#To get location - os.getcwd()
print(os.getcwd())

# to change cwd  os.chdir() -- argument new path
# to careate a directory - os.mkdir() os.makedirs()
# os.mkdir("/home/abhis/Documents/newfolderss")
# os.path.join(parent_dir, dirc)
# os.listdir() to get the list of all files and directories in the specified directry
# os.remove() - delete directory r files

# traverse root directory, and list directories as dirs and files as files


# os.walk() .. it generates the filenane by walking the tree
# returns a genreator 
# that creates a tuple of values (dirpath, dirname,filnames)


import os

# a =os.walk("/home/abhis/Documents/Test_Directory")
# print(a)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

print("#########")

for dirpath, dirname, files in os.walk("/home/abhis/Documents/Test_Directory"):
   for i in files:
      print(os.path.join(dirpath, i))
   for x in dirname:
      print(os.path.join(dirpath, x))



for root, dirs, files in os.walk("/home/abhis/Documents/Test_Directory"):
    path = root.split(os.sep)
    print((len(path) - 1) * '+++', os.path.basename(root))
    for file in files:
        print(len(path) * '***', file)


# os.path.join() :  joins  path components with exactly one direct separator (“/”)


