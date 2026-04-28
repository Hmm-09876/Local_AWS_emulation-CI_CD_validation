# Evidence

Folder này là nơi giữ lại các output sinh ra trong quá trình thực hành. Gồm:
- Terraform đã chạy ra sao
- LocalStack đã phản hồi như thế nào
- Test nào pass, test nào fail
- Output nào cần xem lại sau này

## Cách đọc folder này

Mỗi file ở đây đại diện cho một bước trong flow thực hành.

### Terraform / LocalStack
- `tf-plan.json`  
  Output của Terraform plan. Dùng để xem trước Terraform sẽ làm gì.

- `tf-show.txt`  
  Output sau khi apply. Dùng để đối chiếu resource thực tế.

- `lambda-list.json`  
  Kết quả liệt kê Lambda sau khi tạo xong, hoặc bằng chứng là Lambda đã tồn tại.

- `lambda-invoke.json`  
  Kết quả invoke Lambda. Cho thấy Lambda đã chạy được.

- `lambda-logs.json`  
  Log runtime của Lambda.

- `s3-ls.txt`  
  Kết quả kiểm tra S3 bucket / object.

- `evidence/postman/`  
  Các API testing bằng Postman sau này sẽ được thêm vào đây.

## Mục đích của folder này

Các file này được giữ lại để:
- Xem lại quá trình mình đã làm
- Biết chỗ nào đã đúng, chỗ nào chưa đúng
- Có bằng chứng rõ ràng khi cần review lại project



