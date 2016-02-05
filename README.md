# PytSite
Сайт-приложение на Python.

Цель
--------
Легкий, менее зависимый от внешних библиотек простой сайт. Предназначен для таких систем как RasberryPi.
Принцип работы: запустился, обработал запрос, вернул ответ, завершился процесс.
Должна быть возможность развернуть всю цепочку обработки запроса с минимальными затратами.
Наивысший контроль над ситуацией (вся цепочка - свой легкий сервер, сайт).


Цепочка выполнений
--------
zex (nginx) -> zesap -> pytsite


Настройка
--------
- zex (nginx): слушает UNIX-сокет от zesap
пример конфига ngix
>upstream backend {
>    server unix:/var/tmp/zesap.sock;
>}
>
>server {
>   listen 3542;
>   server_name localhost;
>   location ~* \.(js|jpg|png|css|ico)$ {
>        root /home/zelder/Projects/Zexes/pytsite/App/;
>    }
>   location / {
>      proxy_pass http://backend;
>   }
>}

- zesap: подменяет свой же процесс, запуском кода. Указывается скрипт питона 'main.py' (/home/zelder/Projects/Zexes/pytsite/App/main.py)


Принцип сайта
--------
- Движок сайта подобен MVC. Есть Контроллеры, Вьюшки, Модели.
- Контроллеры создаются каждый свой в папке Controllers
- Контроллеры прописываются в файле 'Controllers/__init.py__'
- Добавляются маршруты в файл 'Configs/routes'
- Вьюшки кладутся в 'Views/{controllername}/{actionname}.zr.html' (название Контроллера без слова 'Controller' на конце)
- Во вьюшках можно использовать значение из моделей 'SomeValue = @{value1}'


