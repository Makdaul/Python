'''
n = int(input('Введите число: '))
i = 1
result = 1
while i <= n:
    result *= i
    i += 1

print(result)
'''

'''
n = int(input('Ввидите число: '))
n0 = 0
n1 = 0
n2 = 1
i = 2

while n0 < n:
    n0 = n1 + n2
    n1 = n2
    n2 = n0
    i += 1
    if n0 > n:
        i = -1
print(i)
'''

'''
n = int(input('Ввидите кол-во дней: '))
k = 0
max = 0
for i in range(n):
    x = int(input('Введите t: '))
    if x > 0:
        k += 1
    else:
        if max < k:
            max = k
        k = 0

print(max)
'''

n = int(input('Введите кол-во арбузов: '))
max = -1
min = 30001

for i in range(n):
    x = int(input('Введите вес арбуза: '))
    if x > max:
        max = x
    if x < min:
        min = x

print(max, min)