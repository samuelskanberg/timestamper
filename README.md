# Django-postgres-docker

This is a boilerplate for django, postgres and docker compose.

## Setup

```bash
cp .env.example .env
docker-compose build
docker-compose up
docker-compose exec django python manage.py createsuperuser
```

## Next step

[Create an app](https://docs.djangoproject.com/en/3.1/intro/tutorial01/):

```bash
docker-compose exec django python manage.py startapp polls
```

Remember that everything created from within docker will be with root permissions.
