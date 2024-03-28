# _Market_
[![Static Badge](https://img.shields.io/badge/Python-blue?style=flat&logo=Python&labelColor=ffff99&color=0066ff)](https://www.python.org)
[![Static Badge](https://img.shields.io/badge/-Django-006400?style=&logo=django)](https://www.djangoproject.com)
[![Static Badge](https://img.shields.io/badge/Django%20Rest%20Framework-FF4500?logo=django)](https://www.django-rest-framework.org)
[![Static Badge](https://img.shields.io/badge/Swagger-3CB371?logo=swagger&logoColor=black)](https://swagger.io)
[![Static Badge](https://img.shields.io/badge/PostgreSQL-blue?style=flat&logo=postgresql&labelColor=white)](https://www.postgresql.org)
[![Static Badge](https://img.shields.io/badge/Redis-ff5050?style=flat&logo=Redis&labelColor=white)](https://redis.io)
[![Static Badge](https://img.shields.io/badge/Gunicorn-white?style=flat&logo=Gunicorn)](https://gunicorn.org)
[![Static Badge](https://img.shields.io/badge/Nginx-white?style=flat&logo=Nginx&labelColor=green)](https://nginx.org/en)
[![Static Badge](https://img.shields.io/badge/Docker-gray?style=flat&logo=Docker&labelColor=white)](https://www.docker.com)

<a name="Ссылка на магазин" href="https://tumch.xyz">📚 tumch.xyz</a>

<a name="project_desc"></a> 
### ✏️ Описание проекта ###
Проект на Django Rest Framework, с открытым доступом в интеренет, предназначенный показать взаимодействие
"**Книжного Магазина**" с _Пользователем_ и _Администратором_.

__Проект имеет следующие возможности__:
```
- Регистрация, авторизация, аутентификация,
- Смена пароля,
- Редактирование профиля,
- Просмотр профилей других пользователей,
- Получение каталога книг,
- Получение детальной информациии о книге,
- Поиск книги по ключевым словам(автор, ISBN, название и т.д.),
- Фильтрация каталога книг по цене и рейтингу,
- Добавление книг в избранное, получение избранных книг,
- Получение избранных книг всех пользователей(для администратора),
- Написание/удаление отзыва к книге, получение всех отзывов к книге,
- Создание корзины,
- Добавление элементов(книг) в корзину и их удаление,
- Создание заказа на основе корзины,
- Просмотр заказа, просмотр всех заказов(для администатора)
```
<a name="installation_ide"></a>
### 📔 Установка проекта в IDE ##
- Клонирование репозитория:
```text
git clone https://github.com/reznya22/market.git
```
- Создание виртуального окружения и установка зависимостей(Linux):
```text
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
- Создание `.env` на основе `example.env`
```.env
SECRET_KEY=
DEBUG=
ALLOWED_HOSTS=

PG_DATABASE=
PG_USER=
PG_PASSWORD=
DB_HOST=
DB_PORT=
```
<a name="installation_docker"></a>
### 🐳 Установка проекта в Docker ###
- (В разработке)

<a name="documentation_api"></a>
### 📗 Документация API ###
Документация к API доступна по `/api`.