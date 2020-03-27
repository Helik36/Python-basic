# Задание 1  ________________________________________________________________
from sys import argv
from random import randrange, randint
from functools import reduce
from itertools import count, cycle

name, house, money_in_h, prize = argv

print(
    f"Cотрудник отработал {house} часов, его ЗП в час составляет {money_in_h}, а премия {prize}. ЗП сотрудника состовляет "
    f"{(int(house) * int(money_in_h)) + int(prize)} рублей")

# Задание 2  ________________________________________________________________

my_list = [randrange(0, 201) for i in range(15)]
my_new_list = []
print("задание 2, исходный список:", my_list)
for i in range(1, len(my_list)): # указал, чтобы шёл с единницы, чтобы начинался с первого, т.к иначе если сделать i - 1, элемент [0] будет сравнивать самое первое значение, с самым последним.
    if my_list[i] > my_list[i-1]:
        my_new_list.append(my_list[i])
print("Список, в котором следующей значение больше предыдущего", my_new_list)

# Задание 3  ________________________________________________________________

my_list_rand = [i for i in range(20, 201) if i % 20 == 0 or i % 21 == 0]
print("Задание 3 ", my_list_rand)


# Задание 4 ________________________________________________________________

list_numb = [randrange(0, 16) for i in range(30)]
print("Задание 4, исходный список", list_numb)
result = [i for i in list_numb if list_numb.count(i) == 1]
print("Уникальный список", result)

# Задание 5  ________________________________________________________________
def func_reduce(var_1, var_2):
    return var_1 + var_2

my2_list = reduce(func_reduce,[i for i in range(100, 1001) if i % 2 == 0])
print(my2_list)

# задание 6  ________________________________________________________________
# a
print("Задание 6")
e = 1
for i in count(5):
    if e > 10:
        break
    else:
        print(randrange(0, i))
        e += 1
"""
Если нужно, что цикл был бесконечный

for i in count(5):
    print(randrange(0, i))
"""

# b ____________

cycle_list = [randrange(0, 11) for i in range(11)]
print(cycle_list)
q = 0
for i in cycle(cycle_list):
    if q > 12:
        break
    else:
        print(i)
        q += 1

"""
Если нужно, чтобы цикл был  бесконечный

cycle_list = [randrange(0, 11) for i in range(11)]
for i in cycle(cycle_list):
    print(i)
"""
# Задание 7  ________________________________________________________________
print("Задание 7")
def fibo_gen():
    factor = 1
    for i in range(1, 16):
        factor *= i
        yield factor

for el in fibo_gen():
    print(el)