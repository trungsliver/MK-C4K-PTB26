# Variables - Biến số
    # Dùng để lưu trữ dữ liệu
    # Có thể thay đổi trong khi lập trình

# Khai báo biến số: [Tên biến] = [Giá trị]
    # Khai báo 1 biến
x = 10
    # Khai báo nhiều biến số 1 lúc
a, b, c = 5, 6, 7

# Data types - Kiểu dữ liệu
    # String - chuỗi ký tự / xâu ký tự
name = 'Duc Trung'    
    # Integer (int): số nguyên
age = 30
    # Float: số thực, số thập phân
score = 9.5
    # Bool / Boolean: chỉ gồm 2 giá trị True/False - Đúng/Sai
male = True

# Kiểm tra kiểu dữ liệu - type()
print('Kiểu dữ liệu của name:', type(name))
print('Kiểu dữ liệu của age:', type(age))
print('Kiểu dữ liệu của score:', type(score))
print('Kiểu dữ liệu của male:', type(male))

# 4 cách hiển thị dữ liệu
    # Cách 1: Dùng dấu cộng
print('Họ tên: ' + name)        
print('Tuổi: ' + str(age))      # ép kiểu dữ liệu
    # Cách 2: Dùng dấu phẩy
print('Điểm số:', score)
print('Giới tính nam:', male)
    # Cách 3: Dùng format - f: truyền dữ liệu vào string
print('Tôi tên là ' + name + ', hiện đang ' + str(age) + ' tuổi.')
print(f'Tôi tên là {name}, hiện đang {age} tuổi.')
    # Cách 4: in trên nhiều dòng
print(f'''
Điểm số trung bình: {score}
Giới tính nam: {male}
''')