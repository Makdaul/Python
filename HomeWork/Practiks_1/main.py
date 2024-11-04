# Задание №1

a = 8
b = 10
c = 12
d = 18

divider = ((-3 + a ** 2) * b - 2 ** 3)

divisible = (c - 2 * d)

res = divider / divisible

print(res)

# Задание №2

min = int(input('Введите количество минут: '))

hours = min // 60

minutes = min % 60

print(f'{hours} часов и {minutes} минут')

# Задание №3

n = int(input('Введите номер билета: '))

n1 = n // 100000
n2 = (n % 100000) // 10000
n3 = (n % 10000) // 1000
n4 = (n % 1000) // 100
n5 = (n % 100) // 10
n6 = n % 10

if n1 + n2 + n3 == n4 + n5 + n6:

    print('Билет счастливый')

else:

    print('Билет несчастливый')

# Задача №4

katet_1 = int(input('Введите длину первого катета: '))

katet_2 = int(input('Введите длину второго катета: '))

square = katet_1 * katet_2 / 2

print(f'Площадь прямоугольного треугольника: {square}')

#Задача №5

a = int(input('Введите первое число: '))

b = int(input('Введите второе число: '))

print(a, b)

a = a + b

b = a - b

a = a - b

print(a, b)