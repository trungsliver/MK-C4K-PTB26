# Vòng lặp hữu hạn - vòng lặp for

# Cú pháp đầy đủ: range(start, end, step)
    # start: số bắt đầu, mặc định = 0
    # end: số kết thúc
    # step: bước nhảy, mặc định = 1
# Lưu ý: chạy từ start đến (end-1)

# TH1: range(start, end, step)
# for i in range(1, 10, 2):
#     print(i)
#     print('Bảo')

# TH2: range(start, end)
# for i in range(1, 5):
#     print(i)

# TH3: range(end)
# for i in range(5):
#     print(i)

# Ví dụ:
# range(5,10): 5 => 9
# range(2, 10, 2): 2,4,6,8
# range(-5): không chạy
# range(-10, -5): -10 => -6
# range(1): 0
# range(2,8,3): 2,5
# range(2): 0,1 => rang(0, 2, 1)
# range(-5, 2): -5 => 1

# ========== LUYỆN TẬP ===========
# Bài 1: Nhập 2 số nguyên a và b từ bàn phím.
# In ra các số nguyên trong khoảng [a, b]

a = int(input('Nhập a: '))
b = int(input('Nhập b: '))
print(f'Các số trong khoảng [{a}, {b}] là:')
for i in range(a, b+1):
    print(i, end = ' ')

# Bài 2: Nhập 2 số nguyên a và b từ bàn phím.
# In ra các số nguyên trong khoảng [a, b] nếu b >= a
# In ra các số nguyên trong khoảng [b, a] nếu a > b