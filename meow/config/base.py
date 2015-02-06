import os

# set API token as environment variable or in local config
API_TOKEN = os.getenv('SLACK_MEOW_BOT_API_TOKEN')

BOT_USERNAME = 'meow'
BOT_ICON_EMOJI = 'cat'
BOT_ICON_DIR = 'https://s3-us-west-2.amazonaws.com/slack-files2/avatars/'
BOT_ICON_URL = '{}2015-02-06/3644035180_b2b02bb5d4db2a6a41fa_48.jpg'.format(
    BOT_ICON_DIR)

try:
    from config.local import *
except ImportError:
    pass
