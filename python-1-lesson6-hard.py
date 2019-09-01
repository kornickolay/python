# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка
import random, time


class Toy():
    def __init__(self, new_name):
        self.name = new_name
        palette = ('Красный', 'Оранжевый', 'Жёлтый', 'Зелёный', 'Голубой', 'Синий', 'Фиолетовый')
        self.color = palette[random.randint(0, 6)]


class AnimalToy(Toy):
    def __init__(self, new_name):
        super().__init__(new_name)
        self.toy_type = 'Животное'


class CartoonToy(Toy):
    def __init__(self, new_name):
        super().__init__(new_name)
        self.toy_type = 'Персонаж мультфильма'


class Factory():
    def buying(self):
        print('Идёт закупка сырья')
        for _ in (1, 2):
            print('%%%%%', end='')
            time.sleep(1)
        print()

    def tailoring(self):
        # 1. определяемся с названием игрушки и её типом
        # цвет будет выбираться рандомно в __init__
        new_name = input('Название игрушки: ')
        # 2. выбираем тип игрушки. Вводит также пользователь
        level = 0
        while not (level in [1, 2]):
            try:
                level = int(input('Выберите тип игрушки (1- Животное; 2 - Персонаж мультфильма)'))
                if level == 1:
                    new_toy = AnimalToy(new_name)
                    break
                elif level == 2:
                    new_toy = CartoonToy(new_name)
                    break
                else:
                    print('Нет такого варианта!')
            except ValueError:
                print('Неверный формат данных!')
        # 3. возвращаем прототип изделия
        return new_toy

    def processing(self):
        # 1. закупка сырья
        self.buying()
        # 2. пошив
        toy = self.tailoring()
        # 3. окраска
        print('Идёт покраска игрушки в {} цвет!'.format(toy.color))
        for _ in (1, 2):
            print('%%%%%', end='')
            time.sleep(1)
        print()

        # 4. после покраски изделие высыхает и готово к отгрузке на склад
        return toy


def main():
    print('Процесс производства запущен...')
    factory = Factory()
    ready_toy = factory.processing()
    print('-----------------------------------------\nНа выходе мы получили игрушку:\nТип:', ready_toy.toy_type,
          '\nНазвание:', ready_toy.name, '\nЦвет игрушки:', ready_toy.color)


if __name__ == '__main__':
    main()
