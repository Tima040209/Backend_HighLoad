# Dockerfile

# Используем базовый образ Python
FROM python:3.9

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . .

# Устанавливаем зависимости из requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Устанавливаем системные зависимости для psycopg2 и Redis
RUN apt-get update && apt-get install -y gcc musl-dev

# Указываем порт, который должен быть доступен
EXPOSE 8000

# Команда для запуска сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
