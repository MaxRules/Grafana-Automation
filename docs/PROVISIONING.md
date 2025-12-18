# Grafana Provisioning (examples)

Grafana supports provisioning datasources and dashboards via YAML + JSON files placed in the provisioning directories.

Example datasource (`provisioning/datasources/example-datasource.yaml`):

apiVersion: 1
datasources:
  - name: Prometheus
    type: prometheus
    access: proxy
    url: http://prometheus:9090

Dashboards
- Place dashboard JSON files under `provisioning/dashboards/` or provide a provider entry that points to a directory/URL.

Example provider (short):

apiVersion: 1
providers:
  - name: 'default'
    orgId: 1
    folder: ''
    type: file
    options:
      path: /var/lib/grafana/dashboards

See Grafana docs for more details: https://grafana.com/docs/grafana/latest/administration/provisioning/
