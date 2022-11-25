## touch_Celery
Мини-Проект в к. осуществляется рассылка на почту Контактов по дате ДР<br>
Есть форма для записи Контакта (Имя, Фамилия, ДР, email).<br>



При регистрации приходит рассылка что вы включены в список рассылок. <br>



## Стек технологий

![python version](https://img.shields.io/badge/Python-2.7-yellowgreen) 
![python version](https://img.shields.io/badge/Django-1.11-yellowgreen) 
![python version](https://img.shields.io/badge/Celery-4.4-yellowgreen) 
![python version](https://img.shields.io/badge/Redis-dockers-yellowgreen) 

## Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:

```
https://github.com/alvaresShD/api_yamdb.git
```

Перейти в папку с проектом

```
cd api_yamdb
```

Cоздать и активировать виртуальное окружение:

```
WIN: python -m venv venv
MAC: python3 -m venv venv
```

```
WIN: source venv/scripts/activate
MAC: source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
WIN: python -m pip install --upgrade pip
MAC: python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
WIN: python manage.py migrate
MAC: python3 manage.py migrate
```

Запустить докер REDIS:

```
docker run -d -p 6379:6379 redis
```

Запустить проект в терминале:

```
WIN: python manage.py runserver
MAC: python3 manage.py runserver
```

Запустить в др.терминале celery worker (из директории с файлом manage.py):

```
celery -A birthday worker -P solo
```

Запустить в др.терминале celery beat (из директории с файлом manage.py):

```
celery -A birthday beat -l info
```

### Как пользоваться проектом
1. Запись в БД осуществляется на странице http://127.0.0.1:8000/create <br>
При регистрации приходит рассылка на почту нового Контакта что он включен в список рассылок.<br><br>
2. После валидной записи нового Контакта происходит редирект на http://127.0.0.1:8000/home <br>
На странице home отображены все Контакты к.записали для рассылки <br><br>
3. В дату ДР по списку Контактов отправляется сообщение с поздравлением на email.

### PS
Как п.4 ТЗ выполнить не совсем понял, поэтому не стал делать
Решений может быть несколько
- Встроить отбивку о прочтении в само письмо (возможными инструментами почтового ящика)
- Установить "flower" для мониторинга исполнения задач, но это больше о доставки а не о прочтении
- возможно еще какие-то варианты если подумать