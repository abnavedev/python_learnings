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




# + PLUS 1+ occurance of preceding elements
# ? Question mark ... 0/1 occurance

# {}  Braces {n,m}  atleast n and at most m repetitions
# a{2,5}   a can be 2 to 5


# Examples
# [0-9]{2,4}

# | Alteranation Vertical bar(or operator)
# a|b  match to string either contains a or b



# Group  () - used to group sub patterns 
# (a|b|c)xyz -- match to a string a or b or c xyz



# \ backslash -  escape char include all metachars
# \$a  -  match to a sstrinf contains $ followdd by a. $ is not intepereted in a speical way


# SPECIAL SEQUENCES
# \Athe   --- at the start 
# \bxyz ------ at the start or  xyz\b  at the endend
# \B opposite of \b
# \d match to any decial digit eql [0-9]
# \D match to any non decial digit eql [^0-9]
# \s - match to string anywhitespace chars [\t\n\r\f\v]
# \S match to non-white char cotn [^\t\n\r\f\v]
# \w matchs to alphnuchars  [a-zA-Z0-9_] underscore _ is also considered an alphanumeric char
# \W matchs to non-apa char [^a-zA-Z0-9_]
# \Z - Matches if the specified characters are at the end of a strin

# Python RegEx

import re

# re.findall() - returns a list of all matchs

# Program to extract numbers from a string

string = "hello 12 hi 89. Howdy 34"

pattern = '\d+'
#pattern = '[0-9]+'


res = re.findall(pattern,string)

print(res)
print(type(res))

# re.split() - split the string where there is a mtach ,returns list of string

str = "Twelve:12 Eight nine:89"
patt = '\d+'
result = re.split(patt,str)
print(result)

# maxsplit argument that will occur , default 0 all possible split
result = re.split(patt,str,1)
print(result)


# re.sub() - resub(pattern,replace, string)


# Program to remove all whitespaces
# multiline string
str = 'abc 12\
de 23 \n f45 6'
# matches all whitespace characters
pattern = '\s+'
replace = ''

print(str) 

new_string = re.sub(pattern, replace, str)  ## count as a fourth parameter
print(new_string)

new_string = re.sub(pattern, replace, str,3)  ## count as a fourth 
# o default - replace all occurane
print(new_string)

#re.subn() is similar to re.sub() 
# it returns a tuple of 2 . new string and np. of substition

new_string = re.subn(pattern, replace, string) 
print(new_string)


# re.search(pattern, string) looks for first occurance of pattern matach
# return a match object or None
#  - 

string = "hello this is test string"
# check if 'hello' is at the beginning
match = re.search('\Ahello', string)
#match object
if match :
        print("pattern found")
else :
    print("pattern not found")


# Match object
# print(dir(match)) # It returns the list of valid attributes od match oject

##match.group() # returns the part of string where there is a matach



string = '39801 356, 2102 1111'


# Three digit number followed by space followed by two digit number
pattern = '(\d{3}) (\d{2})'
# match variable contains a Match object.
match = re.search(pattern, string) 

if match:
    
    print(match.group())
else:
    print("pattern not found")


#match.start(), match.end() and match.span()
#match.re and match.string
#Using r prefix before RegEx