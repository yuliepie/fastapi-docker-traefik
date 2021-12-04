## Docker commands
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

## Traefik architecture
-  Traefik is a reverse proxy service deployed in a container
-  Redirects web requests to appropriate services
### Flow
1. Client --> VM:8008
   1. Goes to Traefik:80 - web request processor
   2. Routes to appropriate service according to rules
   3. Here, requests for domain `fastapi.localhost` will be routed to fastapi API service
2. Client --> VM:8081
   1. Goes to Traefik:8080 - dashboard

## Traefik & HTTPS
- Traefik will automatically contact the certificate authority (Let's Encrypt) to issue and renew certificates.
- Certificates are required for HTTPS connection

###  Steps
- After securing a domain name, create the `traefik.prod.toml` config file
- Create mapping (A records) that point at the VM's public IP:
  - `fastapi-traefik.your-domain.com` - for the web service
  - `dashboard-fastapi-traefik.your-domain.com` - for the Traefik dashboard
- Update `docker-compose.prod.yml`
- Add `Dockerfile.traefik`
- Spin up new container
```bash
$ docker-compose -f docker-compose.prod.yml up -d --build
```
- Check the URLS work:
  - https://fastapi-traefik.your-domain.com
  - https://dashboard-fastapi-traefik.your-domain.com/dashboard
  - HTTP should redirect to HTTPS automatically.
### Create new password for traefik
```bash
# username: testuser
# password: password

$ echo $(htpasswd -nb testuser password) | sed -e s/\\$/\\$\\$/g
testuser:$$apr1$$jIKW.bdS$$eKXe4Lxjgy/rH65wP1iQe1
```
Store as env file `env_file`:
```bash
USERNAME=testuser
HASHED_PASSWORD=$$apr1$$jIKW.bdS$$eKXe4Lxjgy/rH65wP1iQe1
```