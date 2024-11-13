# Задание 1
# Задача 1

array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

all_elems = array_1 + array_2 + array_3

new_elems_1 = []

for elem in all_elems:
    if elem not in new_elems_1 and (elem in array for array in [array_1, array_2, array_3]):
        new_elems_1.append(elem)

print("Решение без множеств:", new_elems_1)

new_elems_1_set = set(array_1) & set(array_2) & set(array_3)

print("Решение с множествами:", new_elems_1_set)

# Задача 2

new_elems_2 = []

for elem in array_1:
    if elem not in array_2 and elem not in array_3:
        new_elems_2.append(elem)

print("Решение без множеств:", new_elems_2)

new_elems_2_set = set(array_2) - set(array_1) - set(array_3)

print("Решение с множествами:", new_elems_2_set)

# Задание 2

def is_poly(string):
    char_dict = dict()
    for i_sym in string:
        char_dict[i_sym] = char_dict.get(i_sym, 0) + 1
    
    odd_count = 0
    for i_value in char_dict.values():
        if i_value % 2 != 0:
            odd_count += 1
    
    return odd_count <= 1

my_string = input('Введите строку: ')

if is_poly(my_string):
    print('Строка является полиндромом')
else:
    print('Строка не является полиндромом')

# Задание 3

synonyms_dict = dict()

pars_count = int(input('Введите количество пар слов: '))

for i_pair in range(pars_count):
    first_word, second_word = input(f'{i_pair + 1} пара: ').lower().split(' - ')
    synonyms_dict[first_word] = second_word
    synonyms_dict[second_word] = first_word

while True:
    user_word = input('Введите слово для проверки синонимов: ').lower()
    if user_word in synonyms_dict:
        print(f'Синонимы для слова "{user_word}": {synonyms_dict[user_word]}')
        break
    else:
        print('Слово не найдено в словаре')

# Задание 4

def histogram(string):
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
    
    return sym_dict

def invert_dict(d):
    inv = dict()
    for key in d:
        val = d[key]
        if val not in inv:
            inv[val] = [key]
        else:
            inv[val].append(key)
    
    return inv

my_string = input('Введите строку: ')

hist = histogram(my_string)

print('Оригинальный словарь частот:')
for i_sym in sorted(hist.keys()):
    print(i_sym, ':', hist[i_sym])

inv_hist = invert_dict(hist)

print('\nИнвертированный словарь частот:')

for i_sym in sorted(inv_hist.keys()):
    print(i_sym, ':', inv_hist[i_sym])
