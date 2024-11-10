#Задача 1
videoCardsNumber = int(input('Введите количество видеокарт: '))
videoCards = []
newVideoCardsList = []
maxItem = 0

for item in range(videoCardsNumber):
    videoCards.append(int(input(f'Видеокарта {item + 1}: ')))
    if videoCards[item] > maxItem:
        maxItem = videoCards[item]

for item in range(videoCardsNumber):
    if videoCards[item] != maxItem:
        newVideoCardsList.append(videoCards[item])

print()
print('Старый список видеокарт: [', end=' ')
for item in range(videoCardsNumber):
    print(videoCards[item], end=' ')
print(']')

print('Новый список видеокарт: [', end=' ')
for item in range(len(newVideoCardsList)):
    print(newVideoCardsList[item], end=' ')
print(']')

#Задача 2
films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
my_list = []

movies_count = int(input('Сколько фильмов хотите добавить? '))

for i in range(movies_count):
    movie = input('Введите название фильма: ')

if movie in films:
    my_list.append(movie)
else:
    print(f'Фильм {movie} не найден.')

print('Ваш список любимых фильмов: ', my_list)

#Задача 3
original_list = [1, 4, -3, 0, 10]
print ('Изначальный список: ', original_list)

for i in range(len(original_list) - 1):
    for j in range(len(original_list) - 1 - i):
        if original_list[j] > original_list[j + 1]:
            original_list[j], original_list[j + 1] = original_list[j + 1], original_list[j]

print ('Отсортированный список: ', original_list)

#Задача 4

goods = {
'Лампа': '12345',
'Стол': '23456',
'Диван': '34567',
'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for item_name in goods.keys():
    item_code = goods[item_name]
    total_quantity = 0
    total_cost = 0

    for entry in store[item_code]:
        total_quantity += entry['quantity']
        total_cost += entry['price'] * entry['quantity']

    print(f'Наименование: {item_name}, Код: {item_code}, Общее количество: {total_quantity}, Общая стоимость: {total_cost}')

#Задача 5

orders_count = int(input('Введите количество заказов: '))
database = dict()

for i_order in range(orders_count):
    customer, pizza_name, count = input('{} заказ: '.format(i_order + 1)).split()
    count = int(count)
    if customer not in database:
        database[customer] = {pizza_name: count}
    else:
        if pizza_name in database[customer]:
            database[customer][pizza_name] += count
        else:
            database[customer][pizza_name] = count

for customer in sorted(database.keys()):
    print('{} заказы:'.format(customer))
    for pizza_name, count in database[customer].items():
        print('{} - {}'.format(pizza_name, count))