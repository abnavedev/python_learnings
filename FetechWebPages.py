#Python - HTTP Requests

# HTTP protocol  - clinet(Web browser) - send HTTP requests to a server

# GET and POST request
# GET request - TO request data from specific server
# POST request - to send user data to a host server for processing, update datbas


#For example, if you search "xyz", browser sends a GET request to Google server by appending the query string to the url. url in your address bar, you should see something like: https://www.google.com/search?q=xyz


# Http Request Methods – GET POST PUT DELETE HEAD PATCH

# in Python we need requests module for making http request
# pip install requests

# Response object  - When a request is made to a URL... It returns a resposne
# In python Reponse object is rturned by request.method() #method being get post etc
# reponse obect.... lot of functions and attributes
# Eg response.status_code


import requests

# making a request 
res =  requests.get("https://github.com/abnavedev/python_learnings")
#response 

# print(res.text)
print(res.url)
print(res.status_code)

# Authentication using Python Requests

