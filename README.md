# 🐺 Grey Wolf Optimization (GWO) - Group XX  
## Project Demo: Thuật toán Tối ưu hóa Sói Xám (Grey Wolf Optimizer)  
**Đề tài:** Tìm hiểu và cài đặt thuật toán GWO cùng ví dụ minh họa tối ưu hóa hàm số liên tục.

---

## 1. Giới thiệu (Introduction)

Đây là phần demo mã nguồn thuộc báo cáo bài tập lớn của **Nhóm XX**.  
Trong dự án này, chúng tôi cài đặt và minh họa hoạt động của **Grey Wolf Optimizer (GWO)** — thuật toán tối ưu hóa mô phỏng hành vi săn mồi của sói xám trong tự nhiên.

### 🔎 Mục tiêu của bản demo
- Minh họa cách GWO tìm nghiệm tối ưu trong không gian liên tục.  
- Thử nghiệm trên bài toán tối ưu hàm số phi tuyến:  
  \[
  f(x, y) = x^2 + y^2 + 5\sin(x)
  \]
- Quan sát đường hội tụ và nghiệm tối ưu mà GWO tìm thấy.  
- Làm nền tảng cho việc mở rộng sang các bài toán phức tạp hơn.

---

## Thông tin nhóm thực hiện (Team Members)

| STT | Họ và tên | MSSV | Vai trò |
|----|-----------|-------|---------|
| 1  |Vũ Huy Hoàng|20235732|Nghiên cứu lý thuyết & Code|
| 2  |Nguyễn Minh Tiệp|20235845|Nghiên cứu biến thể & Báo cáo|

## 2. Chi tiết thuật toán (Algorithm Implementation)

### 🐺 Thuật toán sử dụng: **Grey Wolf Optimizer (GWO)**

GWO mô phỏng 4 cấp bậc trong bầy sói:

- **Alpha (α)** — nghiệm tốt nhất  
- **Beta (β)** — nghiệm tốt thứ hai  
- **Delta (δ)** — nghiệm tốt thứ ba  
- **Omega (ω)** — phần còn lại

Ba con đầu đàn hướng dẫn việc di chuyển của toàn bộ bầy sói trong quá trình tối ưu.

---

### ⚙️ Quy tắc cập nhật vị trí

Tại mỗi vòng lặp:

- Sói di chuyển dựa trên khoảng cách đến α, β, δ  
- Hệ số kiểm soát **a** giảm tuyến tính từ 2 → 0  
- Vị trí mới được tính từ 3 vector ứng viên:

\[
X(t+1) = \frac{X_1 + X_2 + X_3}{3}
\]

---

### 🧪 Bài toán Demo: Tối ưu hàm phi tuyến

Hàm cần tối ưu:

\[
f(x, y) = x^2 + y^2 + 5\sin(x)
\]

Miền tìm kiếm:

\[
-5 \le x, y \le 5
\]

Lý do chọn hàm này:

- Có nhiều cực trị cục bộ → minh họa rõ khả năng tránh local minima của GWO  
- Đơn giản nhưng đủ đặc trưng để quan sát hành vi tối ưu hóa  
- Dễ mở rộng sang các bài toán khác như tuning tham số, tối ưu mô hình,...

---

## 3. Cài đặt và Sử dụng (Installation & Usage)

### 🔧 Yêu cầu
- Python 3.8+  
- Các thư viện:
numpy
matplotlib
pandas
