# Start Edge Container

```
docker pull ghcr.io/pragmaticindustries/portal-connect:latest
docker run -e FREQUENCY=5 -e PLC_ADDRESS="s7://192.168.167.210/0/0" -e PARAMETERS="{\"motor-current\": \"%DB444.DBD8:REAL\", \"position\": \"%DB444.DBD0:REAL\", \"rand_val\": \"%DB444.DBD4:REAL\"}" ghcr.io/pragmaticindustries/portal-connect:latest
```

# Start Database

```
docker run -d --name timescaledb -p 5432:5432 -e POSTGRES_PASSWORD=password timescale/timescaledb:latest-pg14
```

# Grafana

```
docker run -d -p 3000:3000 --link timescaledb --name grafana grafana/grafana
```

# Bridge

```
docker run -e DATABASE="postgresql://postgres:password@timescaledb:5432/postgres" --link timescaledb julianfeinauer/mbc-demo
```

