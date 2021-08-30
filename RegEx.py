# Regular Expressions
# python module to work 

# regex ?
# a sequence of characters that define a search pattern
# EX- ^a...s$
# thi is any 5 letter string starting with a and ending with s
# python module re 

import re
pat = "^a....s"

test_string = "abyfs"
print(re.match(pat,test_string))