# api_final

## Description: 

A training project. A python backend is being created for the site. The site has a feature for sending posts. commenting on posts. subscribe to the user. The site can be accessed via the API. In this part of the project, I learned how to interact with the API

## Installation

How to launch a project:

Clone the repository and go to it on the command line:

```git clone https://github.com/GrigoriyNe/api_final_yatube```

```cd api_final_yatube```

Create and activate a virtual environment:

```python3 -m venv env```

```source env/bin/activate```

Install dependencies from a file requirements.txt:

```python3 -m pip install --upgrade pip```

```pip install -r requirements.txt```

Perform migrations:

```python3 manage.py migrate```

Launch a project:

```python3 manage.py runserver```



## Examples. Some examples of API requests.

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

```
{
  "text": "string"
}
```

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

