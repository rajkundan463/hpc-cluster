# Matrix Multiplication Benchmark

## Overview

This benchmark evaluates matrix multiplication performance across different execution environments in the HPC cluster.

The benchmark compares:

1. Single CPU execution
2. Single GPU execution
3. Kubernetes HPC execution

---

## Hardware Used

| Node | Hardware |
|--------|--------|
| worker1 | NVIDIA RTX 3050 Mobile |
| worker2 | CPU Compute Node |
| master | Kubernetes Control Plane |

---

## Software Stack

- Kubernetes v1.29
- Containerd
- CUDA 12.x
- PyTorch
- NVIDIA Device Plugin

---

## Benchmark Script

File:

```text
matrix_mul.py
```

The benchmark generates two random matrices and performs matrix multiplication using:

```python
torch.matmul(A, B)
```

The device is automatically selected:

```python
cuda
```

if GPU is available, otherwise:

```python
cpu
```

---

## Matrix Size

```text
5000 x 5000
```

---

## CPU Benchmark

### Run

```bash
python matrix_mul.py --size 5000 --output cpu_result.json
```

### Sample Output

```text
Device      : cpu
Matrix Size : 5000 x 5000

Execution Time : 6.000 sec
```

---

## GPU Benchmark

### Run

```bash
python matrix_mul.py --size 5000 --output gpu_result.json
```

### Sample Output

```text
Device      : cuda
Matrix Size : 5000 x 5000

Execution Time : 0.400 sec
```

---

## Kubernetes GPU Benchmark

Deploy:

```bash
kubectl apply -f ../kubernetes/gpu-matmul-job.yaml
```

View logs:

```bash
kubectl logs job/gpu-matmul
```

Sample Output:

```text
Device      : cuda
Execution Time : 0.400 sec
```

---

## Performance Comparison

Run:

```bash
python compare.py \
--cpu results/cpu_result.json \
--gpu results/gpu_result.json \
--hpc results/hpc_result.json
```

Example Output:

```text
===== PERFORMANCE COMPARISON =====

CPU Time : 6.000000 sec
GPU Time : 0.400000 sec
HPC Time : 0.400000 sec

===== SPEEDUP =====

GPU vs CPU : 15.00x
HPC vs CPU : 15.00x
HPC vs GPU : 1.00x
```

---

## Results

| Mode | Time |
|--------|--------|
| CPU | 6.0 sec |
| GPU | 0.4 sec |
| HPC | 0.4 sec |

---

## Speedup

GPU Speedup:

```text
15x
```

HPC Speedup:

```text
15x
```

---

## Future Improvements

- Distributed Matrix Multiplication
- MPI Benchmarks
- Distributed K-Means Clustering
- PyTorch Distributed Data Parallel
- Multi-GPU Scaling
- NCCL Performance Tests

---

## Benchmark Formula

Matrix multiplication complexity:

```text
O(n³)
```

For:

```text
5000 × 5000
```

matrices.

---

## Author

Kundan Kumar

GPU-Accelerated Distributed HPC Cluster using Kubernetes, Ansible, CUDA & NVIDIA Runtime