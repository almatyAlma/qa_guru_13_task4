
# Boolean - 3 состояния
b = bool

{
    "key": True
}

t = True
f = False
n = None

# if/elif/else

if True:
    print("я выполняюсь!")

if not False:
    print("я никогда не выполняюсь")

    code = 400

    if 200 <= code < 400:
        print("Проверка прошла, хороший ответ!")
    elif 400 <= code < 600:
        print("плохой ответ")
    else:
        print("какой-то странный код")

        #пустой объект
    user_list = []

    if user_list == []:
        pass

    if user_list:
        pass

    items_count = 0

    if items_count:
        pass

    if "abc" == "":
        pass

    if "abs":
        pass

    print(bool(100))
    print(bool(-100))
    print(bool(0))


    print(bool("abc"))
    print(bool(""))

    print(bool([]))
    print(bool([1, 2, 3]))
    print(bool([False]))


