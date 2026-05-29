# GPU-Accelerated Distributed HPC Cluster using Kubernetes, Ansible, CUDA & NVIDIA Runtime

## Overview

A production-style GPU-enabled High Performance Computing (HPC) cluster built using Kubernetes, Ansible, Containerd, Calico Networking, NVIDIA Runtime, and CUDA.

The cluster consists of one control plane node and two worker nodes, including a dedicated NVIDIA RTX 3050 GPU node for accelerated AI/ML workloads.

This project demonstrates:

* Automated cluster provisioning using Ansible
* Multi-node Kubernetes deployment
* Calico-based cluster networking
* NVIDIA GPU integration with Kubernetes
* CUDA-enabled container execution
* Matrix multiplication benchmarking
* Distributed workload scheduling
* HPC-ready architecture for AI/ML applications

---

## Cluster Architecture

```text
                    MASTER NODE
                172.31.65.147
             (Control Plane Node)

                         |
      ------------------------------------------------
      |                                              |
      |                                              |
+------------------+                    +------------------+
|     WORKER1      |                    |     WORKER2      |
| 172.31.65.144    |                    | 172.31.65.111    |
|                  |                    |                  |
| RTX 3050 GPU     |                    | CPU Worker       |
| CUDA Runtime     |                    | Compute Worker   |
+------------------+                    +------------------+

                Kubernetes + Calico CNI
```

---

## Technologies Used

### Infrastructure

* Ubuntu 22.04 LTS
* Kubernetes v1.29
* Containerd
* Calico CNI
* Ansible

### GPU Stack

* NVIDIA Driver
* NVIDIA Container Toolkit
* NVIDIA Device Plugin
* CUDA 12.x

### Benchmarking

* Python
* NumPy
* PyTorch

---

## Hardware Configuration

| Node    | Role          | CPU      | RAM   | GPU                 |
| ------- | ------------- | -------- | ----- | ------------------- |
| master  | Control Plane | 4 Cores  | 8 GB  | No                  |
| worker1 | GPU Worker    | 16 Cores | 16 GB | RTX 3050 Mobile 4GB |
| worker2 | CPU Worker    | 16 Cores | 16 GB | No                  |

---

## Kubernetes Cluster Verification

```bash
kubectl get nodes
```

Example Output:

```text
NAME      STATUS   ROLES           VERSION
master    Ready    control-plane   v1.29.15
worker1   Ready    <none>          v1.29.15
worker2   Ready    <none>          v1.29.15
```

---

## GPU Verification

```bash
nvidia-smi
```

Example Output:

```text
NVIDIA GeForce RTX 3050 Mobile
Driver Version: 535.x
CUDA Version: 12.x
```

---

## Kubernetes GPU Detection

```bash
kubectl describe node worker1
```

Example:

```text
Capacity:
  nvidia.com/gpu: 1
```

---

## Matrix Multiplication Benchmark

Matrix Size:

```text
5000 x 5000
```

### Results

| Execution Mode        | Time     |
| --------------------- | -------- |
| Single CPU            | ~6.0 sec |
| Single GPU (RTX 3050) | ~0.4 sec |

### Speedup

```text
GPU Speedup ≈ 15x
```

---

## Repository Structure

```text
gpu-hpc-kubernetes-cluster/
├── README.md
├── ansible/
├── kubernetes/
├── benchmarks/
├── docs/
└── screenshots/
```

---

## Future Work

* Distributed K-Means Clustering
* MPI-based Matrix Multiplication
* PyTorch Distributed Data Parallel (DDP)
* Kubeflow
* MLflow
* Ray Cluster
* JupyterHub
* Distributed Deep Learning Training

---

## Author

Kundan Kumar

Motilal Nehru National Institute of Technology

---

## License

MIT License
