import os, shutil, sys


def create_dir(Name):
    for i in os.listdir():
        if Name == i and os.path.isdir(Name):
            print('Папка с таким именем уже существует!')
            return
    os.mkdir(Name)
    if os.path.isdir(Name):
        print('Папка была успешно создана!')
    else:
        print('Папка не создана!')


def remove_dir(Name):
    try:
        os.rmdir(Name)
        if os.path.isdir(Name):
            print('Папка не была удалена!')
        else:
            print('Папка была успешно удалена!')
    except FileNotFoundError:
        print('Указанной папки не существует!')
    except OSError:
        print('Папка не пуста!')


def main():
    # Задача-1:
    # Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
    # из которой запущен данный скрипт.
    # И второй скрипт, удаляющий эти папки.
    print('Задание №1\n----------------------')
    input('Нажмите клавишу Enter для создания директорий')
    for i in range(1, 10):
        create_dir('dir_{}'.format(i))

    input('Нажмите клавишу Enter для удаления директорий')
    for i in range(1, 10):
        remove_dir('dir_{}'.format(i))
    print('----------------------')

    # Задача-2:
    # Напишите скрипт, отображающий папки текущей директории.
    print('Задание №2\n----------------------')
    for i in os.listdir():
        if os.path.isdir(i):
            print(i)
    # Вариант в одну строчку при помощи генератора списков
    # print([i for i in os.listdir() if os.path.isdir(i)])
    print('----------------------')

    # Задача-3:
    # Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
    print('Задание №3\n----------------------')
    shutil.copy(os.path.basename(sys.argv[0]), os.path.basename(sys.argv[0]) + '.copy')
    # или вариант:
    # shutil.copy(sys.argv[0], sys.argv[0] + '.copy')
    print('Файл успешно скопирован!')
    print('----------------------')


if __name__ == '__main__':
    main()
