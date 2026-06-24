#!/usr/bin/env python3
import argparse
import pathlib
import requests


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="输入 txt 文件")
    parser.add_argument("--url", default="http://127.0.0.1:9090/v1/tts")
    parser.add_argument("--reference-id", default="qingminyi")
    parser.add_argument("--format", default="mp3", choices=["wav", "mp3", "opus", "pcm"])
    parser.add_argument("--chunk-length", type=int, default=200)
    parser.add_argument("--max-new-tokens", type=int, default=1024)
    parser.add_argument("--top-p", type=float, default=0.8)
    parser.add_argument("--repetition-penalty", type=float, default=1.2)
    parser.add_argument("--temperature", type=float, default=0.8)
    parser.add_argument("--use-memory-cache", default="on", choices=["on", "off"])
    args = parser.parse_args()

    input_path = pathlib.Path(args.file)
    text = input_path.read_text(encoding="utf-8").strip()

    payload = {
        "text": text,
        "reference_id": args.reference_id,
        "format": args.format,
        "chunk_length": args.chunk_length,
        "max_new_tokens": args.max_new_tokens,
        "top_p": args.top_p,
        "repetition_penalty": args.repetition_penalty,
        "temperature": args.temperature,
        "use_memory_cache": args.use_memory_cache,
        "streaming": False,
        "normalize": True,
    }

    resp = requests.post(args.url, json=payload, timeout=600)
    resp.raise_for_status()

    out_path = input_path.with_suffix(f".{args.format}")
    out_path.write_bytes(resp.content)
    print(f"saved: {out_path}")


if __name__ == "__main__":
    main()
