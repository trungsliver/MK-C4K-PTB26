# Toán tử số học
    # Các phép toán cơ bản: + - * /
print('1 + 1 =', 1 + 1)
    # Lũy thừa: **
print('2 ^ 3 =', 2**3)
    # Chia lấy nguyên: //
    # Chia lấy dư: %
print('7 / 3 =', 7/3)
print('7 // 3 =', 7//3)
print('7 % 3 =', 7%3)

# Toán tử số học với string
    # Phép nối +
print('Khôi Nguyên'  + ' ' +  'Gia Bách')
    # Phép lặp lại *
print('hi' * 3)

# Toán tử quan hệ (so sánh) => True / False
    # So sánh bằng: ==
print('5 == 5', 5 == 5)         # True
print('6 == 5', 6 == 5)         # False
    # So sánh khác: !=
print('6 != 5', 6 != 5)         # True
print('5 != 5', 5 != 5)         # False
    # So sánh lớn/nhỏ hơn: >, <, >=, <=
print('5 >= 5', 5 >= 5)         # True
print('8 < 5', 8 < 5)           # False

# Bài tập 1
x, y, z = 10, 6, 8
a = x < 12 and z > 6
b = x > 15 or y < 8
c = not b
print('a =', a)
print('b =', b)
print('c =', c)
