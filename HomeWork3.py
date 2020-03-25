# Задание 1

def func_first(a, b):
    try:
        result = a // b
    except ZeroDivisionError:
        print("На ноль делить нельзя :c ")
    else:
        return print(f'{a} / {b} = {result}')


a = int(input("Введи первое число: "))
b = int(input("Введи второе число: "))

func_first(a, b)

# задание 2

def data_func(name, t_name, age, city, email, phone):
    return name, t_name, age, city, email, phone


print(data_func(name=input("Имя: "),
                t_name=input("Фамилия: "),
                age=int(input("Год рождения: ")),
                city=input("Город проживания: "),
                email=input("емайл: "),
                phone=int(input("Телефон: "))))

# Задание 3

def my_func(var_1, var_2, var_3):
    result_sum = [var_1, var_2, var_3]
    if min(result_sum):
        result_sum.remove(min(result_sum))
    return sum(result_sum)


print(my_func(35, 60, 40))

# Задание 4

def my_func2(var_1, var_2):
    print(f"Решение 1: {var_1} ** {var_2} =", var_1 ** var_2)
    var_3 = var_1
    for i in range(abs(var_2) - 1):
        var_3 *= var_1
    var_3 = 1 / var_3
    print("Решение 2:", var_3)


a = int(input("Укажи целое положительно число: "))
b = int(input("Укажи целое отрицательно число: "))

my_func2(a, b)

# Задание 5

def func_sum(numb):

    while numb != 'Q':

        numb = input("Добавляй числа: ").split()
        for i in range(len(numb)):
            if numb[i] == 'q' or numb[i] == 'Q':
                numb = 'Q'
                break
            else:
                m.append(int(numb[i]))
                sum(m)

        print("Получилось: ", sum(m))

    print('Работа завершена')

m = []
numb = None
print("Для выхода, нажмите - 'Q'")

func_sum(numb)

# Задание 6

def int_func(word):
    for i in range(len(word)):
        word[i] = word[i].title()
    return word


text = input("Напиши какое-нибудь слово: ").split()

print(int_func(text))
