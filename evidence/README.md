# Evidence

This folder is where outputs generated during the practice process are stored. It includes:
- How Terraform executed
- How LocalStack responded
- Which tests passed and which failed
- Outputs that may need to be reviewed later

## How to read this folder

Each file here represents a step in the practice flow.

### Terraform / LocalStack
- `tf-plan.json`  
  Output of Terraform plan. Used to preview what Terraform will do.

- `tf-show.txt`  
  Output after apply. Used to compare actual resources.

- `lambda-list.json`  
  Result of listing Lambda functions after creation, or evidence that the Lambda exists.

- `lambda-invoke.json`  
  Result of invoking Lambda. Shows that the Lambda executed successfully.

- `lambda-logs.json`  
  Runtime logs of the Lambda.

- `s3-ls.txt`  
  Result of checking S3 buckets / objects.

- `evidence/postman/`  
  API testing files using Postman will be added here later.

## Purpose of this folder

These files are kept to:
- Review what has been done
- Identify what worked and what didn’t
- Provide clear evidence when reviewing the project