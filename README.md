# PytSite
Сайт-приложение на Python.

Цель
--------
- Выполняется приложением zesap (подменяет себя этим)


Цепочка выполнений:
zex (nginx) -> zesap -> pytsite


Настройка
--------
- zex (nginx): слушает UNIX-сокет от zesap
- zesap: подменяет свой же процесс, запуском кода. Указывается скрипт питона 'main.py' (/home/zelder/Projects/Zexes/pytsite/App/main.py)


Принцип сайта
--------
- Контроллеры создаются каждый свой в папке Controllers
- Контроллеры прописываются в файле 'Controllers/__init.py__'
- Добавляются маршруты в файл 'Configs/routes'


