def my_fun():
    print("мы вызвали функцию!")


my_fun()

def sum_numbers(a:int, b:int):
    print(a + b)
    #raise AssertionError

sum_numbers(10, 15)
sum_numbers(20, 30)
sum_numbers(-78798989, 1)
sum_numbers("anv", "gvg")

def sum(a:int, b:int):
    return a + b


n = sum(10, 15)
print(n)


sum_numbers(a=10, b=15)
sum_numbers(b=10, a=15)



def multiply(n, mult: int =2):
    print(n * mult)

multiply(10)
multiply(10, 5)

print(1, 2, 3, 4, 5, sep=" | ")


def return_tuple():
    return 1, 2, 3

t = return_tuple()
print(t)
t1, t2, t3 = return_tuple()
print(t1, t2, t3)

t1, *t2 = return_tuple()
print(t1, t2)


