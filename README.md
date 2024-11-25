
### Описание элементов README.md

- **Название и описание проекта**: Введение в проект и его основные функции.
- **Логика работы**: Объяснение того, как работает API и какие операции доступны.
- **Установка**: Подробные шаги по клонированию репозитория, созданию виртуального окружения, установке зависимостей и запуску сервера.
- **Примеры запросов к API**: Примеры запросов с использованием `curl`, включая ожидаемые ответы для каждого запроса.
- **Заключение**: Общее резюме о проекте и его возможностях.



# API Online-магазина

Это проект API для онлайн-магазина, разработанный с использованием Django и Django Rest Framework. API позволяет пользователям получать список товаров, добавлять новые товары и управлять аутентификацией через токены.

## Логика работы

API состоит из трех основных представлений:

1. **Получение токена**: Позволяет пользователям получать уникальный токен для аутентификации.
2. **Получение списка товаров**: Позволяет пользователям просматривать все доступные товары.
3. **Добавление нового товара**: Позволяет пользователям добавлять новые товары в базу данных.

Каждое представление проверяет наличие и действительность токена перед выполнением операций.

## Установка

Чтобы установить проект на своем компьютере, выполните следующие шаги:

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/meganis0-0/RestShopApi.git

2. Создайте виртуальное окружение:

   ```bash
   python -m venv venv

3. Активируйте виртуальное окружение:
-Для Windows:
   ```bash
   venv\Scripts\activate

4. Установите необходимые зависимости:
   ```bash
   pip install django djangorestframework

5. Выполните миграции:
   ```bash
   python manage.py makemigrations shop
   python manage.py migrate

6. Запустите сервер разработки:
   ```bash
   python manage.py runserver

Теперь ваше API будет доступно по адресу http://127.0.0.1:8000/shop/.


## Примеры запросов к API

1. Получение токена <br />

   Запрос:
      ```bash
      curl -X GET http://127.0.0.1:8000/shop/get_token/
      ```
   Ответ:
      ```json
      {
       "token": "123e4567-e89b-12d3-a456-426614174000"
      }
      ```

2. Получение списка товаров <br />
   Запрос (замените <ваш_токен> на полученный токен):
      ```bash
      curl -X GET "http://127.0.0.1:8000/shop/goods/?token=<ваш_токен>"
      ```
   Ответ (если товаров нет):
      ```json
      []
      ```

   Ответ (если товары есть):
      ```json
      [
       {
           "id": 1,
           "name": "Товар 1",
           "amount": 10,
           "price": 100
       },
       {
           "id": 2,
           "name": "Товар 2",
           "amount": 5,
           "price": 200
       }
      ]
      ```
3. Добавление новых товаров <br />
   Запрос (замените <ваш_токен> на полученный токен):
      ```bash
      curl -X POST "http://127.0.0.1:8000/shop/new_good/?token=<ваш_токен>" \
      -H "Content-Type: application/json" \
      -d '{"name": "Новый товар", "amount": 15, "price": 150}'
      ```
   Ответ (успех):   
      ```json
      {
       "id": 3,
       "name": "Новый товар",
       "amount": 15,
       "price": 150
      }
      ```

   Ответ (ошибка при добавлении) (например, если цена меньше или равна нулю):
      ```json
      {
       "price": [
           "Price must be more than 0"
       ]
      }
      ```

Или же можно перейти по адресу http://127.0.0.1:8000/shop/new_good/?token=<your_token>
и добавить товар вручную, введя данные в json формате и нажав POST
![image](https://github.com/user-attachments/assets/e6cf5a4e-ac0d-4327-b6e1-69012dad847c)

## Заключение
Этот проект предоставляет базовую функциональность для управления товарами в онлайн-магазине через RESTful API с использованием Django Rest Framework и аутентификацией через токены. Вы можете расширять его функциональность по своему усмотрению.
