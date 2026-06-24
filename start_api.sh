#!/usr/bin/env bash
set -e

REPO_DIR=/home/liuhui/repos/fish-speech

source activate fish-speech
cd "$REPO_DIR"

python tools/api_server.py \
  --listen 127.0.0.1:9090 \
  --llama-checkpoint-path "$REPO_DIR/checkpoints/openaudio-s1-mini" \
  --decoder-checkpoint-path "$REPO_DIR/checkpoints/openaudio-s1-mini/codec.pth" \
  --device cuda \
  --compile \
  --workers 1
