from abc import abstractmethod

# Задани 1

class Matrix:
    def __init__(self, list):
        self.list1 = list
        self.list2= list

    def __str__(self):
        for i in self.list1:
            print(i)
        print()

    def __add__(self):
        result = [] # создаю новый список
        for i in range(len(self.list1)):
            result.append([0] * 3) # Делаю так, в списке появился список из 3 элементов

            for w in range(len(self.list2[i])):
                result[i][w] = self.list1[i][w] + self.list2[i][w]

        for i in result:
            print(i)

a = Matrix([[1,2,3], [4,5,6], [7,8,9]])
a.__str__()
a.__add__()


# Задание 2 ____________________________________________________________________________________________________________

class Clothes:

    def __init__(self, coat, costume):
        self.coat = coat
        self.costume = costume

    @abstractmethod
    def cloth_coat(self):
        return self.coat / 6.5 + 0.5

    @abstractmethod
    def cloth_cost(self):
        return 2 * self.costume + 0.3

    @property
    def method(self):
         return str(f'Общая сумма ткани - ' \
                    f'{(self.coat / 6.5 + 0.5) + (2 * self.costume + 0.3)}')

class Coat(Clothes):
    def __init__(self, coat, costume):
        super().__init__(coat, costume)

    def cloth_coat(self):
        return f'Расход ткани на пальто - {self.coat / 6.5 + 0.5}'

class Costume(Clothes):
    def __init__(self, coat, costume):
        super().__init__(coat, costume)

    def cloth_costume(self):
        return f'Расход ткани на костюм -  {2 * self.costume + 0.3}'

a = Clothes(2, 5)
b = Coat(2, 5)
print(b.cloth_coat())
c = Costume(2, 5)
print(c.cloth_costume())
print(a.method)

# Задание 3 ____________________________________________________________________________________________________________

class Cell:
    def __init__(self, count):
        self.count = int(count)

    def __add__(self, other):
        return self.count + other.count

    def __sub__(self, other):
        if self.count - other.count <= 0:
            print("Error")
        else:
            return self.count - other.count

    def __mul__(self, other):
        return self.count * other.count

    def __truediv__(self, other):
        return self.count // other.count

    def make_order(self, row):
        r = ''
        for i in range(int(self.count / row)):
            r = r + ("*" * row) + "\n" # сначала добавляем целый
        r = r + ("*" * (self.count % row)) # потом добавляем остаток
        return r

cell1 = Cell(34)
cell2 = Cell(16)
print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 / cell2)
print()
print(cell1.make_order(10)) # количество ячеек в ряду
print()
print(cell2.make_order(5))