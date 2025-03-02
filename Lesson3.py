# # Toán tử số học
#     # Các phép toán cơ bản: + - * /
# print('1 + 1 =', 1 + 1)
#     # Lũy thừa: **
# print('2 ^ 3 =', 2**3)
#     # Chia lấy nguyên: //
#     # Chia lấy dư: %
# print('7 / 3 =', 7/3)
# print('7 // 3 =', 7//3)
# print('7 % 3 =', 7%3)

# # Toán tử số học với string
#     # Phép nối +
# print('Khôi Nguyên'  + ' ' +  'Gia Bách')
#     # Phép lặp lại *
# print('hi' * 3)

# # Toán tử quan hệ (so sánh) => True / False
#     # So sánh bằng: ==
# print('5 == 5', 5 == 5)         # True
# print('6 == 5', 6 == 5)         # False
#     # So sánh khác: !=
# print('6 != 5', 6 != 5)         # True
# print('5 != 5', 5 != 5)         # False
#     # So sánh lớn/nhỏ hơn: >, <, >=, <=
# print('5 >= 5', 5 >= 5)         # True
# print('8 < 5', 8 < 5)           # False

# # Bài tập 1
# x, y, z = 10, 6, 8
# a = x < 12 and z > 6
# b = x > 15 or y < 8
# c = not b
# print('a =', a)
# print('b =', b)
# print('c =', c)

# # Câu điều kiện
#     # Dạng thiếu
# age = int(input('Nhập tuổi của bạn: '))
# if age >= 18:
#     print('Bạn đã đủ 18 tuổi')

#     # Dạng đủ
# num = int(input('Hãy nhập 1 số nguyên: '))
# if num % 2 == 0:
#     print(num, 'là số chẵn')
# else:
#     print(num, 'là số lẻ')

    # Dạng đa nhánh
# Nhập điểm từ bàn phím (float)
# Điểm >= 8: Giỏi
# Điểm >= 6.5: Khá
# Điểm >= 5: Trung bình
# Điểm < 5: Yếu
# score = float(input('Nhập điểm của bạn: '))
# if 8 <= score <= 10:
#     print('Học lực: Giỏi')
# elif 6.5 <= score < 8:
#     print('Học lực: Khá')
# elif 5 <= score < 6.5:
#     print('Học lực: Trung bình')
# elif 0 <= score < 5:
#     print('Học lực: Yếu')
# else:
#     print('Điểm không hợp lệ')

# =============== LUYỆN TẬP ===================
#  Bài 1: Viết chương trình nhập số điểm của 3 bạn học sinh, 
# In ra màn hình bạn có điểm cao nhất.
score1 = float(input('Nhập điểm bạn 1: '))
score2 = float(input('Nhập điểm bạn 2: '))
score3 = float(input('Nhập điểm bạn 3: '))

if score1 >= score2 and score1 >= score3:
    print('Bạn 1 có điểm cao nhất')
elif score2 >= score1 and score2 >= score3:
    print('Bạn 2 có điểm cao nhất')
else:
    print('Bạn 3 có điểm cao nhất')