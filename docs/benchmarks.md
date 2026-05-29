# Benchmark Results

## Objective

Evaluate matrix multiplication performance on:

1. Single CPU Node
2. Single GPU Node
3. Kubernetes HPC Cluster

---

## Test Configuration

### Matrix Size

```text
5000 x 5000
```

### Framework

- PyTorch
- CUDA 12.x
- Kubernetes Jobs

---

## CPU Benchmark

Node:

```text
worker2
```

Command:

```bash
python matrix_mul.py --size 5000
```

Result:

```text
Execution Time : 6.0 sec
```

---

## GPU Benchmark

Node:

```text
worker1
```

GPU:

```text
NVIDIA RTX 3050 Mobile
```

Command:

```bash
python matrix_mul.py --size 5000
```

Result:

```text
Execution Time : 0.4 sec
```

---

## HPC Benchmark

Framework:

```text
Kubernetes Job Scheduling
```

Result:

```text
Execution Time : 0.4 sec
```

---

## Comparison

| Mode | Execution Time |
|--------|--------|
| CPU | 6.0 sec |
| GPU | 0.4 sec |
| HPC | 0.4 sec |

---

## Speedup

GPU vs CPU:

```text
15x
```

HPC vs CPU:

```text
15x
```

---

## Analysis

The GPU-enabled worker node significantly outperformed CPU execution.

The RTX 3050 Mobile completed matrix multiplication approximately 15 times faster than CPU execution.

The Kubernetes cluster successfully scheduled GPU workloads through the NVIDIA Device Plugin and NVIDIA Container Runtime.

---

## Future Work

- Distributed Matrix Multiplication
- MPI
- Distributed K-Means Clustering
- PyTorch Distributed Data Parallel
- Kubeflow
- MLflow
- JupyterHub