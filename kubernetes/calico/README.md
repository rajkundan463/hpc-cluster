# Calico CNI

Calico provides networking and network policy support for the Kubernetes cluster.

Installation:

```bash
kubectl apply -f \
https://raw.githubusercontent.com/projectcalico/calico/v3.28.0/manifests/calico.yaml
```

Verification:

```bash
kubectl get pods -n kube-system
```

Expected:

```text
calico-node
calico-kube-controllers
```