# #  Danh sách: Array / List
# #  Thao tác CRUD: Create - Read - Update - Delete

# Create - Khởi tạo danh sách
    # Danh sách rỗng - không có phần tử 
arr = []
    # Danh sách có sẵn phần tử
ptb26 = ['Minh', 'Hoàng', 'An', 'Bách', 'Nguyên']
    # len() - trả về độ dài / số lượng phần tử danh sách
print(len(ptb26))

# # Read - Duyệt, hiện phần tử
#     # Hiện phần tử bằng chỉ số index
print(ptb26[2])
print(ptb26[0])     # Phần tử đầu tiên
print(ptb26[-1])    # Phần tử cuối cùng
    
#     # Duyệt và hiện các phần tử
        # Cách 1: Dùng cả index và value
for i in range(len(ptb26)):
    print(f"Index: {i}, Value: {ptb26[i]}")

        # Cách 2: Chỉ dùng value
for item in ptb26:
    print(item)

        # Cách 3: Dùng hàm có sẵn
for index, value in enumerate(ptb26):
    print(f"Index: {index}, Value: {value}")

        # Cách 4: dùng để test
print(ptb26)

# # Update - Chỉnh sửa danh sách
    # Thêm phần tử vào cuối danh sách - append(value)
ptb26.append('Khiêm')
    # Thêm vào vị trí chỉ định - insert(index, value)
ptb26.insert(4, 'Bảo')
    # Chỉnh sửa value
ptb26[4] = 'imposter'

# # Delete - Xóa phần tử danh sách
#     # Xóa bằng giá trị - remove(value)
# ptb26.remove('Bách')
#     # Xóa bằng index - pop(index)
# ptb26.pop(4)
#     # Xóa toàn bộ danh sách - clear()
# ptb26.clear()

# # Sắp xếp phần tử danh sách - sort()
# num_list = [5, 2, 9, 7, 1, 6, 3, 8, 4]
#     # Theo thứ tự từ nhỏ đến lớn
# num_list.sort()
#     # Theo thứ tự từ lớn đến nhỏ
# num_list.sort(reverse=True)

# print(num_list)

# # Tìm phần tử lớn nhất & nhỏ nhất
# print('Phần tử lớn nhất:', max(num_list))
# print('Phần tử nhỏ nhất:', min(num_list))

# ============ LUYỆN TẬP ===============
# Bài 1: Nhập từ bàn phím 1 số nguyên n
# Yêu cầu: Kiểm tra xem n có phải là số nguyên tố hay không
# Biết rằng số nguyên tố là số chỉ chia hết cho 1 và chính nó
n = int(input('Nhập số nguyên n: '))
    # Khai báo biến count để đếm số lượng ước
count = 0
    # Duyệt từ 1 đến n
for i in range(1, n+1):
    # Nếu n chia hết cho i thì count += 1
    if n % i == 0:
        count += 1
    # Hiển thị kết quả
if count == 2:
    print(f'{n} là số nguyên tố')
else:
    print(f'{n} không phải là số nguyên tố')

# Bài 2: In ra các số nguyên tố trong khoảng [50,100] và tính tổng các số đó
sum = 0
# Duyệt các số từ 50 đến 100
for n in range (50, 101):
        # Khai báo biến count để đếm số lượng ước
    count = 0
        # Duyệt từ 1 đến n
    for i in range(1, n+1):
        # Nếu n chia hết cho i thì count += 1
        if n % i == 0:
            count += 1
        # Nếu n là snt thì cộng thêm vào biến sum
    if count == 2:
        print(n, end = ' ')
        sum += n
print('\nTổng các snt:', sum)     