# Django-postgres-docker

This is a boilerplate for django, postgres and docker compose.

Setup

```bash
cp .env.example .env
docker-compose build
docker-compose up
docker-compose exec django python manage.py createsuperuser
```
