# open() function  - returns a file object
# can specify the mode
# r 
# w
# a 

# operating system interfaces
# os module -  os depenedednt funcanality 

# CWD - current working directoryu 
# python assumes - whenever a files is called by name it is in cwd

# 
import os

#To get location - os.getcwd()
print(os.getcwd())

# to change cwd  os.chdir() -- argument new path
# to careate a directory - os.mkdir() os.makedirs()
#os.mkdir("/home/abhis/Documents/newfolderss")

# os.path.join(parent_dir, dirc)

# os.listdir() to get the list of all files and directories in the specified directry


# traverse root directory, and list directories as dirs and files as files
# os.walk returns a generator, that creates a tuple of values (current_path, directories in current_path, files in current_path).



import os

for root, dirs, files in os.walk("/home/abhis/Documents/Test_Directory"):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))



for root, dirs, files in os.walk("/home/abhis/Documents/Test_Directory"):
    path = root.split(os.sep)
    print((len(path) - 1) * '+++', os.path.basename(root))
    for file in files:
        print(len(path) * '***', file)

