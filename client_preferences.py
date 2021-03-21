import os
import json

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_sdk.web import SlackResponse
from config import Config
from data_jsons import recommendation_buttons

class ClientPreferences(object):
    def __init__(self):
        print('initing ClientPreferences')
        self.checkvalues = {}
        for element in recommendation_buttons:
            self.checkvalues[element['accessory']['value']] = False
        

    def update_recommendations_options(self, data):
        try:
            data = json.loads(data)
            print(data['type'] == 'block_actions')
            data_id = data['actions'][0]['action_id']

            self.checkvalues[data_id] = not(self.checkvalues[data_id])
            return data_id

        except SlackApiError as e:
            # You will get a SlackApiError if "ok" is False
            print(f"Got an error: {e.response['error']}")

            

    def get_client_preference(self):
        return self.checkvalues

