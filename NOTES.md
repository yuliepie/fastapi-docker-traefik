Build & run the Docker image:
```bash
$ docker-compose build

$ docker-compose up -d
```

Bring down containers and volumes
```bash
$ docker-compose down -v
```

Run production docker
```bash
$ docker-compose -f docker-compose.prod.yml up -d --build
```

Check docker logs:
```bash
docker-compose logs -f
```

Check db
- List dbs
- Connect to db
- check tables
- quit
```bash
$ docker-compose exec db psql --username=fastapi_traefik --dbname=fastapi_traefik

fastapi_traefik=# \l
fastapi_traefik=# \dt

fastapi_traefik=# \q
```

Check db volume created
```bash
$ docker volume inspect fastapi-docker-traefik_postgres_data
```

## Ormar
- An ORM that is built on top of SQLAlchemy and Pydantic
- Ormar models serve as both Pydantic & database models
- Uses SQLAlchemy for creating tables & queries
- Uses databases for async execution of queries
- pydantic for model validation

## production docker file
- The prod docker file uvicorn-gunicorn uses gunicorn to manage uvicorn processes
- utilizes a `prestart.sh` script which can be used to wait for db to start