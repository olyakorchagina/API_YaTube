# REST API для социальной сети YaTube


### Описание проекта

Проект выполнен в рамках учебного курса Яндекс.Практикум.

Реализован REST API CRUD для основных моделей проекта YaTube, для аутентификации примненяются JWT-токены.


### Запустить проект

1. Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/olyakorchagina/api_final_yatube.git

cd yatube_api
```

2. Cоздать и активировать виртуальное окружение:

```
python3 -m venv env

source env/bin/activate
```

3. Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip

pip install -r requirements.txt
```

4. Выполнить миграции:

```
python3 manage.py migrate
```

5. Запустить проект:

```
python3 manage.py runserver
```


### Документация к проекту

Документация для API после установки доступна по адресу /redoc/.
