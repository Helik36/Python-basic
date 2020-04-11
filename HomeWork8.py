class Data:

    @classmethod
    def my_cl(cls, param):
        result = []
        for i in param:
            result.append(int(i))
        for i in range(len(result)):
            print(type(result[i]))
        # print(result)

    @staticmethod
    def my_met(dta):
        print(dta[0])
        if int(dta[0]) < 1 or int(dta[0]) > 31:
            print('неверно указан дата')
        print(dta[1])
        if int(dta[1]) < 1 or int(dta[1]) > 12:
            print('неверно указан месяц')
        print(dta[2])
        if int(dta[2]) < 2000 or int(dta[2]) > 2222:
            print('неверно указан год')

m_data = input("Введи числа через пробел в формате дд:мм:гг: ").split()
# m_data = ['6', '4', '2000']
print('-'.join(m_data))
Data.my_cl(m_data)
mc = Data()
mc.my_met(m_data)

# Задание 2 ____________________________________________________________________________________________________________

class Error(Exception):
    def __init__(self, numb):
        self.numb = numb

n = input("Укажи число: ")
w = input("Укажи число: ")

try:
    n = int(n)
    w = int(w)
    if n == 0:
        raise Error("Деление на ноль невозожно")
    if w == 0:
        raise Error("Деление на ноль невозожно")
except ValueError:
    print("Вы ввели не число")
except Error as err:
    print(err)
else:
    print(f"Ответ: {n // w }")

# Задание 3_____________________________________________________________________________________________________________

class My_Err(Exception):
    def __init__(self, par):
        self.par = par

m = []
print("Для выхода, напишите - 'stop'")
numb = None

while numb != 'stop':

    numb = input("Добавляй числа: ").split()
    for i in range(len(numb)):
        if numb[i] == 'stop':
            numb = 'stop'
            break
        else:
            try:
                if numb[i].isdigit() == False:
                    raise My_Err("Нельзя добавить буквы или слова.")
            except My_Err as err:
                print(err)
            else:
                m.append(int(numb[i]))

    print("Получилось: ", m)

print('Работа завершена')

# задание 4-6 ____________________________________________________________________________________________________________
q = None

class My_Err(Exception):
    def __init__(self, par):
        self.par = par

class Stock_T:
    @staticmethod
    def cler(param = []):
        return f'весь склад - {param}'

class Techics:
    def __init__(self, type, name, quant):
        self.type = type
        self.name = name
        self.quant = quant
        self.model = {"Тип": [], "Модель": [], "Количество:": []}
        self.stocs = {"Бухгалтерия": [], "Офис": [], "Себе": []}

    def __str__(self):
        return f"{self.type} - {self.name}, количество - {self.quant}"

    def enter(self):
            try:
                type1 = input("Принтер, Сканер или Ксерокс: ").title()
                if type1 != "Принтер" and type1 != "Сканер" and type1 != "Ксерокс":
                    raise My_Err("Укажите тип из приведённого списка")

                name1 = input("Модель: ").title()
                quant1 = int(input("Количество: "))
                new_list = {"Тип": type1, "Модель": name1, "Количество:": quant1}
                for i in new_list.keys():
                    self.model[i].append(new_list[i])

                print("*" * 30)
                print("Текущий список:")
                for key, value in self.model.items():
                    print(f'{key[:15]:>20}: {value}')
                print("*" * 30)

            except My_Err as err:
                    print(err)
                    return Techics.enter(self)
            except ValueError:
                print("Ошибка, в строке 'количесто' нужно вводить числа")
                return Techics.enter(self)

            print(f'Для выхода - Q, продолжение - Enter')
            q = input().title()
            if q == 'Q':
                print(Stock_T.cler(self.model))
                return "Выход"
            else:
                return Techics.enter(self)

    def broadcust(self):
        for i in self.model["Тип"]:
            # print(i)
            if i == "Принтер":
                self.stocs["Бухгалтерия"].append(i)
                print(f'{i}ы уходят в бухгалтерию')
            elif i == "Сканнер":
                self.stocs["Офис"].append(i)
                print(f'{i}ы уходят в Офис')
            elif i == "Ксерокс":
                self.stocs["Себе"].append(i)
                print(f'{i}ы забераю себе')

class Print(Techics):

    def print_met(self):
        return f'Принтер {self.name} - Количество: {self.quant}'

class Scan(Techics):
    def scan_met(self):
        return f'Сканнер {self.name} - Количество: {self.quant}'

class Kserc(Techics):
    def kserc_met(self):
        return f'Ксер {self.name} - Количество: {self.quant}'

my = Techics("Принтер", "HP", 10)
printer = Print("Принтер", "HP", 10)
print(printer.print_met())
my.enter()
my.broadcust()

# Задание 7 ____________________________________________________________________________________________________________

class Complex_n:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'{(self.a + other.a) + (self.b + other.b)}*i'

    def __mul__(self, other):
        return f'{((self.a * other.a) + (self.b * other.b) + (self.b * other.a) + (self.a * other.b))}*i'

# a = 4
# b = 6
# aa = 8
# bb = 10

a = Complex_n(4, 6)
b = Complex_n(8, 10)
print(a + b)
print(a * b)