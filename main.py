import slack_connect
from config import Config

def main():
    
    slack_client = slack_connect.SlackClient()
    user_info = slack_client.get_user_by_email('ivangarcialaverde@gmail.com')
    user_id = user_info["id"]
    slack_client.post_message_to_channel(channel=user_id, message="hello ivan")

if __name__ == "__main__":
    main()
