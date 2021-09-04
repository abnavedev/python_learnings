#HTTP Requests - requests library 

# HTTP protocol  - clinet(Web browser) - send HTTP requests to a server

# GET and POST request
# GET request - TO request data from specific server
# POST request - to send user data to a host server for processing, update datbas


#For example, if you search "xyz", browser sends a GET request to Google server by appending the query string to the url. url in your address bar, you should see something like: https://www.google.com/search?q=xyz


# Http Request Methods – GET POST PUT DELETE HEAD PATCH

# in Python we need requests module for making http request
# pip install requests
# Requests Module-  provides funcationalities form managing reuest and response

# Response object  - When a request is made to a URL... It returns a resposne
# In python Reponse object is rturned by request.method() #method being get post etc
# reponse obect.... lot of functions and attributes
# Eg response.status_code


import requests

# making a request 
# built-in methods to make HHT req to a URL

# get method-    to retrive information from a specified server givern a URL
# get methd - ? char.. encoded user info appended withthe page req

res =  requests.get("https://github.com/abnavedev/python_learnings")
#response 

# print(res.text)
print(res.url)
print(res.status_code)


# GET - 
#POST reuest 
# PUt
# Delete 

# RESPONSe OBJECT
# request.method() --- get put post
# return repinse object
# status code
# header
# close
# url
# text
# content 
# Authentication using Python Requests

# Can implement web scrapping with BeautifulSoup

