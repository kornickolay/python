"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html
"""

import random, sys, time, os


# 3. Игра:
#     а. Генерируем случайное число
#     б. оба зачёркивают или не зачеркивают
#     в. у кого первого все числа зачёркнуты, тот выиграл, конец игры.

class Card():
    def __init__(self):
        self.cell = [[], [], []]
        for i in range(0, 3):
            for j in range(0, 9):
                self.cell[i].append('  ')

    # горизонтальная линия
    def print_line(self):
        print('+----+----+----+----+----+----+----+----+----+')

    # печатает один из трёх рядов с учетом форматирования
    def print_row(self, row):
        for i in self.cell[row]:
            print('| {:>2} '.format(i), end='')
        print('|')

    # выводит карту игрока
    # print('+----+----+----+----+----+----+----+----+----+')
    # print('| {} | {} | {} | {} | {} | {} | {} | {} | {} |')
    # print('+----+----+----+----+----+----+----+----+----+')
    # print('| {} | {} | {} | {} | {} | {} | {} | {} | {} |')
    # print('+----+----+----+----+----+----+----+----+----+')
    # print('| {} | {} | {} | {} | {} | {} | {} | {} | {} |')
    # print('+----+----+----+----+----+----+----+----+----+')
    def print_card(self):
        for i in range(0, 3):
            self.print_line()
            self.print_row(i)
        self.print_line()

    # проверка на уникальность числа. Прогоняем по всем ячейкам (на вход не подаются пустые). Если какая-то из ячеек
    # в отличном от входного ряду совпадает с входной, то возвращаем False.
    def check_num(self, i, j):
        check = True
        for _i in range(0, len(self.cell)):
            for _j in range(0, len(self.cell[_i])):
                if self.cell[_i][_j] == self.cell[i][j] and i != _i:
                    check = False
        return check

    # метод заполняет ряд числами и пробелами
    def fill_line(self, row):
        while True:
            check = True
            while check == True:
                # создаем новый список из 9ти случайных элементов
                new_line = []
                for i in range(0, 9):
                    new_line.append(random.randint(1, 90))
                # проверка на повторы с помощью оборачивания списка в множество. Если элементов по-прежнему 9,
                # то повторов нет, сортируем по возрастанию 9 элементов, выходим и цикла while, иначе повторяем
                new_line = list(set(new_line))
                if len(new_line) == 9:
                    new_line.sort()
                    check = False
            count = 9
            # для каждого из 9ти отсортированных элементов "подкидываем монетку", будет там пусто или будет число
            for i in range(len(new_line)):
                empty_or_full = random.randint(0, 1)
                if empty_or_full == 0:  # если пусто, то затираем ячейку, счетчик заполненных ячеек уменьшается на 1
                    new_line[i] = '  '
                    count -= 1
            # если заполненных ячеек получилось ровно 5, то ряду присваиваем наш новый обработанный список и заканчиваем выполнять метод
            if count == 5:
                self.cell[row] = new_line
                break

    # метод, заполняющий карту числами с учетом условий
    def fill_card(self):
        while True:
            for i in range(0, 3):
                self.fill_line(i)
            # проверка на дубликаты чисел
            check_all = True
            for i in range(0, len(self.cell)):
                for j in range(0, len(self.cell[i])):
                    # если ячейка пустая, то нет нужды ее проверять, идем дальше, иначе проверяем с помощью нашего метода check_num
                    if self.cell[i][j] != '  ':
                        if self.check_num(i, j) == False:
                            # если есть в ходе проверок хоть один False, то финальный флаг проверок становится равным False
                            check_all = False
            if check_all == True:
                break

    def check_another_number(self, num):
        check = False
        for i in range(0, len(self.cell)):
            for j in range(0, len(self.cell[i])):
                # если текущий разыграный номер совпадает с одним из значений, то это значение заменяется на "--"
                if self.cell[i][j] == num:
                    self.cell[i][j] = '--'
                    check = True
        # функция возвращает True, если число найдено, False - если такого в карточке нет
        return check

    def check_all_cells(self):
        check = True
        for i in range(0, len(self.cell)):
            for j in range(0, len(self.cell[i])):
                # если значение каждого элемента не указывает на число, значит карточка решена, возвращаем True
                if self.cell[i][j] == '  ' or self.cell[i][j] == '--':
                    pass
                else:
                    # если есть хоть одно значение отличное (число), возвращаем False - данный игрок не выиграл на этот момент.
                    check = False
        return check

# Создаём класс игрока - наследуем от базового, но добавляем ему новый атрибут, указывающий на ошибку при очередном ходе
class Player(Card):
    def __init__(self):
        super().__init__()
        self.mistake = True

class Game():
    def __init__(self):
        # 1. Создаем модели карточек
        self.player = Player()
        self.enemy = Card()
        # 2. Заполняем карточки игрока и соперника
        self.player.fill_card()
        self.enemy.fill_card()
        self.bag = []
        # заполняем мешочек с бочонками
        for i in range(0, 90):
            self.bag.append(i + 1)

    # берет из остатка в мешочке следующий бочонок
    def get_new_number(self):
        # заглушка на случай, если количество в мешочке будет равно нулю
        if len(self.bag) == 0:
            return 0
        # берём случайный индекс из списка оставшихся, возвращаем значение по индексу и удаляем это значение из мешочка
        new_number = random.randint(0, len(self.bag) - 1)
        num = self.bag[new_number]
        self.bag.remove(self.bag[new_number])
        return num

    def start(self):
        print('Игра началась')
        exit_game = 0  # флаг окончания игры и выхода из цикла
        while exit_game == 0:
            time.sleep(1)  # задержка по времени для удобства восприятия
            os.system('cls')  # если запускать программу из консоли, то будет после каждого хода очищать экран.
            # Вывод на экран игровых карт
            print('Ваша карта:')
            self.player.print_card()
            print('\nКарта соперника')
            self.enemy.print_card()
            # очередное число из оставшихся выдаёт нам метод объекта текущего класса
            another_number = self.get_new_number()
            print('Выпал бочонок:', another_number, ' осталось:', len(self.bag))
            # Безусловная проверка выпавшего числа в карте соперника
            self.enemy.check_another_number(another_number)
            # У игрока уже есть условия: сначала он выбирает, зачеркнуть выпавшее число или пропустить ход (продолжить)
            choice = 0
            while not (choice in ['1', '2']):
                choice = input('1. Зачеркнуть\n2. Продолжить')
            if choice == '1':
                # если зачеркнули, а такого номера нет, то игрок проиграл
                if self.player.check_another_number(another_number) == False:
                    self.player.mistake = False
            else:
                # если не зачеркнули, а такой номер есть, то игрок проиграл
                if self.player.check_another_number(another_number) == True:
                    self.player.mistake = False
            # если в результате своих действий игрок проиграл, то выдаём соответствующее сообщение и заканчиваем игру.
            if self.player.mistake == False:
                print('Игра окончена. Вы проиграли!!!')
                break
            # Если проверка показала, что после хода у игрока остались только пустые и зачёркнутые клетки, он выиграл.
            if self.player.check_all_cells():
                print('Вы выиграли!!! Игра окончена!')
                exit_game = 1
            # Если проверка показала, что после хода у соперника остались только пустые и зачёркнутые клетки, игрок проиграл.
            elif self.enemy.check_all_cells():
                print('Вы проиграли!!! Игра окончена!')
                exit_game = 1
            # В противном случае игра продолжается - следующий ход





# Запуск игры
game = Game()
game.start()