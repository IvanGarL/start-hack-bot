
start_text = "Welcome to HomeFocus :wave: Ready to get focused? Simply choose a feature " + \
    "that might help you focus. :raised_hands:"

recommendation_buttons = [{
    "type": "section",
    "text": {
            "type": "mrkdwn",
        "text": "Create a To-Do-List!"
    },
    "accessory": {
        "type": "button",
        "text": {
                "type": "plain_text",
            "text": "Create a To-Do List!"
        },
        "value": "v_todo",
        "action_id": "v_todo"
    },
}, {
    "type": "section",
    "text": {
            "type": "mrkdwn",
            "text": "Create a To-Do-List!"
    },
    "accessory": {
        "type": "button",
        "text": {
                "type": "plain_text",
                "text": "Timer Time!"
        },
        "value": "v_timer",
        "action_id": "v_timer"
    },
}, {
    "type": "section",
    "text": {
            "type": "mrkdwn",
            "text": "Create a To-Do-List!"
    },
    "accessory": {
        "type": "button",
        "text": {
                "type": "plain_text",
                "text": "Play Focus Music"
        },
        "value": "v_music",
        "action_id": "v_music"
    },
}, {
    "type": "section",
    "text": {
            "type": "mrkdwn",
            "text": "Create a To-Do-List!"
    },
    "accessory": {
        "type": "button",
        "text": {
                "type": "plain_text",
                "text": "Working Sounds!"
        },
        "value": "v_work_sounds",
        "action_id": "v_work_sounds"
    },
}, {
    "type": "section",
    "text": {
            "type": "mrkdwn",
            "text": "Create a To-Do-List!"
    },
    "accessory": {
        "type": "button",
        "text": {
                "type": "plain_text",
                "text": "Have a working companion!"
        },
        "value": "v_work_companion",
        "action_id": "v_work_companion"
    },
}, ]

recommendations = [
    {
        "type": "section",
        "text": {
                "type": "mrkdwn",
                "text": start_text
        },
    },
] + recommendation_buttons
