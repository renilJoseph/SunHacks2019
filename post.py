import json
import requests
#url = 'https://shsh-253710.appspot.com/test'
#url = 'https://newsunhack.appspot.com/test'
url = 'http://localhost:5000/test'
files = {'media': open('/Users/renil.joseph/Documents/github/sunhacks/renil.jpg', 'rb')}
response = requests.post(url, files=files)
#json_data = json.loads(response.text)
print(response.text)
