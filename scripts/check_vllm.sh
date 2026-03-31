#!/usr/bin/env bash
set -euo pipefail

PORT="8000"
API_KEY="EMPTY"
PID_FILE="vllm.pid"

echo "Host: $(hostname)"

if [[ -f "$PID_FILE" ]]; then
  PID="$(cat "$PID_FILE")"
  echo "PID file: $PID"
  ps -p "$PID" -f || true
else
  echo "No pid file found"
fi

echo
echo "Port check:"
ss -ltnp | grep ":${PORT}" || true

echo
echo "Health check:"
curl -s "http://127.0.0.1:${PORT}/v1/models" \
  -H "Authorization: Bearer ${API_KEY}" || true

echo
echo "Last 20 log lines:"
tail -n 20 vllm.log || true