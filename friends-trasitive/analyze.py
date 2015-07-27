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


def read_or_get_friends(uid):
    if os.path.isfile(str(uid) + '.txt'):
        return read_friends(uid)
    friends = get_friends(uid)
    dump(uid, friends)
    return friends


out = open('283148693-result.txt','w')
my_friends = [283148693] #set(get_friends('283148693'))
for uid in my_friends:
    user_friends = set(read_or_get_friends(uid))
    direct_friends = set()
    count = 0
    for fid in user_friends:
        friend_friends = set(read_or_get_friends(fid))
        for common_fid in friend_friends.intersection(user_friends):
            direct_friends.add(common_fid)

    d = len(direct_friends)
    t = len(user_friends)
    if t > 0:
        res = '%(id)d\t%(direct)d\t%(total)d\t%(percent).2f%%' % {'id': uid,
                                                                  'direct': d,
                                                                  'total': t,
                                                                  'percent': d * 100.0 / t}
        out.write(res + '\n')
        print res
out.flush()
out.close()