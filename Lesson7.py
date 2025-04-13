# Vòng lặp vô hạn - Vòng lặp while

# Hiện ra màn hình các số từ 0 đến 5
    # Vòng lặp for
# for i in range(6):
#     print(i, end = ' ')
    
    # Vòng lặp while: chạy đến khi điều kiện sai
# i = 0
# while i < 6:
#     print(i, end = ' ')
#     i += 1          # i = i + 1

# Ví dụ: in ra các số nguyên từ 5 đến 12
# i = 5
# while i < 13:
#     print(i, end = ' ')
#     i += 1

# ============= LUYỆN TẬP ===================
# Bài 1: Nhập số nguyên n trong khoảng [0,100]
# nếu nhập sai (n<0 hoặc n>100) thì yêu cầu nhập lại
# n = int(input('Nhập số nguyên n trong khoảng [0,100]: '))
# while n < 0 or n > 100:
#     print('Bạn đã nhập sai, vui lòng nhập lại!')
#     n = int(input('\nNhập số nguyên n trong khoảng [0,100]: '))
# print('Nhập thành công')

# Bài 2: Tạo Mysterious Game
    # Yêu cầu: tạo ra 1 số đặc biệt để đoán (random)
    #  Người chơi cần nhập đến khi nào đoán đúng số đặc biệt thì dừng game

# Khai báo thư viện random
import random
# Tạo số đặc biệt
number = random.randint(0, 50)
# Biến đếm số lần đoán
count = 1
guess = int(input('Nhập dự đoán của bạn: '))
while guess != number:
    if guess < number:
        print('Đoán sai, hãy nhập số lớn hơn')
    if guess > number:
        print('Đoán sai, hãy nhập số nhỏ hơn')
    count += 1
    guess = int(input('\nNhập dự đoán của bạn: '))
print(f'Chúc mừng bạn đã đoán đúng sau {count} lần thử!')