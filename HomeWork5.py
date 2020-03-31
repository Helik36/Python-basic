from random import randrange
import json
# Задание 1

my_f = open("work1.txt", "w")
exit = True
while exit != False:
    content = [input(), "\n"]
    my_f.writelines(content)
    if content[0] == '':
        exit = False
my_f.close()

# второй способ

exit = True
with open("work1", "w") as f:
    while exit != False:
        content = [input(), "\n"]
        f.writelines(content)
        if content[0] == '':
            exit = False

# Задание 2 ____________________________________________________________________________________________________________
strok = 0

with open("work2.txt", "r", encoding="utf-8") as f:

    for i in f:
        strok += 1
        # print(i, end=" ")
        words = 0

        for _ in i.split():
            words += len(_.split())

        print(f"В строке {strok} - {words} слов")
print(f"Всего строк - {strok}")

# Задание 3 ____________________________________________________________________________________________________________

name = []
name_big_salary = []
salary_sum = 0.0
mean = 0.0
with open("work3.txt", "r", encoding="utf-8") as f:

    for i in f:
        name.append(i.split())
    print(name)

    for i in range(len(name)):
        if float(name[i][1]) < 20000.0:
            name_big_salary.append(name[i])

    for i in range(len(name_big_salary)):
        print(f"Имена, у кого оклад больше 20к - {name_big_salary[i][0]}")
        salary_sum += float(name_big_salary[i][1])
        mean = salary_sum // int(len(name_big_salary))

print(f"Общая сумма {salary_sum}")
print(f"Среднее значение: {mean}")


# задание 4 ____________________________________________________________________________________________________________
name = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четрые"
    }
result = []

with open("work4.txt", "r", encoding="utf-8") as f:

    for i in f:
        file = i.split(" - ")
        print(file)
        if file[0] in name:
            word = name[file[0]]
            result.append(word +' - '+ file[1])
print(result)

with open("work44.txt", "w", encoding="utf-8") as ff:
    ff.writelines(result)

# Задание 5 ____________________________________________________________________________________________________________
numb = []
numb_sum = 0

with open("work5.txt", "w") as f:
    for i in range(15):
        numb.append(randrange(1, 21))
    print(numb)
    for i in range(len(numb)):
        f.write(str(numb[i]) + " ")

with open("work5.txt", "r") as f:
    n_s = f.read().split()
    for i in n_s:
        numb_sum += int(i)
print(numb_sum)

# Задание 6 ____________________________________________________________________________________________________________

# пропустил

# Задание 7 ____________________________________________________________________________________________________________
n_list = [] # Добавляем ВСЕ компании
list_cash = [] # Добавляем только те, кто не ушёл в минус
cash = 0 # Общая
mean_cash = 0 # Средняя прибыль

my_list = [
    {},
    {}
]

with open("work7.txt", "r", encoding="utf-8") as f:
    for i in f:
        n_list.append(i.split())
        name, form, s, minus = i.split()
        my_list[0][name] = int(s) - int(minus) # Добавляю имя в список и создаю сразу же их выручку

    for i in range(len(n_list)):
        print(f"Прибыль компании {n_list[i][0]} равна - {int(n_list[i][2]) - int(n_list[i][3])}")
        if int(n_list[i][2]) - int(n_list[i][3]) > 0: # Добавляю в друой список компании у которых выручка больше 0
            list_cash.append(n_list[i])

    for i in range(len(list_cash)):
        cash += int(list_cash[i][2]) - int(list_cash[i][3]) # Считаю общую прибыль
    print(f"\nОбщий кэш: {cash}\n")

    for i in range(len(list_cash)):
        mean_cash = cash // len(list_cash) # Считаю среднюю прибыль
        my_list[1]["average_profit"] = mean_cash
    print(f"Средняя прибыль- {mean_cash}\n")

print(my_list)

with open("work7.json", "w", encoding="utf-8") as w_f:
    json.dump(my_list, w_f)
