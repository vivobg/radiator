# Radiator

## Create test database using docker

```bash
docker run -p 5432:5432 --name radiatordb -e POSTGRES_PASSWORD=radiator -e POSTGRES_USER=radiator -e POSTGRES_DB=radiator -d postgres
```
