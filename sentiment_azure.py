from pprint import pprint
import requests

uri = 'https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment'

documents = {'documents' : [
  {'id': '1', 'language': 'en', 'text': 'I fucking hate niggers'},
  {'id': '2', 'language': 'en', 'text': 'I had a terrible time at the hotel. The staff was rude and the food was awful.'},  
  {'id': '3', 'language': 'es', 'text': 'Los caminos que llevan hasta Monte Rainier son espectaculares y hermosos.'},  
  {'id': '4', 'language': 'es', 'text': 'La carretera estaba atascada. Había mucho tráfico el día de ayer.'}
]}

headers = {
    "Content-Type":"application/json",
    "Ocp-Apim-Subscription-Key":"7844eae8f47c4d7e857caa4b42c20286"
}

r = requests.post(uri,json=documents,headers=headers)
print(r.text)