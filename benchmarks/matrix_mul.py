import torch
import time
import argparse
import json
import os

parser = argparse.ArgumentParser()

parser.add_argument(
"--size",
type=int,
default=5000,
help="Matrix dimension"
)

parser.add_argument(
"--output",
type=str,
default="result.json",
help="Output JSON file"
)

args = parser.parse_args()

N = args.size

device = "cuda" if torch.cuda.is_available() else "cpu"

print("=" * 60)
print("GPU HPC Kubernetes Benchmark")
print("=" * 60)

print(f"Device      : {device}")
print(f"Matrix Size : {N} x {N}")


A = torch.randn(N, N, device=device)
B = torch.randn(N, N, device=device)

# Warm-up for CUDA

if device == "cuda":
torch.cuda.synchronize()

start = time.perf_counter()

C = torch.matmul(A, B)

if device == "cuda":
torch.cuda.synchronize()

end = time.perf_counter()

elapsed = end - start



print(f"Execution Time : {elapsed:.6f} sec")

if device == "cuda":
print(
f"GPU Name       : "
f"{torch.cuda.get_device_name(0)}"
)


result = {
"device": device,
"matrix_size": N,
"execution_time_sec": elapsed
}

if device == "cuda":
result["gpu"] = torch.cuda.get_device_name(0)

with open(args.output, "w") as f:
json.dump(result, f, indent=4)

print("\nResult Saved:", args.output)

print("=" * 60)
print("Benchmark Completed")
print("=" * 60)
