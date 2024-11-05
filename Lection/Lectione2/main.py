'''
list_1 = []
list_1 = list()
list_1 = [1, 2, 3, 4, 5]
#print(*list_1)
for i in list_1:
    print(i)

print(len(list_1))
print(list_1[0])


list_1 = [1, 5]
print(list_1)

list_1.append(8)
print(list_1)


list_1 = []
print(list_1)
for i in range(5):
    list_1.append(i)
    print(list_1)


list_1 = [1, 2, 3, 4, 5]
print(list_1.pop())
print(list_1)

list_1 = [1, 2, 3, 4, 5]
print(list_1.pop(0))
print(list_1)

list_1 = [1, 2, 3, 4, 5]
print(list_1.insert(2, 11))
print(list_1)

t = ()
print(type(t))

t = (1, 2, 3, 4,)
print(type(t))

v = [1, 8, 9]
print(v)
print(type(v))

v = tuple(v)
print(v)
print(type(v))

a,b,c = v

print(a, b, c)


t = (1, 2, 3, 4,)

for i in t:
    print(i)
'''

d = {}
d = dict()

d['q'] = 'qwerty'
print(d)

d['w'] = 'werty'
print(d)
print(d['q'])

dictionary = {}
dictionary = {'up': '^', 'left': '<', 'right': '>'}

print(dictionary.items())
for (k, v) in dictionary.items():
    print(k, v)