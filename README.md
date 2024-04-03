# Backend Capstone

## Prerequisites
- MySQL database
- Database user with admin privileges
- Python 3.12
- Poetry 1.8.2

## Setup instructions

Local env

`poetry env use python`

`poetry install`

Create .env file

`cp example.env .env`

Update db credentials and provide a `django_secret_key`

To generate a key

`poetry run python manage.py generate_secret_key`

DB migrate

`poetry run python manage.py migrate`

## Running test server

`poetry run python manage.py runserver`

## Running tests

`poetry run python manage.py test`

## Urls

### Homepage
http://localhost:8000/

### Auth

List user [GET] http://localhost:8000/auth/users/

Create user [POST] http://localhost:8000/auth/users/

With JSON body
```
{
    "email": "test@test.com",
    "username": "test",
    "password": "abcdef123!!"
}
```

Login [POST] http://127.0.0.1:8000/auth/token/login

With JSON body
```
{
    "username": "test",
    "password": "abcdef123!!"
}
```

### Menu

List [GET] http://localhost:8000/api/menu/

Get single [GET] http://localhost:8000/api/menu/(PK)/

Create [POST] http://localhost:8000/api/menu/

WIth JSON body
```
{
    "title": "Spam",
    "price": 3.50,
    "inventory": 5000
}
```

### Booking

List [GET] http://localhost:8000/api/booking/tables/

Get single [GET] http://localhost:8000/api/booking/tables/(PK)/

Create [POST] http://localhost:8000/api/booking/tables/

WIth JSON body
```
{
	"name": "Mr F",
	"no_of_guests": 5,
	"booking_date": "2024-04-03T12:00:00.0Z"
}
```
