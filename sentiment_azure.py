from pprint import pprint
import requests
import os
import json


def sentiment(bunch):
    
    documents = {'documents':[]}
    for i,element in zip(range(1,len(bunch)+1),bunch):
        documents['documents'].append(
            {
                'id':str(i),
                'language':'en',
                'text':element['text']
            }
        )

    headers = {
    "Content-Type":"application/json",
    "Ocp-Apim-Subscription-Key":os.environ['AZURE_KEY']
    }
    uri = 'https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment'

    r = requests.post(uri,json=documents,headers=headers)
    data = json.loads(r.text)
    for i,response in enumerate(data['documents']):
        bunch[i]['sentiment'] = response['score']
    


    return bunch
