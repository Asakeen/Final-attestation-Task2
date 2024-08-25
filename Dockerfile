# Используем базовый образ Python
FROM python:3.9

# Устанавливаем зависимости
RUN pip install psycopg2-binary

# Копируем файл app.py в контейнер
COPY app.py /app/app.py

# Устанавливаем рабочую директорию
WORKDIR /app

# Запускаем скрипт
CMD ["python", "app.py"]
