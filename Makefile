server:
	python manage.py runserver

makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

fill_db:
	python manage.py fill_db

run_bot:
	python manage.py run_bot

ngrok:
	ngrok http 8000

set_webhook:
	python manage.py set_webhook

remove_webhook:
	python manage.py remove_webhook