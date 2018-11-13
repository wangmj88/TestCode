from random import randint
d = {k:randint(50,100) for k in 'abcdefgh'}
l =[(v,k) for k,v in d.items()]
print(sorted(l,reverse = True))
print('#'*20)
print(sorted(list(zip(d.values(),d.keys())),reverse = True))
print(sorted(d.items(),key = lambda x:x[1],reverse=True))
p =sorted(d.items(),key = lambda x:x[1],reverse=True)

print('enumerate------------------------------')
#增加排名次序 enumerate
print(p)#[('d', 99), ('a', 96), ('c', 88), ('e', 77), ('h', 74), ('b', 70), ('f', 70), ('g', 51)]
print(list(enumerate(p)))#[(0, ('d', 99)), (1, ('a', 96)), (2, ('c', 88)), (3, ('e', 77)), (4, ('h', 74)), (5, ('b', 70)), (6, ('f', 70)), (7, ('g', 51))]
print(list(enumerate(p,1)))#[(1, ('d', 78)), (2, ('c', 69)), (3, ('a', 66)), (4, ('e', 66)), (5, ('f', 65)), (6, ('b', 64)), (7, ('g', 63)), (8, ('h', 51))]
for i,(k, v) in enumerate(p, 1):
    print(i, (k, v))
    '''
        1 ('f', 98)
        2 ('c', 90)
        3 ('b', 86)
        4 ('d', 83)
        5 ('a', 74)
        6 ('h', 74)
        7 ('g', 73)
        8 ('e', 53)
    '''
for i, (k, v) in enumerate(p, 1):
    d[k] = (i,v)
print(d) #{'a': (1, 100), 'b': (7, 68), 'c': (5, 79), 'd': (8, 59), 'e': (4, 80), 'f': (2, 92), 'g': (3, 84), 'h': (6, 75)}