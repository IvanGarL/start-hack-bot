
start_text = "Welcome to HomeFocus :wave: Ready to get focused? Simply choose a feature " + \
				"that might help you focus. :raised_hands:"

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
				"options": [
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
			}
		}
	]

todo_modal = {
	"type": "modal",
	"title": {
		"type": "plain_text",
		"text": "Create a task :scroll:",
		"emoji": True
	},
	"submit": {
		"type": "plain_text",
		"text": "Submit",
		"emoji": True
	},
	"close": {
		"type": "plain_text",
		"text": "Cancel",
		"emoji": True
	},
	"blocks": [
		{
			"type": "input",
			"block_id": "my_block",
			"element": {
				"type": "plain_text_input",
				"action_id": "my_action"
			},
			"label": {
				"type": "plain_text",
				"text": "what task do you want to add?",
				"emoji": True
			}
		}
	]
}