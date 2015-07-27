# -*- coding: utf-8 -*-

from collections import defaultdict
from math import fmod, floor

__author__ = 'kozyatinskiy'

import json

f = open('messages.txt', 'r')

# period = 29.530589
# start = 1398751983 - period / 2.0
# intervals = 8
# per_interval = period / intervals

period = 24 * 60 * 60
start = 1398729600
intervals = 24
per_interval = period / intervals

count = defaultdict(int)

for raw in f:
    msg = json.loads(raw)['body']
    if u'боян' in msg or u'баян' in msg:
        print msg
        count[json.loads(raw)['from_id']] += 1
    # break
    # count[json.loads(raw)['from_id']] += 1
    # count[int(floor(fmod(json.loads(raw)['date'] - start, period) / per_interval))] += 1
f.close()


#
out = open('output.txt', 'w')

for k in count:
    out.write('{0}\t{1}\n'.format(k, count[k]))

out.flush()
out.close()
