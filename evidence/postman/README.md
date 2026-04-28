# Postman Evidence

Folder này chứa các file liên quan tới API testing bằng Postman.

Mục tiêu của folder này là lưu lại quá trình học cách dùng Postman để test API cơ bản, rồi giữ luôn kết quả test thành evidence.

## Trong folder này có gì

### `demo-3.postman_collection.json`
Collection chứa các request mình tạo để test app trong repo.

Các request cơ bản:
- `GET /`
- `GET /health`
- `GET /no-such-route`

### `demo-3.local.postman_environment.json`
Environment chứa biến dùng khi chạy local.

Biến chính:
- `base_url = http://localhost:8080`

### `run-notes.md`
File ghi chú ngắn về lần chạy test:
- App đang chạy ở URL nào
- Đã test những request nào
- Pass hay fail
- Có gì cần chỉnh lại

## Mục tiêu

Postman này chỉ được dùng ở mức smoke test, tức là kiểm tra nhanh những gì app đang có.

Kỳ vọng:
- `GET /` trả `200` và body có `status: ok`
- `GET /health` trả `200` và body có `status: ok`
- `GET /no-such-route` trả `404`

## Học được gì ở phần này

- Cách tạo request trong Postman
- Cách dùng environment để đổi URL nhanh
- Cách viết test cơ bản cho response
- Cách export collection và environment để giữ làm evidence
