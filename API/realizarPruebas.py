import requests

r = requests.get('http://' + 'localhost:21' + '/login.cgi', headers=headers, verify=False, timeout=2)
