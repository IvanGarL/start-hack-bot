import os
import json

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_sdk.web import SlackResponse
from config import Config
from data_jsons import recommendations_options

class ClientPreferences(object):
    def __init__(self):
        print('initing ClientPreferences')
        self.checkvalues = []
        for element in recommendations_options:
            self.checkvalues.append({'value': element['value'], 'status': False})
        

    def update_recommendations_options(self, data):
        try:
            data = json.loads(data)
            data = data['message']['blocks'][0]['accessory']['options']
            for element in data:
                print(element)
        except SlackApiError as e:
            # You will get a SlackApiError if "ok" is False
            print(f"Got an error: {e.response['error']}")

