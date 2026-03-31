#!/usr/bin/env bash
set -euo pipefail

PID_FILE="vllm.pid"

if [[ -f "$PID_FILE" ]]; then
  PID="$(cat "$PID_FILE")"
  if ps -p "$PID" > /dev/null 2>&1; then
    kill "$PID"
    echo "Stopped vLLM PID $PID"
  else
    echo "Process $PID not running"
  fi
  rm -f "$PID_FILE"
else
  echo "No pid file found"
fi