import torch
import time
import json

N = 5000

device = "cuda"

A = torch.randn(N, N, device=device)
B = torch.randn(N, N, device=device)

torch.cuda.synchronize()

start = time.perf_counter()

C = torch.matmul(A, B)

torch.cuda.synchronize()

end = time.perf_counter()

elapsed = end - start

result = {
    "device": "cuda",
    "matrix_size": N,
    "execution_time_sec": elapsed,
    "gpu": torch.cuda.get_device_name(0)
}

with open("gpu_result.json", "w") as f:
    json.dump(result, f, indent=4)

print(f"GPU Time: {elapsed:.6f} sec")