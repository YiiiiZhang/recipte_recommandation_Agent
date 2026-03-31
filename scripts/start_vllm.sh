#!/usr/bin/env bash
set -euo pipefail

MODEL_PATH="/dss/dssmcmlfs01/pn25ju/pn25ju-dss-0000/models/Qwen2.5-7B-Instruct"
PORT="8000"
API_KEY="EMPTY"
LOG_FILE="vllm.log"
PID_FILE="vllm.pid"

if [[ ! -d "$MODEL_PATH" ]]; then
  echo "Model path does not exist: $MODEL_PATH"
  exit 1
fi

echo "Starting vLLM on $(hostname) ..."
nohup vllm serve "$MODEL_PATH" \
  --host 0.0.0.0 \
  --port "$PORT" \
  --api-key "$API_KEY" \
  > "$LOG_FILE" 2>&1 &

echo $! > "$PID_FILE"
sleep 5

if ps -p "$(cat "$PID_FILE")" > /dev/null 2>&1; then
  echo "vLLM started. PID: $(cat "$PID_FILE")"
  echo "Log: $LOG_FILE"
  echo "Health check:"
  curl -s "http://127.0.0.1:${PORT}/v1/models" \
    -H "Authorization: Bearer ${API_KEY}" || true
else
  echo "vLLM failed to start."
  echo "Last 50 log lines:"
  tail -n 50 "$LOG_FILE" || true
  exit 1
fi