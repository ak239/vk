from time import sleep

__author__ = 'kozyatinskiy'

import urllib2
import json

"https://oauth.vk.com/authorize?client_id=CLIENT_ID&scope=messages&redirect_uri=https://oauth.vk.com/blank.html&display=mobile&v=5.34&response_type=token"

TOKEN = "HERE_TOKEN"
REQUEST_URL = "https://api.vk.com/method/messages.getHistory?offset={0}&count=200&chat_id={1}&version=5.34&access_token=" + TOKEN

f = open('messages.txt', 'w')

# noinspection PyBroadException
def get_messages(offset, chat):
    for k in range(0, 10):
        try:
            response = urllib2.urlopen(REQUEST_URL.format(offset, chat))
            data = json.loads(response.read())
            messages = data['response']
            print '{0}/{1} {2}'.format(offset, messages[0], offset * 1.0 / messages[0])
            if len(messages) > 1:
                for i in range(1, len(messages)):
                    f.write(json.dumps(messages[i]) + '\n')
                return True
            return False
        except:
            print 'error'
        sleep(1)
    return False


offset = 0
while get_messages(offset, 88):
    offset += 200
    # exit(0)

f.flush()
f.close()