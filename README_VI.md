# Dr. Biết Tuốt

[![justforfunnoreally.dev badge](https://img.shields.io/badge/justforfunnoreally-dev-9ff)](https://justforfunnoreally.dev)

![Dr. Biết Tuốt](./res/screenshot.png)

Ứng dụng Streamlit này cung cấp giao diện giống Wikipedia để truy vấn mô hình ngôn ngữ OLLAMA. Người dùng có thể nhập câu hỏi và ứng dụng sẽ tạo phản hồi thông tin bằng mô hình OLLAMA được cấu hình.

## Cài đặt

1. Cài đặt các phụ thuộc cần thiết:
   ```
   pip install -r requirements.txt
   ```

2. Cấu hình file `.env` với URL API OLLAMA và tên mô hình của bạn (sao chép file `env.example` thành `.env` và chỉnh sửa).

3. Chạy ứng dụng Streamlit:
   ```
   streamlit run src/main.py
   ```

4. Mở trình duyệt web và truy cập URL được cung cấp bởi Streamlit (thường là `http://localhost:8501`).

## Mẹo sử dụng

- Bạn có thể sử dụng file `Dr. Biết Tuốt.desktop` hoặc `Dr. Biết Tuốt.bat` để chạy ứng dụng. Các file này cung cấp cửa sổ terminal cho ứng dụng và cách dễ dàng để khởi chạy bằng cách nhấp đúp.

## Cách sử dụng

1. Nhập câu hỏi của bạn vào khu vực văn bản được cung cấp.
2. Nhấp nút "Submit" để tạo phản hồi.
3. Ứng dụng sẽ hiển thị phản hồi được tạo bởi OLLAMA theo định dạng giống Wikipedia.

## Cấu hình

- Chỉnh sửa file `system_prompt.txt` để thay đổi lời nhắc hệ thống gửi đến mô hình OLLAMA.
- Cập nhật file `.env` để thay đổi URL API OLLAMA hoặc tên mô hình.
