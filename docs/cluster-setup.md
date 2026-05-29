# Kubernetes HPC Cluster Setup Guide

## Cluster Overview

This project implements a GPU-enabled High Performance Computing (HPC) cluster using Kubernetes, Ansible, NVIDIA Runtime, CUDA, and Calico Networking.

## Cluster Nodes

| Node | IP Address | Role |
|--------|--------|--------|
| master | 172.31.65.147 | Kubernetes Control Plane |
| worker1 | 172.31.65.144 | GPU Worker |
| worker2 | 172.31.65.111 | CPU Worker |

---

## Hardware Configuration

### Master Node

- 8 GB RAM
- Ubuntu 22.04 LTS
- Kubernetes Control Plane

### Worker1

- 16 GB RAM
- NVIDIA GeForce RTX 3050 Mobile
- CUDA Enabled
- Kubernetes Worker

### Worker2

- 16 GB RAM
- CPU Compute Worker

---

## Network Configuration

### Proxy

```bash
http://edcguest:edcguest@172.31.100.25:3128/
```

### NO_PROXY

```bash
localhost
127.0.0.1
master
worker1
worker2
172.31.65.147
172.31.65.144
172.31.65.111
10.96.0.0/12
10.244.0.0/16
```

---

## Kubernetes Components

### Runtime

- containerd

### Network Plugin

- Calico CNI

### GPU Stack

- NVIDIA Driver
- NVIDIA Container Toolkit
- NVIDIA Device Plugin
- CUDA Runtime

---

## Kubernetes Installation

### Initialize Cluster

```bash
sudo kubeadm init \
--pod-network-cidr=10.244.0.0/16 \
--cri-socket=unix:///run/containerd/containerd.sock
```

### Configure Kubectl

```bash
mkdir -p $HOME/.kube

sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config

sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

---

## Install Calico

```bash
kubectl apply -f \
https://raw.githubusercontent.com/projectcalico/calico/v3.28.0/manifests/calico.yaml
```

---

## Join Worker Nodes

```bash
kubeadm join ...
```

---

## Verify Cluster

```bash
kubectl get nodes
```

Expected:

```text
master    Ready
worker1   Ready
worker2   Ready
```

---

## GPU Enablement

Install NVIDIA Device Plugin:

```bash
kubectl apply -f \
https://raw.githubusercontent.com/NVIDIA/k8s-device-plugin/v0.17.0/deployments/static/nvidia-device-plugin.yml
```

Verify:

```bash
kubectl describe node worker1
```

Expected:

```text
nvidia.com/gpu: 1
```

---

## Cluster Architecture

                    MASTER
                172.31.65.147

                      |
      ----------------------------------

      |                                |

   WORKER1                        WORKER2

  RTX 3050 GPU                   CPU Worker

      ----------------------------------

                Calico Network

                      |

                Kubernetes