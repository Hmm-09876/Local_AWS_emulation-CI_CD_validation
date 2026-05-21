# Evidence
This folder holds outputs created when running the examples in the repo. Files show what commands did and help reviewers see the results.

How to use this folder (short): run the commands below, then open the files to see the outputs.

Common files:

- `tf-plan.json` — Terraform plan output (preview of changes).
- `tf-show.txt` — Terraform apply/show output (actual resources after apply).
- `lambda-list.json` — Result of listing Lambda functions.
- `lambda-invoke.json` — Result of invoking a Lambda function.
- `lambda-logs.json` — Lambda runtime logs.
- `s3-ls.txt` — S3 listing output.
- `postman/` — Postman collections, environments, and run notes.

Quick commands (from repo root):

```bash
# start LocalStack
docker compose -f infra/localstack/docker-compose.yml up -d

# create plan and apply locally
make tf-plan

# gather evidence files
make evidence
```

Purpose: keep a clear record of what was run and what happened. Use these files when you review or write a short report.