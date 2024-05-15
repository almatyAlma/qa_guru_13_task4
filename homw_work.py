from datetime import time
def test_dark_theme_by_time():
    current_time = time(hour=23)
    if time(6)<= current_time <= time(22):
        is_dark_theme = False
        print('Светлая тема')
    else:
        is_dark_theme = True
        print('Светлая тема')
        assert is_dark_theme is True

def test_dark_theme_by_time_and_user_choice():
    current_time = time(hour=16)
    dark_theme_enabled_by_user = True
    is_dark_theme = None
    if dark_theme_enabled_by_user is True:
        is_dark_theme = True
        print('Принудительно включена темная тема.')
    elif dark_theme_enabled_by_user is False:
        is_dark_theme = False
        print('Принудительно включена светлая тема.')
    elif dark_theme_enabled_by_user is None:
        if time(6) <= current_time <= time(22):
            is_dark_theme = False
            print('Включена светлая тема по времени.')
        else:
            is_dark_theme = True
            print('Включена темная тема по времени.')
    else:
        print('Невозможоно определить время.')

    assert is_dark_theme is True

def test_find_suitable_user():

    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    suitable_users = []
    for user in users:
        if user['name'] == "Olga":
            suitable_users = user
            print(suitable_users)

    assert suitable_users == {"name": "Olga", "age": 45}

    suitable_users = []
    for user in users:
        if user['age'] < 20:
            suitable_users.append(user)
            print("Пользовтель младше 20 лет: ", suitable_users)













