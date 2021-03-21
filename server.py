# ---------------------------- #
#           server             #
# ---------------------------- #
from flask import Flask, request, Response
from slackeventsapi import SlackEventAdapter
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_sdk.web import SlackResponse
import time
import re
import data_jsons
from config import Config
import json
from client_preferences import ClientPreferences
from tasksbuffer import TaskBuffer


client = WebClient(token=os.environ['SLACK_OAUTH_ACCESS_TOKEN'])
BOT_ID = client.api_call("auth.test")['user_id']
client_preferences = ClientPreferences()
tasksbuffer = TaskBuffer()
class SlackServer(object):
    app = Flask(__name__)
    slack_event_adapter = SlackEventAdapter(
        Config.SIGNING_SECRET, '/slack/events', app)

    def __init__(self, token=None):
        print('init slackserver')

    @app.route('/interactive', methods=['POST'])
    def interactive():
        payload = json.loads(request.form["payload"])
        user_id = payload['user']['id']
        if(BOT_ID != user_id and payload['type'] == 'view_submission'):
            task = payload['view']['state']['values']['my_block']['my_action']['value']
            todolist_update =  tasksbuffer.addTask(task)
            client.chat_postMessage(channel="#todo-list", text=todolist_update)
        elif(BOT_ID != user_id and payload['type'] == 'block_actions'):
            try:
                btn_id = client_preferences.update_recommendations_options(
                    request.form['payload'])
                if(btn_id == 'v_deep_focus'):
                    print('btn change')
            except Exception as e:
                return ('', 204)
        return Response()

    @app.route('/slashcommand', methods=['GET', 'POST'])
    def slashcommand():
        print(request.form["trigger_id"])
        client.views_open(trigger_id=request.form["trigger_id"], view=json.dumps(data_jsons.todo_modal))
        return Response()

    def send_check_box(self):
        result = client.chat_postMessage(channel='#test', text="Recommendations", blocks=data_jsons.recommendations)

    @slack_event_adapter.on('message')
    def message(payload):
        event = payload.get('event', {})
        channel_id = event.get('channel')
        user_id = event.get('user')
        text = event.get('text')

        print(' ok?')

        if(BOT_ID != user_id):
            times_up = True
            if('timer' in text):
                response = 'how long?'
                client.chat_postMessage(channel='#test', text=response)
            elif('seconds' in text):
                times_up = False
                print('text: ', text)
                response = 'The timer started!'
                time_in_s = [int(s) for s in re.findall(r'\b\d+\b', text)][0]

                client.chat_postMessage(channel='#test', text=response)
            else:
                print('nothng')