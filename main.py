import slack_connect
from config import Config
import server
from server import app, send_check_box

# ---------------------------- #
#           non-server         #
# ---------------------------- #

def main():
    # slack_client = slack_connect.SlackClient()
    # user_info = slack_client.get_user_by_email('mariahendrikx@gmail.com')
    # user_id = user_info["id"]
    # slack_client.post_message_to_channel(channel=user_id, message="Maria")
    send_check_box()


if __name__ == "__main__":
    main()
    app.run(debug=True)
