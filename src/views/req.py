import requests
import json

def getResponse(input_message):
    url = 'http://facerecog.io:12000/chatbot/wikimon'
    payload = {"message":input_message}
    r = requests.post(url, json=payload)
    return r.text


