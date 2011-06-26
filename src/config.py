#Configuration file for IRC Bot
import os

#internals
owner = [
        'paullik',
        'foobarfoo',
        ]
search = "http://google.ro"

#connection and authentication
server = 'chat.freenode.net'
port = 6667

nick = 'PPyBot'
realName = 'Paul Python Bot'

channel = '#ppybot'

#messages
quit_msg = 'Bye bye'

#log directory
log = os.getcwd() + os.sep + '..' + os.sep + 'logs' + os.sep

#commands list
c_lst = [
        'search',
        'wiki',
        'quit',
        'answer',
        ]

#standard messages
nick_auth = 'NICK ' + nick + '\r\n'
user_auth = 'USER ' + nick + ' ' + nick + ' ' + nick + ' :' + realName + '\r\n'

channel_join = 'JOIN ' + channel + '\r\n'
channel_part = 'PART ' + channel + ' :' + quit_msg + '\r\n'

privmsg = 'PRIVMSG ' + channel + ' :'

quit = 'QUIT\r\n'

#connection should stay alive
alive = True

