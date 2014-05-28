# submitting to a web form

import requests

url = 'http://httpbin.org/post'
data = {'fname': 'Nicholas', 'lname': 'Johnson'}

# submit post requests
r = requests.post(url, data=data)

# display the response to screen
print r.content