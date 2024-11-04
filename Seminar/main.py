'''
n = int(input())
m = int(input())

print(m + n - 1//n)
'''

'''
a = int(input())
b = int(input())
c = int(input())

s1=((a + 1)//2)
s2=((b + 1)//2)
s3=((c + 1)//2)

print(s1 + s2 + s3)
'''

'''
i = int(input())
j = int(input())

if i - j == 0:
    print(-1)
else:
    print(i + j -1)
'''

n = int(input())

if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print("YES")
else:
    print("NO")