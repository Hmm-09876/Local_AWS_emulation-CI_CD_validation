[![CI](https://github.com/Hmm-09876/demo-3/actions/workflows/ci.yml/badge.svg)](https://github.com/Hmm-09876/demo-3/actions/workflows/ci.yml)

[![CD](https://github.com/Hmm-09876/demo-3/actions/workflows/cd.yml/badge.svg)](https://github.com/Hmm-09876/demo-3/actions/workflows/cd.yml)

[![Security Scan](https://github.com/Hmm-09876/demo-3/actions/workflows/sec-scan.yml/badge.svg)](https://github.com/Hmm-09876/demo-3/actions/workflows/sec-scan.yml)
# demo-3

Repo này là chỗ ghi lại quá trình học và tự tay thực hành với các tool và flow cơ bản trong DevOps / QA, như Terraform, LocalStack, pytest, Docker, GitHub Actions, GHCR, Trivy, Kubernetes và Postman.

Mục tiêu của repo này không phải là một project production hoàn chỉnh. Nó giống một cuốn sổ thực hành hơn: làm thử, chạy thử, kiểm tra lại, rồi lưu evidence để sau này còn xem lại được.

## Đã học và thử những gì

### 1. Terraform và LocalStack
- Làm quen với Terraform để khai báo hạ tầng
- Dùng LocalStack để mô phỏng AWS trên máy local
- Tự kiểm tra Lambda, S3 và các resource liên quan
- Tập đọc plan, apply và output sau khi chạy

### 2. Python và pytest
- Viết test bằng Python
- Dùng pytest để kiểm tra hành vi cơ bản
- Tập quen với việc test không chỉ để pass, mà còn để tạo ra output có thể lưu lại

### 3. Docker, GitHub Actions, GHCR, Trivy
- Build image bằng Docker
- Chạy workflow bằng GitHub Actions
- Push image lên GHCR
- Scan image bằng Trivy
- Hiểu dần flow từ code tới artefact

### 4. Kubernetes
- Làm quen với manifest
- Tập deploy cơ bản
- Tập kiểm tra rollout và trạng thái triển khai

### 5. Postman / API testing
- Dùng app nhỏ trong repo để test API cơ bản
- Tạo collection, environment và smoke test
- Lưu file export lại làm evidence

## Evidence

Folder `evidence/` là nơi lưu các file sinh ra trong quá trình chạy test, plan, apply và kiểm tra kết quả.

Mỗi file trong đó là một dấu vết của một bước cụ thể. Nhìn lại folder này, mình muốn biết nhanh:
- Đã chạy gì
- Kết quả ra sao
- File nào đang chứng minh cho bước nào

***
## Nguồn cài và tham khảo

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
## Pull & run image từ GHCR
```
docker pull ghcr.io/hmm-09876/demo-3/demo-app:ci-54fca15914be974f1fed0ae748c076fba4f39c4b
```

