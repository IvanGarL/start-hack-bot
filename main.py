import slack_connect
from config import Config

# ---------------------------- #
#           server             #
# ---------------------------- #

from flask import Flask
from slackeventsapi import SlackEventAdapter
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_sdk.web import SlackResponse

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(
    os.environ['SIGNING_SECRET'], '/slack/events', app)

client = WebClient(token=os.environ['SLACK_OAUTH_ACCESS_TOKEN'])
# client.chat_postMessage(channel='#test', text="Hello world!")

@slack_event_adapter.on('message')
def message(payload):
    print('test?')
    event = payload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')

    client.chat_postMessage(channel='#test', text=text)


# ---------------------------- #
#           non-server         #
# ---------------------------- #

def main():
    slack_client = slack_connect.SlackClient()
    user_info = slack_client.get_user_by_email('mariahendrikx@gmail.com')
    user_id = user_info["id"]
    slack_client.post_message_to_channel(channel=user_id, message="Maria")


if __name__ == "__main__":
    app.run(debug=True)
    # main()
