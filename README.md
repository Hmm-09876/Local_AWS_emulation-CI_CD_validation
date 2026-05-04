[![CI](https://github.com/Hmm-09876/demo-3/actions/workflows/ci.yml/badge.svg)](https://github.com/Hmm-09876/demo-3/actions/workflows/ci.yml)

[![CD](https://github.com/Hmm-09876/demo-3/actions/workflows/cd.yml/badge.svg)](https://github.com/Hmm-09876/demo-3/actions/workflows/cd.yml)

[![Security Scan](https://github.com/Hmm-09876/demo-3/actions/workflows/sec-scan.yml/badge.svg)](https://github.com/Hmm-09876/demo-3/actions/workflows/sec-scan.yml)
# demo-3

This repo is a place to record the learning process and hands-on practice with basic tools and flows in DevOps / QA, such as Terraform, LocalStack, pytest, Docker, GitHub Actions, GHCR, Trivy, Kubernetes, and Postman.

The goal of this repo is not to be a complete production project. It is more like a practice notebook: try things out, run them, verify them, then store evidence so it can be reviewed later.

## What has been learned and tried

### 1. Terraform and LocalStack
- Get familiar with Terraform for infrastructure declaration
- Use LocalStack to simulate AWS locally
- Manually test Lambda, S3, and related resources
- Practice reading plan, apply, and output after execution

### 2. Python and pytest
- Write tests in Python
- Use pytest to verify basic behavior
- Get used to testing not just for passing, but also for generating storable outputs

### 3. Docker, GitHub Actions, GHCR, Trivy
- Build images with Docker
- Run workflows with GitHub Actions
- Push images to GHCR
- Scan images with Trivy
- Gradually understand the flow from code to artifact

### 4. Kubernetes
- Get familiar with manifests
- Practice basic deployments
- Practice checking rollout and deployment status

### 5. Postman / API testing
- Use the small app in the repo to test basic APIs
- Create collections, environments, and smoke tests
- Save exported files as evidence

## Evidence

The evidence/ folder is where files generated during test runs, plan, apply, and result verification are stored.

Each file is a trace of a specific step. Looking at this folder, the goal is to quickly understand:
- What was run
- What the results were
- Which file proves which step

***
## Installation and reference sources

Docker Engine: 
https://docs.docker.com/engine/install/ubuntu/

Terraform: 
https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli

kind:
https://kind.sigs.k8s.io/docs/user/quick-start/

kubectl:
https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/

Python, pip, Make: 
```
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.10 python3-pip make
```

***
## Pull & run image from GHCR
```
docker pull ghcr.io/hmm-09876/demo-3/demo-app:ci-54fca15914be974f1fed0ae748c076fba4f39c4b
```

