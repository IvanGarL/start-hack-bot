# ---------------------------- #
#           server             #
# ---------------------------- #

from flask import Flask
from slackeventsapi import SlackEventAdapter
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_sdk.web import SlackResponse
import time
import re
from data_jsons import recommendations

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(
    os.environ['SIGNING_SECRET'], '/slack/events', app)

client = WebClient(token=os.environ['SLACK_OAUTH_ACCESS_TOKEN'])
BOT_ID = client.api_call("auth.test")['user_id']


@slack_event_adapter.on('message')
def message(payload):
    event = payload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')
    times_up = True

    if(BOT_ID != user_id):
        if('timer' in text):
            response = 'how long?'
            client.chat_postMessage(channel='#test', text=response)
        elif('seconds' in text and times_up):
            times_up = False
            print('text: ', text)
            response = 'The timer started!'
            time_in_s = [int(s) for s in re.findall(r'\b\d+\b', text)][0]

            client.chat_postMessage(channel='#test', text=response)
            # time.sleep(time_in_s)
            response = 'Time is up!'
            client.chat_postMessage(channel='#test', text=response)
        else:
            text = ''
            client.chat_postMessage(channel='#test', text=text)


def send_check_box():
    # Post the message to Slack, storing the result as `res`

    result = client.chat_postMessage(channel='#test', text="Recommendations", blocks=recommendations)
    print(result)
