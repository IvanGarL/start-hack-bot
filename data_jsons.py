
start_text = "Welcome to HomeFocus :wave: Ready to get focused? Simply choose a feature " + \
				"that might help you focus. :raised_hands:"

recommendations_options = [
					{
						"value": "v_music",
						"text": {
							"type": "plain_text",
							"text": "Play Focus Music"
						}
					},
					{
						"value": "v_desk_sounds",
						"text": {
							"type": "plain_text",
							"text": "Play Desk Sounds"
						}
					},
					{
						"value": "v_todo",
						"text": {
							"type": "plain_text",
							"text": "Create a To-Do list!"
						}
					},
					{
						"value": "v_working_companion",
						"text": {
							"type": "plain_text",
							"text": "Have a working companion!"
						}
					}
				]

recommendations = [
		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": start_text
			},

			"accessory": {
				"type": "checkboxes",
				"action_id": "this_is_an_action_id",
				"options": recommendations_options
			}
		}
	]