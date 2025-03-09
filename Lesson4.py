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

# Nhập số điện bạn sử dụng (kWh)
kwh = float(input('Nhập số điện bạn sử dụng: '))
# Khai báo biến tiền điện
cash = 0

# Tính tiền điện
if 0 <= kwh <= 50:
    cash = kwh * 1.8
elif 50 < kwh <= 100:
    cash = 50 * 1.8 + (kwh - 50) * 2
elif 100 < kwh < 200:
    cash = 50 * 1.8 + 50 * 2 + (kwh - 100) * 2.3
elif kwh > 200:
    cash = 50 * 1.8 + 50 * 2 + 100 * 2.3 + (kwh - 200) * 3
else:
    print('Số điện không hợp lệ')

# Hiển thị kết quả
print(f'Tiền điện: {cash}k VND')

# ============= LUYỆN TẬP ===============
# Câu 1: Nhập một số từ bàn phím và in ra số đó.

# Câu 2: Viết chương trình kiểm tra nhập vào 1 số và kiểm tra số đó là chẵn hay lẻ.

# Câu 3: Viết chương trình tính tổng, hiệu, tích, thương của hai số nhập từ bàn phím.

# Câu 4: Viết chương trình chuyển đổi từ USD sang VND (số tiền được nhập từ bàn phím).

# Câu 5: Viết chương trình nhập số điểm của 3 bạn học sinh, in ra màn hình bạn có điểm thấp nhất và bạn có điểm cao nhất.