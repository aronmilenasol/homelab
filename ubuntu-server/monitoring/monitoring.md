# :computer: Monitoring

This directory contains the configuration files used to monitor my Ubuntu Server using **Docker**, **Prometheus**, and **Grafana**.

## Technologies used:

- [Docker](https://www.docker.com/)
- [Prometheus](https://prometheus.io/)
- [Grafana](https://grafana.com/)
- [Node Exporter](https://github.com/prometheus/node_exporter)

## Purpose and features

With this setup, I can monitor system metrics from my Ubuntu Server (such as CPU, memory, disk, and network usage) using the [Node Exporter Full](https://grafana.com/grafana/dashboards/1860-node-exporter-full/) Grafana dashboard.

I also configured email alerts for key metrics like:

- High CPU usage
- Low memory availability
- Low disk space

These alerts help me stay aware of issues.

## Directory structure

```bash
.
├── docker-compose.yml
└── prometheus
    └── prometheus.yml

```

## Files

- `docker-compose.yml`: Docker Compose file for running Prometheus and Grafana.
- `prometheus/prometheus.yml`: Prometheus configuration file.

## Usage

1. Copy the files to the desired directory and run `docker-compose up -d` to start the containers.
2. Open Grafana at `http://localhost:3000` to view the dashboard.
3. Import the [Node Exporter Full](https://grafana.com/grafana/dashboards/1860-node-exporter-full/) dashboard.
