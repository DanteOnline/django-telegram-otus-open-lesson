# django-telegram-otus-open-lesson
Code for otus open lesson "Django+Telegram bot"

## Step 2.2. Sync Djagno + Sync Telebot + Webhook

Для использования webhook нужен: 
- ssl (https), используется ngrok для локального запуска
- endpoint для получения обновлений

## Usage

```commandline
pip install -r requirements.txt
```

```commandline
make migrate
```

```commandline
make server
```

```commandline
make ngrok
```

```commandline
make set_webhook
```
