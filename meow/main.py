from pprint import pprint
import sys
from slacker import Slacker

from config import API_TOKEN, BOT_USERNAME, BOT_ICON_EMOJI, BOT_ICON_URL


if __name__ == '__main__':
    slack = Slacker(API_TOKEN)
    msg = sys.argv[1] if len(sys.argv) > 1 else 'mrowr?'
    response = slack.chat.post_message(
        '#bot_tests', msg, username=BOT_USERNAME,
        icon_emoji=BOT_ICON_EMOJI, icon_url=BOT_ICON_URL)
    pprint(response.__dict__)
