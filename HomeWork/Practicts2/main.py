#Задача 1

rating = int(input('Enter number: '))
positive_count = 0
negative_count = 0

while rating != 0:
    if rating > 0:
        positive_count += 1
    elif rating < 0:
        negative_count += 1
    rating = int(input('Enter number: '))

print('Positive count: ', positive_count)
print('Negative count: ', negative_count)


# Задача 2

hour = 0
tasks_sum = 0
go_to_store = False

print('Начался 8-часовой рабочий день')

while hour != 8:
    hour += 1
    print(f'Час {hour}:')

    solved_tasks = int(input('Сколько задач решит Максим? '))
    tasks_sum += solved_tasks
    call = int(input('Звонит жена. Взять трубку? (1 - да, 0 - нет): '))
    if call == 1:
        go_to_store = True

print('Рабочий день закончился. Всего выполнено задач: ', tasks_sum)
if go_to_store:
    print('Нужно зайти в магазин')


# Задача 3

number = 7
guess_count = 0

while True:
    guess_num = int(input('Введите число: '))
    guess_count += 1
    if guess_num > number:
        print('Загаданное число меньше. Попробуйте еще раз!')
    elif guess_num < number:
        print('Загаданное число больше. Попробуйте еще раз!')
    else:
        print(f'Вы угадали число! Это было число {number}. Вы потратили {guess_count} попыток.')
        break


# Задача 4

salary_year = 0

for month in range(1, 13):
    salary_month = int(input('Зарплата сотрудника за месяц {}: '.format(month)))
    salary_year += salary_month

average_salary = salary_year / 12

print('Средняя зарплата за год: ', average_salary)


# Задача 5

total_cards = int(input('Введите кол-во карточек: '))
total_sum = 0

for card in range(1, total_cards + 1):
    total_sum += card

for card in range(total_cards - 1):
    remaining_card = int(input('Номер оставшейся карты: '))
    total_sum -= remaining_card

print('Номер потерявшейся карты: ', total_sum)


# Задача 6

boys = int(input('Введите кол-во мальчиков: '))
girls = int(input('Введите кол-во девочек: '))
answer = ''

if (boys > 2 * girls) or (girls > 2 * boys):
    print('Нет решения')

elif boys >= girls:
    k = boys - girls
    for bgb in range(k):
        answer += 'BGB'
    for bg in range(girls - k):
        answer += 'BG'
else:
    k = girls - boys
    for gbg in range(k):
        answer += 'GBG'
    for gb in range(boys - k):
        answer += 'GB'

print('Вариант решения: ', answer)
