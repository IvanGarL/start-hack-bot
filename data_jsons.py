
start_text = "Welcome to HomeFocus :wave: Ready to get focused? Simply choose a feature " + \
    "that might help you focus. :raised_hands:"

recommendation_buttons = [
    {
        "type": "button",
        "text": {
            "type": "plain_text",
            "text": "Create a To-Do List!"
        },
        "value": "v_todo",
        "action_id": "v_todo"
    },
    {
        "type": "button",
        "text": {
            "type": "plain_text",
            "text": "Play Focus Music"
        },
        "value": "v_music",
        "action_id": "v_music"
    },
	{
        "type": "button",
        "text": {
            "type": "plain_text",
            "text": "Play Sounds that makes you feel at work!"
        },
        "value": "v_work_sounds",
        "action_id": "v_work_sounds"
    },
	{
        "type": "button",
        "text": {
            "type": "plain_text",
            "text": "Have a working companion!"
        },
        "value": "v_work_companion",
        "action_id": "v_work_companion"
    },
]

recommendations = [
	{
  "type": "section",
  "text": {
    "type": "mrkdwn",
    "text": start_text
  }
},
    {
        "type": "actions",
        "block_id": "actionblock789",
        "elements": recommendation_buttons
    }
]
