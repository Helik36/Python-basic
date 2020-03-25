# Задание 1

my_list = [6, 'text', None, 66.6, True, (5, 6), -28.4]

for i in my_list:
    print(type(i))

# # Задание 2

my_list2 = []
q = 0
z = int(input("Cколько будет значений: "))

for i in range(z):
    my_list2.append(input("Добавляем значение: "))

copy_list = my_list2.copy()

for i in range(int(len(my_list2) / 2)):
    my_list2[q + 1] = my_list2[q]
    my_list2[q] = copy_list[q + 1]
    q += 2
print(my_list2)

# Задание 3

answer = int(input("Введи число от 1 до 12: "))

mouth_list = (
    "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь")

if answer == 1 or 2 or 3 or 4 or 6 or 7 or 8 or 9 or 10 or 11 or 12:
    print(mouth_list[answer - 1])

mouth_dict = {1: "Январь", 2: "Февраль", 3: "Март", 4: "Апрель", 5: "Май", 6: "Июнь", 7: "Июль", 8: "Август",
              9: "Сентябрь", 10: "Октябрь", 11: "Ноябрь", 12: "Декабрь"}

if answer == 1 or 2 or 3 or 4 or 6 or 7 or 8 or 9 or 10 or 11 or 12:
    print(mouth_dict.get(answer))

# Задание 4

text = input("Напиши разные слова: ")
text_list = []
numb = 1

for i in range(len(text)):
    text_list = text.split()

for i in range(len(text_list)):
    if len(text_list[i][:11]) < 11:
        print(f'{numb} {text_list[i]}')
        numb += 1

# Задание 5

my_list3 = [7, 5, 3, 2]
z = int(input('Сколько значений хотите добавить: '))

for i in range(z):
    ans = int(input("Какие значения добавить: "))

    if ans == my_list3[i]:
        my_list3.insert(i, ans)
        print(my_list3)

    elif ans > my_list3[i]:
        for _ in range(len(my_list3)):
            if ans == my_list3[_]:
                my_list3.insert(_, ans)
                print(my_list3)
                break

            elif ans > my_list3[_]:
                my_list3.insert(_, ans)
                print(my_list3)
                break

    elif my_list3[-1] > ans:
        my_list3.append(ans)
        print(my_list3)

    elif ans < my_list3[i] and ans > my_list3[-1]:
        for _ in range(len(my_list3)):
            if ans == my_list3[_]:
                my_list3.insert(_, ans)
                print(my_list3)
                break

            elif ans > my_list3[_]:
                my_list3.insert(_, ans)
                print(my_list3)
                break

# Задание 6

product = []
new_list = []
numb = int(input("Введите количество товара "))

for i in range(numb):
    product = dict(
        {'Название': input("Введите название "),
         'цена': input("Введите цену "),
         'количество': input('Введите количество '),
         'eд': input("Введите единицу измерения ")
         })
    new_list.append(tuple([i + 1, product]))
print(f'{new_list} \n')

analitics = {}
for i in new_list:
    for j, q in i[1].items():
        if j in analitics:
            analitics[j].append(q)
        else:
            analitics[j] = [q]
print(analitics)
