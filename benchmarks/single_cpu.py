import torch
import time
import json

N = 5000

device = "cpu"

A = torch.randn(N, N)
B = torch.randn(N, N)

start = time.perf_counter()

C = torch.matmul(A, B)

end = time.perf_counter()

elapsed = end - start

result = {
    "device": "cpu",
    "matrix_size": N,
    "execution_time_sec": elapsed
}

with open("cpu_result.json", "w") as f:
    json.dump(result, f, indent=4)

print(f"CPU Time: {elapsed:.6f} sec")