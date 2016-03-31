import requests
import json
import sys, os
sys.path.append('..')
import config

unique_database = str(config.auth[0])
def getResponse(input_message):
    url = 'http://facerecog.io:12000/chatbot/%s' % unique_database
    payload = {"message":input_message}
    r = requests.post(url, json=payload)
    return r.text
