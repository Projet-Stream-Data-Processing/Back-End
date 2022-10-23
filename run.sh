#!/bin/bash

exec python3 server.py &
exec python3 gatewayData.py &
exec python3 API_GRAFANA/main.py