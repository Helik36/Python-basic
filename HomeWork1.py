# Задание 1

name = 'Герман'

age = 21
i_human = True
height = 177.5

print(f'Меня зовут - {name}, мне {age}')

n_friend = input("как Зовут твоего друга: ")
a_frined = int(input('Сколько ему лет? '))

print(f'У меня есть друг - {n_friend}, ему {a_frined}')

# Задание 2

time = int(input("Введи время в секундах или просто числа: "))

time_s = time % 60

time_m = (time // 60) % 60

time_h = time // (60*60)

print('Получилось - %.2d:%.2d:%.2d' % (time_h, time_m, time_s))

# задание 3

n = input("Введи число: ")

nn = n + n
nn_int = int(nn)

nnn = n + n + n
nnn_int = int(nnn)

n_int = int(n)

n_sun = n_int + nn_int + nnn_int

print(f'{n_int} + {nn_int} + {nnn_int} = {n_sun}')

# Задание 4

number = int(input("Введи положительные числа: " )) 
n = 0

while number % 10:

	if number % 10 >= n:
		n = number % 10
		number = number // 10

	elif number % 10 <= n:
		number = number // 10

	elif n >= number % 10:
		number = number // 10

print(f"Самое большое число, это {n}")

# Задание 5

cash = int(input("Укажи выручку компании: "))
not_cash = int(input("Укажи издержки компании: "))

if cash > not_cash:
	print("Прибыль — выручка больше издержек! =)")
	rentabl = cash / not_cash
	print(f'рентабильность - {rentabl:.2f}')
	workmens = int(input('Сколько людей работает в компании: '))
	ras = cash / workmens
	print(f'Расчёт прибыли на одного сотрудника: {ras:.2f}')

elif cash == not_cash:
	print("выручки ноль -_-")

else:
	print("убыток — издержки больше выручки :c")

# Задание 6

start = int(input("Сколько километров пробежал первый день: "))
end = int(input("Сколько он должен пробежать: "))
day = 1

while True:

	print(f'{day}-й день: {start:.2f}')
	day += 1
	start += start / 10

	if int(start) == end:
		print(f'{day}-й день: {start:.2f}')
		print(f'на {day}-й день, спортсмен пробежит - {int(start)} километров.')
		break