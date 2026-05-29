# NVIDIA Device Plugin

The NVIDIA Device Plugin exposes GPU resources to Kubernetes.

Installation:

```bash
kubectl apply -f \
https://raw.githubusercontent.com/NVIDIA/k8s-device-plugin/v0.17.0/deployments/static/nvidia-device-plugin.yml
```

Verification:

```bash
kubectl describe node worker1
```

Expected:

```text
nvidia.com/gpu: 1
```

Test:

```bash
kubectl apply -f ../cuda-test.yaml

kubectl logs cuda-test
```