#!/usr/bin/env python3
# inspect_fake.py

import numpy as np
import sys

fake_npy = "/home/liuhui/repos/fish-speech/fake.npy"

try:
    tokens = np.load(fake_npy)
    print(f"🔍 fake.npy inspection:")
    print(f"   Shape: {tokens.shape}")
    print(f"   Data type: {tokens.dtype}")
    print(f"   Min value: {tokens.min()}")
    print(f"   Max value: {tokens.max()}")
    print(f"   Total elements: {tokens.size}")
    
    if tokens.ndim == 2:
        print(f"   Codebooks: {tokens.shape[0]}")
        print(f"   Frames: {tokens.shape[1]}")
        print(f"   First frame: {tokens[:, 0] if tokens.shape[0] > 0 else 'N/A'}")
    
    # Check if it's all zeros (fake/empty)
    if np.all(tokens == 0):
        print("⚠️  This appears to be a zero-filled tensor (placeholder)")
    else:
        print("✅ Contains non-zero values")
        
except Exception as e:
    print(f"Error: {e}")
