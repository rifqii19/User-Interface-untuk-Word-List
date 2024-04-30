import requests

api_key = '93e97a84-1492-46a7-85f1-418b8cca2b0e'
word = 'Potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for defenition in definitions:
    print(defenition)