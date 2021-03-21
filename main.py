import slack_connect
from config import Config
import server
from server import SlackServer

# ---------------------------- #
#           non-server         #
# ---------------------------- #

def main():
    slack_server = SlackServer()
    slack_server.send_check_box()
    slack_server.app.run(debug=True)

if __name__ == "__main__":
    main()