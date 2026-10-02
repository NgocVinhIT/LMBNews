# 🚀 LMBNews - Nền Tảng Chia Sẻ Kiến Thức, Phim & Sách

**LMBNews** là một ứng dụng web nhỏ gọn được xây dựng bằng framework **Flask (Python)** và giao diện **Bootstrap 5**. Đây là nơi mọi người có thể tự do chia sẻ, lưu trữ và đọc các bài viết thuộc 3 chủ đề cốt lõi:
*   📚 **L**earn: Chia sẻ phương pháp, kiến thức học tập.
*   🍿 **M**ovie: Đánh giá, review các bộ phim điện ảnh bom tấn.
*   📖 **B**ook: Cảm nhận, review các cuốn sách hay nên đọc.

---

## ✨ Tính Năng Nổi Bật

- **Bố cục tối giản & mượt mà:** Giao diện dạng thẻ (Card) chuẩn responsive, giúp máy chạy nhẹ nhàng không bị mỏi.
- **Phân loại thông minh:** Lọc bài viết nhanh chóng theo từng chuyên mục Learn, Movie, Book ngay trên thanh Menu.
- **Đánh giá trực quan:** Tự động hiển thị ô chấm điểm từ 1 đến 5 sao (⭐) khi người dùng viết bài review Phim hoặc Sách.
- **Cơ sở dữ liệu tích hợp:** Sử dụng SQLite siêu nhẹ, tự động khởi tạo dữ liệu ngay lần chạy đầu tiên.

---

## 🌐 Hướng Dẫn Sử Dụng & Trải Nghiệm

### 🌍 Cách 1: Sử dụng trực tiếp trên Web (Không cần cài đặt)
> 📢 **Thông báo:** Nếu bạn không muốn cài đặt và chạy mã nguồn trên máy tính cá nhân, phiên bản Web trực tuyến chính thức của **LMBNews** đang được cấu hình và sẽ **chính thức mở truy cập công khai sau 10 ngày nữa**! Đường link truy cập sẽ được cập nhật ngay tại đây.

### 💻 Cách 2: Chạy thử nghiệm trên máy tính (Localhost)
Nếu muốn chạy thử mã nguồn ngay bằng VS Code, bạn hãy làm theo các bước sau:

**1. Cài đặt các thư viện cần thiết:**
Mở Terminal trong VS Code và cài đặt các gói phụ thuộc (Lưu ý phiên bản `greenlet` phù hợp cho Windows nếu gặp lỗi):
```bash
pip install "greenlet<3.0.0"
pip install Flask Flask-SQLAlchemy
```

**2. Khởi chạy ứng dụng:**
```bash
python app.py
```

**3. Truy cập trang web local:**
Mở trình duyệt internet và truy cập vào đường dẫn: `http://127.0.0.1:5000`

---

## 📂 Cấu Trúc Thư Mục Dự Án
```text
lmbnews/
│
├── app.py               # File xử lý Backend chính (Flask)
├── database.db          # Cơ sở dữ liệu SQLite (Tự động sinh ra)
│
├── templates/           # Thư mục chứa giao diện HTML (Jinja2)
│   ├── base.html        # Giao diện khung và thanh điều hướng Navbar
│   ├── index.html       # Trang chủ hiển thị danh sách bài viết mới nhất
│   ├── category.html    # Trang lọc bài viết theo từng chuyên mục riêng biệt
│   └── create_post.html # Giao diện biểu mẫu đăng bài viết mới
│
└── README.md            # Tài liệu hướng dẫn dự án (File này)
```

---
Dự án được phát triển và quản lý bởi **NgocVinhIT** 🎯
