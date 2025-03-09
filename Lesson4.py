# Chữa BTVN: Nhập số giây
# Yêu cầu: Chuyển sang định dạng giờ - phút - giây
# 1h = 3600s, 1p = 60s
# Ví dụ: 3661s = 1h 1p 1s

# Nhập số giây cần chuyển đổi
second = int(input('Nhập số giây cần chuyển đổi: '))

# Tính số giờ
h = second // 3600
# Tính số phút
m = (second % 3600) // 60
# Tính số giây
s = second % 60

# Hiện kết quả
print(f'{second}s = {h}h {m}p {s}s')

# Bài 2: Nhập n là số kẹo, nhập m là số học sinh
# Yêu cầu: Tính số kẹo còn thừa và số kẹo dư

# Nhập dữ liệu
n = int(input('Nhập số kẹo: '))
m = int(input('Nhập số học sinh: '))

# Tính và hiển thị kết quả
print('Số kẹo học sinh nhận được:', n // m)
print('Số kẹo còn thừa:', n % m)

# Bài 3: Nhập số điện bạn sử dụng (kWh)
# Tính tiền điện theo dữ liệu sau và hiển thị ra màn hình
# Bậc 1:    0kWh - 50kWh           giá 1.8k VND
# Bậc 2:    51kWh - 100kWh         giá 2k VND
# Bậc 3:    101kWh - 200kWh        giá 2.3k VND
# Bậc 4:    trên 201kWh            giá 3k VND