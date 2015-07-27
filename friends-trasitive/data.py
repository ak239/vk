__author__ = 'kozyatinskiy'

URL_TEMPLATE = "https://api.vk.com/method/%(method)s?%(parameters)s"
FRIENDS_GET_TEMPLATE = URL_TEMPLATE % {'method': 'friends.get', 'parameters': 'user_id=%(user_id)d'}

import urllib
import json
import time
import os.path


def read_friends(uid):
    f = open(str(uid) + '.txt', 'r')
    friends = []
    for fid in f:
        friends.append(int(fid))
    f.close()
    return friends


def get_friends(uid):
    raw_answer = urllib.urlopen(FRIENDS_GET_TEMPLATE % {'user_id': uid})
    time.sleep(0.2)
    answer = json.loads(raw_answer.read())
    if 'response' in answer:
        return answer['response']
    print answer
    return []


def dump(uid, friends):
    f = open(str(uid) + '.txt', 'w')
    for friend in friends:
        f.write(str(friend) + '\n')
    f.flush()
    f.close()


queue = read_friends('test')
# queue = [182732]
already = set()
# add_amount =0 256
add_amount = 0
while len(queue) > 0:
    id = queue.pop()
    if id in already:
        continue

    already.add(id)

    friends = []
    if os.path.isfile(str(id) + '.txt'):
        if add_amount > 0:
            friends = read_friends(id)
    else:
        friends = get_friends(id)
        dump(id, friends)

    if add_amount > 0:
        queue = friends + queue
        add_amount -= 1

    if len(queue) < 100 or len(queue) % 100 == 0:
        print id
        print str(len(queue)) + ' left'

print 'finished'