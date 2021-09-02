# Regular Expressions
# python module tre
# regex ?
# Regular Expressions
# sequence of characters that define a search pattern
# used for password/email/text validation
# EX- ^a...s$
# thi is any 5 letter string starting with a and ending with s

# python module re 

import re
pat = "^a....s"

test_string = "abyfs"
print(re.match(pat,test_string)) #None


#re.match() function to search pattern
# returns match object or None

#About RegExpressions

#Specify pattern using regex -  Metachars are interpreted in a spcial way RegEx engine
# []
# . 
# ^
# +
# ?
# {}
# ()
# \
# |

# Square brackects []
# a set of chars to match

# [abc] , a 1match, ac 2 matc, xyx no match, abc de ca. 5 match
# [abc] will match to string contains any of a,b,c
# [a-e] is same as [abcde]

# INVERT using caret ^ symbol 
# [^abc] means anything except a or b or c .eg hello

# Period . 
# any ONE char except newline '\n'
# 1.  1a  Match
# .. aa     match
# .. abc    match


# ^ Caret  - if a string start with certain chars
# ^p prabcs    match   ,  nagcbss No match
# ^pq

# $ Dollar -- if it end with certain chars
# a$ formula 1 match , cab no match

# * Star  -  0+ occurance of preceding elements

# ma*n      -- a can be 0 or more




# + Plus 1+ occurance of preceding elements
# ? Question mark ... 0/1 occurance

# {}  braces 







