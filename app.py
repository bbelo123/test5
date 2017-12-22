import requests

text_string = 'What a wonderful day'

r = requests.post('http://text-processing.com/api/sentiment/', data={'text': text_string})
json_response = r.json()
label = json_response['label']

print (json_response)
print (label)