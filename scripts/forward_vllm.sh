#!/usr/bin/env bash
set -euo pipefail

LOGIN_NODE="ra92miz2@login-02"
COMPUTE_NODE="mcmll-hgx-a100-006"
LOCAL_PORT="8000"
REMOTE_PORT="8000"

echo "Forwarding localhost:${LOCAL_PORT} -> ${COMPUTE_NODE}:${REMOTE_PORT} via ${LOGIN_NODE}"
echo "Press Ctrl+C to stop forwarding."

ssh -N -L ${LOCAL_PORT}:${COMPUTE_NODE}:${REMOTE_PORT} "${LOGIN_NODE}"