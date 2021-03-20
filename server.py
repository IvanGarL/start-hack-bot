# ---------------------------- #
#           server             #
# ---------------------------- #
import json
from flask import Flask, request
from slackeventsapi import SlackEventAdapter
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_sdk.web import SlackResponse
import time
import re
from data_jsons import recommendations, recommendation_buttons
from client_preferences import ClientPreferences

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(
    os.environ['SIGNING_SECRET'], '/slack/events', app)

client = WebClient(token=os.environ['SLACK_OAUTH_ACCESS_TOKEN'])
BOT_ID = client.api_call("auth.test")['user_id']
client_preferences = ClientPreferences()


@app.route('/slack/interactions', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        client_preferences.update_recommendations_options(
            request.form['payload'])
    if request.method == 'GET':
        print('GET')
    return ('', 204)
    

class SlackServer(object):
    def __init__(self, token=None):
        print('init slackserver')

    def send_check_box(self):
        result = client.chat_postMessage(
            channel='#test', text="Recommendations", blocks=recommendations)

    @slack_event_adapter.on('app_mention')
    def app_mention(payload):
        print('ok')

    @slack_event_adapter.on('message')
    def message(payload):
        event = payload.get('event', {})
        channel_id = event.get('channel')
        user_id = event.get('user')
        text = event.get('text')

        print(' ok?')

        if(BOT_ID != user_id):
            if('timer' in text):
                response = 'how long?'
                client.chat_postMessage(channel='#test', text=response)
            elif('seconds' in text):
                times_up = False
                print('text: ', text)
                response = 'The timer startded!'
                time_in_s = [int(s) for s in re.findall(r'\b\d+\b', text)][0]

                client.chat_postMessage(channel='#test', text=response)
            else:
                print('nothng')
