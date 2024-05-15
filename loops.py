# While- цикл с предусловием
# пока пользователь не введет правильный номер, ...
import random

# while True:
    #print("What is your name?")


required_number = 7
user_number = random.randint(0, 10)

while required_number != user_number:
    user_number = random.randint(0, 10)
    print(f"hcfhjdj {user_number}")


    iterations_count = 10
    i = 0

    while i < iterations_count:
        print(f"What is your name? {i}")
        i += 1

# For
user = [
    {"name": "Oleg", "age": 32},
    {"name": "Bob", "age": 33},
    {"name": "Alice", "age": 34},
    {"name": "Dave", "age": 35},

]

from pprint import pprint

for user in user:
    pprint(f"Пользователю {user['name']} {user['age']} лет")


    d = {
        "first": 1,
        "second": 2,
        "third": 3,
    }

    for item in d:
        pprint(item)

    for item in d.keys():
        pprint(item)

    for item in d.keys():
        pprint(item)

    for item in d.items():
        pprint(item)

    #for key. value in d.items():
    #print("ключь: {key}, Значение: {value}")

        interations_count = 10

    for i in range(3, interations_count, 2):
        print(f"Текущая итерация: {i}")

    for i in range(iterations_count):
        if i % 0 == 0:
            continue
            print("Я никогда не выполнюсь")

            if i > 7:
                break
        print(f"Точно нечетное число: {i}")

        for i in range(5):
            for j in range(5):
                print(i, j)
                if j == 3:
                    continue

                if j == 4:
                    break

                if i% 2 == 0:
                    continue












