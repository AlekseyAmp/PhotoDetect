# Отслеживание карточек на площадке Wildberries

Проект предназначен для обнаружения фотографий

## Swagger
### 0.0.0.0:8000/docs

## Эндпоинты

### POST /images/detect
Загружает фото и возвращает JSON ответ..


   ```bash
   git clone https://github.com/AlekseyAmp/PhotoDetect
2. Создайте файл `.env` в директории `server` и укажите в нем свои данные, используя переменные окружения, представленные в `.env.example`.
3. Запустите проект с помощью команды:.

   ```bash
   docker-compose up
## После успешного запуска проекта выполните следующие действия:

### Применение миграций в базу данных

1. Откройте терминал.
2. Выполните команду:

   ```bash
   docker exec -it photodetect-server bash
3. Выполните следующую команду для применения миграций в базу данных:

   ```bash
   python -m src.composites.alembic_runner upgrade head
