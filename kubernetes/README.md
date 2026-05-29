# Kubernetes Job Scheduling

This directory contains Kubernetes Job manifests used to benchmark CPU and GPU performance.

## Files

- cpu-matmul-job.yaml
- gpu-matmul-job.yaml
- cuda-test.yaml

## Scheduling Strategy

CPU Job:

```yaml
nodeSelector:
  accelerator: cpu