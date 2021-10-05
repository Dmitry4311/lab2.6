#!/usr/bin/env python3
# -*- coding^ utf-8 -*-


import sys

if __name__ == '__main__':
    workers = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':

            surname = input("Фамилия ")
            name = input("Имя ")
            zodiac_sign = input("Знак зодиака ")
            date_of_birth = input("Дата рождения ")

            worker = {
                'surname': surname,
                'name': name,
                'zodiac_sign': zodiac_sign,
                'date_of_birth': date_of_birth,
            }

            workers.append(worker)

            if len(workers) > 1:
                workers.sort(key=lambda item: item.get('zodiac_sign', ''))
        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 30,
                '-' * 30
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^30} | {:^30} |'.format(
                    "№",
                    "Имя",
                    "Фамилия",
                    "Знак зодиака",
                    "Дата рождения"
                )
            )
            print(line)

            for idx, worker in enumerate(workers, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:<30} | {:>30}'.format(
                        idx,
                        worker.get('surname', ''),
                        worker.get('name', ''),
                        worker.get('zodiac_sign', ''),
                        worker.get('date_of_birth', '')
                    )
                )
            print(line)

        elif command=='select':

            zd=input("vvedite")

            for worker in workers:

                if worker.get('zodiac_sign') == zd:

                    print(
                        '{:>4}, {}, {}'.format(worker.get('surname', ''),
                                               worker.get('name', ''),
                                               list(map(int,worker.get('date_of_birth', '').split('.'))))
                    )
                else:
                    print("Знак зодиака не найден")

        elif command == 'help':

            print("Список команд:\n")
            print("add - добавить работника;")
            print("list - вывести список работников;")
            print("select - выбрать человека по знаку зодиака;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
