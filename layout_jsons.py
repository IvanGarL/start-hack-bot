home_blocks = [
    {
        # Section with text and a button
        'type': "section",
        'text': {
            'type': "mrkdwn",
            'text': "*Welcome!* \nThis is a home for Stickers app. You can add small notes here!"
        },
        'accessory': {
            'type': "button",
            'action_id': "add_note",
            'text': {
                'type': "plain_text",
                'text': "Add a Stickie"
            }
        }
    },
    # Horizontal divider line
    {
        'type': "divider"
    }
]

home_view = {
    'type': 'home',
    'title': {
        'type': 'plain_text',
        'text': 'Keep notes!'
    },
    'blocks': home_blocks
}
