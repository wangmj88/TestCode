from random import randint
from collections import Counter
data = [randint(0,20) for _ in range(30)]
print(data)

d = dict.fromkeys(data,0)
print(d)

for x in data:
    d[x] += 1
print(d)#{19: 4, 5: 2, 6: 3, 11: 3, 14: 3, 12: 1, 4: 2, 2: 5, 15: 1, 7: 1, 16: 1, 8: 1, 1: 1, 13: 1, 17: 1}

s =sorted(((v,k) for k, v in d.items()),reverse = True)
print(s)#[(5, 2), (4, 19), (3, 14), (3, 11), (3, 6), (2, 5), (2, 4), (1, 17), (1, 16), (1, 15), (1, 13), (1, 12), (1, 8), (1, 7), (1, 1)]
print(s[:3])#[(5, 2), (4, 19), (3, 14)]

import heapq
p = heapq.nlargest(3,s)
print(p)#[(5, 2), (4, 19), (3, 14)]

from collections import Counter
c=Counter(d)
print(c.most_common(3))#[(6, 3), (11, 3), (12, 3)]