
start_text = "Welcome to *HomeFocus* :wave: Ready to get *focused*? Simply choose a feature " + \
    "that might help you *focus*. :raised_hands: \n\n"

end_text = "If you have any questions, check out the Frequently Asked Questions or email us at Focus@Home"
		


recommendation_buttons = [{
    "type": "section",
    "text": {
            "type": "mrkdwn",
        "text": "1. To-Do Lists Create Order \n"+\
			"2. To-Do Lists Help You Create Accountability\n" +\
				"3. To-Do Lists Help Relieve Your Stress\n" +\
					"4. You get the point :wink:"
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
            "text": "The timer can provide motivation as the employee can try to “beat” the clock. Some employees respond better to an object setting boundaries than an adult telling them what to do."
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
            "text": "It reduces distractions and improves focus. Music helps boost motivation when starting a new task. It is beneficial to listen to something you are familiar with for focusing intensely on your project. Researchers recommend listening to instrumental music if you want to hear music while working."
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
            "text": "Want to feel like you are just at your work?"
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
            "text": "keep each other company and keep yourselves accountable while you work."
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

divider = [{
  "type": "divider"
}]

start = [{
        "type": "section",
        "text": {
                "type": "mrkdwn",
                "text": start_text
        },
    },]

end = [{
        "type": "section",
        "text": {
                "type": "mrkdwn",
                "text": end_text
        },
    },]

recommendations = start + divider + recommendation_buttons + divider+ end
