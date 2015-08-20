import os
import os.path
import time
import logging

# some commands can be executed only if the user's nick is found in this list
owner = 'Tsu'

owner_email = "Tsu@example.com"

# server to connect to
server = 'irc.example.com'
# server's port
port = 6667

# bot's nicknames
nicks = list(set(['TsuBot']))
# bot's real name
real_name = 'Tsu Bot'

# channels to join on startup
channels = list(set([
    '#Tsu'
]))

cmds = {
    # core commands list, these commands will be run in the same thread as the bot
    # and will have acces to the socket that the bot uses
    'core': list(set([
    ])),

    # normal commands list, the ones that are accessible to any user
    'user': list(set([
    ])),

    # commands list that the bot will execute even if a human didn't request an
    # action
    'auto': list(set([
    ])),

    # commands list that the bot will execute even if a human didn't request an
    # action and will have acces to the socket that the bot uses
    'auto-core': list(set([
        'email_alert',
    ])),
}

# smtp server for email_alert
smtp_server = 'localhost'
smtp_port = 25
from_email_address = 'irc@example.com'

# users should NOT modify below!
log = os.path.join(os.getcwd(), '..', 'logs', '')
logging_level = logging.DEBUG
start_time = time.time()
current_nick = ''
