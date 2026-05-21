[![CI](https://github.com/Hmm-09876/Local_AWS_emulation-CI_CD_validation/actions/workflows/ci.yml/badge.svg)](https://github.com/Hmm-09876/Local_AWS_emulation-CI_CD_validation/actions/workflows/ci.yml)

[![CD](https://github.com/Hmm-09876/Local_AWS_emulation-CI_CD_validation/actions/workflows/cd.yml/badge.svg)](https://github.com/Hmm-09876/Local_AWS_emulation-CI_CD_validation/actions/workflows/cd.yml)

[![Security Scan](https://github.com/Hmm-09876/Local_AWS_emulation-CI_CD_validation/actions/workflows/sec-scan.yml/badge.svg)](https://github.com/Hmm-09876/Local_AWS_emulation-CI_CD_validation/actions/workflows/sec-scan.yml)
# Local_AWS_emulation-CI_CD_validation
This repository is a learning notebook for practicing DevOps and QA tools. It contains experiments and small demos using Terraform, LocalStack, pytest, Docker, GitHub Actions, GHCR, Trivy, Kubernetes, and Postman.

The project is not a production product. It stores steps you can run and the output files as evidence for learning or review.

**Quick start (simple checks)**

Prerequisites: Docker (Desktop), GNU Make, and a shell (Linux, macOS, or WSL on Windows).

1. Start LocalStack (see infra/localstack/docker-compose.yml):

```bash
docker compose -f infra/localstack/docker-compose.yml up -d
```

2. Create Terraform plan and apply locally (uses LocalStack):

```bash
make tf-plan
```

3. Collect evidence files (lambda list, logs, S3 listing, tf plan):

```bash
make evidence
```

4. Run tests:

```bash
pytest
```

Notes for Windows users: use WSL or Git Bash for best compatibility with `make` and LocalStack commands.

## What this repo shows (short)

- Terraform + LocalStack: practice writing infra code and running it locally.
- Python + pytest: example unit tests and simple verification.
- Docker & GitHub Actions: how images are built and scanned.
- Kubernetes manifests: simple examples for deployments and services.
- Postman: small smoke tests and exported collections kept as evidence.

## Evidence folder

See the `evidence/` folder for outputs created during runs. Typical commands that produce these files are in the top-level `Makefile` (`make evidence`, `make tf-plan`).

***

