# FastAPI + RabbitMQ + Selenium Grid: Сервис для обработки URL

Этот проект представляет собой сервис на FastAPI, который принимает URL через POST-запросы и ставит их в очередь
RabbitMQ. Потребитель на Python с использованием Selenium извлекает URL из очереди и логирует HTML содержимое страницы.

## Функциональность

1. FastAPI сервис:

- Эндпоинт для добавления URL в очередь RabbitMQ.

2. RabbitMQ:

- Управляет очередью задач.

3. Selenium Grid:

- Кластер для удаленного управления браузерами.

4. Потребитель:

- Читает URL из очереди и получает HTML страницы с помощью Selenium.


##  Клонирование репозитория
```
git clone https://github.com/EgorZybin/fastapi_service.git
```

## Установка зависимостей
```
pip install -r requirements.txt
```

## Создание виртуального окружения
```
python -m venv venv
venv\Scripts\activate
```

## Запуск Сервиса сDocker Compose
Должен быть установлен Docker и Docker Compose для запуска сервиса
```
docker-compose up --build
```

## Документация Swagger

Документация по ссылке: http://127.0.0.1:8000/docs

## Тесты
Для запуска тестов используйте pytest.
```
pytest tests/test_main.py
```

## Автор сервиса: (https://github.com/EgorZybin) telegram: @raizzep
