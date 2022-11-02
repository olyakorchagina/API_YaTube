## REST API для социальной сети YaTube.

### Описание проекта:

Проект выполнен в рамках учебного курса **Яндекс.Практикум**.

Реализован REST API CRUD для основных моделей проекта **YaTube**, для аутентификации примненяются JWT-токены.


### Запустить проект:

**Клонировать репозиторий и перейти в него в командной строке:**

```
git clone https://github.com/olyakorchagina/api_final_yatube.git
```

```
cd yatube_api
```

**Cоздать и активировать виртуальное окружение:**

```
python3 -m venv env
```

```
source env/bin/activate
```

**Установить зависимости из файла requirements.txt:**

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

**Выполнить миграции:**

```
python3 manage.py migrate
```

**Запустить проект:**

```
python3 manage.py runserver
```

### Документация:

После запуска проекта по адресу [/redoc/](http://127.0.0.1:8000/redoc/) будет доступна документация для API **Yatube**. Документация представлена в формате **Redoc**.
