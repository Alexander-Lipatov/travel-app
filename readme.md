## Getting Started

Для запуска необходимо создать окружение python и активировать его.

### Installation

1. Создаем изолированное окружение: python -m venv env

2. Активируем созданное окружение 

```sh
 win: env\Scripts\activate
 linux: source env/bin/activate
```

3. Установка зависимостей:

```sh
  pip install -r req.txt
```

4. Создаем миграции и применяем их:
```sh
   python manage.py makemigrations posts users
   python manage.py migrate
```

## Usage

После того как установили окружение и зависимости можно запустить приложение:

```sh
   python manage.py runserver
```