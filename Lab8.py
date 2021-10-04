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

            start = input("Фамилия ")
            finish = input("Имя ")
            number = input("Знак зодиака ")
            number1 = input("Дата рождения ")

            worker = {
                'start': start,
                'finish': finish,
                'number': number,
                'number1': number1,
            }

            workers.append(worker)

            if len(workers) > 1:
                workers.sort(key=lambda item: item.get('number', ''))
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
                    '| {:>4} | {:<30} | {:<20} | {:>30} | {:>30}'.format(
                        idx,
                        worker.get('start', ''),
                        worker.get('finish', ''),
                        worker.get('number', ''),
                        worker.get('number1', '')
                    )
                )
            print(line)

        elif command=='select':

            zd=input("vvedite")

            for worker in workers:
                if worker.get('number') == zd:

                    print(
                        '{:>4}, {}, {}'.format(worker.get('start', ''),
                                               worker.get('finish', ''),
                                               worker.get('number1', ''))
                    )
                else:
                    print("Знак зодиака не найден")

        elif command == 'help':

            print("Список команд:\n")
            print("add - добавить работника;")
            print("list - вывести список работников;")
            print("select <номер маршрута> - запросить работников со стажем;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
