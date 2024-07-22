# api_final

## Описание: 

Учебный проект. Создаётся бэкенд на питоне для сайта. на сайте реализована функция - отправки постов. комментирования постов. подписаться на юзера. К сайту можно обратиться по API. В этой части проекта научился взаимодействию с API.

README in English (https://github.com/GrigoriyNe/api_final_yatube/blob/master/README_en.md)

## Установка

Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```git clone https://github.com/GrigoriyNe/api_final_yatube```

```cd api_final_yatube```

Cоздать и активировать виртуальное окружение:

```python3 -m venv env```

```source env/bin/activate```

Установить зависимости из файла requirements.txt:

```python3 -m pip install --upgrade pip```

```pip install -r requirements.txt```

Выполнить миграции:

```python3 manage.py migrate```

Запустить проект:

```python3 manage.py runserver```


## Примеры. Некоторые примеры запросов к API.

### GET http://127.0.0.1:8000/api/v1/posts/

Response samples

Status == 200:

```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

### POST http://127.0.0.1:8000/api/v1/posts/

Response samples

Status == 200

```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```

Response samples


Status == 201

```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```

Status == 400

```
{
  "text": [
    "Обязательное поле."
  ]
}
```

Status == 401

```
{
  "detail": "Учетные данные не были предоставлены."
}
```

### PUT http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/

Request samples

{
  "text": "string"
}

Response samples

Status == 200

```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```

Status == 400

```
{
  "text": [
    "Обязательное поле."
  ]
}
```

Status == 403

```
{
  "detail": "У вас недостаточно прав для выполнения данного действия."
}
```

Status == 404

```
{
  "detail": "Страница не найдена."
}
```

