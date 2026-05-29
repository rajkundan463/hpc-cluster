import json
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--cpu", required=True)
parser.add_argument("--gpu", required=True)
parser.add_argument("--hpc", required=True)

args = parser.parse_args()

with open(args.cpu) as f:
cpu_data = json.load(f)

with open(args.gpu) as f:
gpu_data = json.load(f)

with open(args.hpc) as f:
hpc_data = json.load(f)

cpu_time = cpu_data["execution_time_sec"]
gpu_time = gpu_data["execution_time_sec"]
hpc_time = hpc_data["execution_time_sec"]

print("\n===== PERFORMANCE COMPARISON =====\n")

print(f"CPU Time : {cpu_time:.6f} sec")
print(f"GPU Time : {gpu_time:.6f} sec")
print(f"HPC Time : {hpc_time:.6f} sec")

print("\n===== SPEEDUP =====\n")

print(f"GPU vs CPU : {cpu_time / gpu_time:.2f}x")
print(f"HPC vs CPU : {cpu_time / hpc_time:.2f}x")
print(f"HPC vs GPU : {gpu_time / hpc_time:.2f}x")

print("\n===== SUMMARY =====\n")

best_time = min(cpu_time, gpu_time, hpc_time)

if best_time == cpu_time:
best = "CPU"
elif best_time == gpu_time:
best = "GPU"
else:
best = "HPC"

print(f"Fastest Execution Mode : {best}")
print(f"Best Runtime           : {best_time:.6f} sec")


# ===== PERFORMANCE COMPARISON =====

# CPU Time : 6.000000 sec
# GPU Time : 0.400000 sec
# HPC Time : 0.400000 sec

# ===== SPEEDUP =====

# GPU vs CPU : 15.00x
# HPC vs CPU : 15.00x
# HPC vs GPU : 1.00x

# ===== SUMMARY =====

# Fastest Execution Mode : GPU
# Best Runtime           : 0.400000 sec