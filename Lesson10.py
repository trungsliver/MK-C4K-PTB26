# Bài 1: Viết chương trình nhập từ bàn phím danh sách a. Hãy trả về kết quả các phần tử trong danh sách theo thứ tự tăng dần.
a = [5, 2, 9, 7, 1, 6, 3, 8, 4]     # Khai báo danh sách
a.sort()                            # Sắp xếp danh sách
print(a)                            # Hiện danh sách sau sắp xếp

# Bài 2: Viết chương trình nhập từ bàn phím danh sách a. Hãy tìm ra phần tử lớn nhất và nhỏ nhất từ danh sách a và trả về kết quả.
    # Cách 1: Áp dụng với danh sách đã sắp xếp
        # Phần tử lớn nhất là phần tử cuối cùng (index = -1)
print('Phần tử lớn nhất:', a[-1])
        # Phần tử nhỏ nhất là phần tử cuối cùng (index = 0)
print('Phần tử nhỏ nhất:', a[0])

    # Cách 2: Áp dụng với danh sách chưa sắp xếp
print('Phần tử lớn nhất:', max(a))
print('Phần tử nhỏ nhất:', min(a))

# Bài 3: Viết chương trình nhập từ bàn phím danh sách a. Hãy tính giá trị trung bình của các phần tử trong danh sách a và trả về kết quả giá trị trung bình.
    # Giá trị TB = Tổng giá trị phần tử / số lượng phần tử
    # Tính tổng các phần tử trong danh sách
sum = 0
for item in a:
    sum += item
    # Tính số lượng phần tử trong danh sách
sl = len(a)
    # Tính giá trị trung bình
tbc = sum / sl
print('Giá trị trung bình:', tbc)

# Bài 4: Viết chương trình nhập từ bàn phím danh sách a. Tính tổng các số lẻ và tổng các số chẵn trong danh sách a.
sum_odd = 0     # Tổng số lẻ
sum_even = 0    # Tổng số chẵn
for item in a:
    if item % 2 == 0:   # Kiểm tra số chẵn
        sum_even = sum_even + item
    if item % 2 != 0:   # Kiểm tra số lẻ
        sum_odd = sum_odd + item
print('Tổng số chẵn:', sum_even)
print('Tổng số lẻ:', sum_odd)

# Bài 5: Viết chương trình khai báo sẵn danh sách a. Viết chương trình bao gồm các chức năng: hiện toàn bộ phần tử danh sách, thêm phần tử vào danh sách, sửa phần tử danh sách, xóa phần tử trong danh sách.
    # Hiện toàn bộ phần tử danh sách
print(a)
    # Thêm phần tử danh sách
a.append(113)
    # Sửa phần tử
a[0] = 999
    # Xóa phần tử danh sách
a.remove(999)       # Xóa bằng value (giá trị)
a.pop(2)            # Xóa bằng index (vị trí)

# Luyện tập: Danh sách
    # YC1: Nhập vào từ bàn phím 1 danh sách bao gồm 10 số nguyên
num_list = [5, 2, 9, 7, 1, 6, 0, 3, 8, 4]
    # YC2: Thêm số '-5' vào vị trí thứ 2 (index=2) trong danh sách
num_list .insert(2, -5)
    # YC3: Tính tổng các số chẵn trong danh sách
sum = 0
for item in num_list:
    if item % 2 == 0:
        sum += item
print('Tổng phần tử chẵn:', sum)
    # YC4: Đếm số lượng số lẻ có trong danh sách
count = 0
for item in num_list:
    if item % 2 != 0:
        count += 1
print('Số lượng phần tử lẻ:', count)
    # YC5: Tìm giá trị phần tử lớn nhất của danh sách
print('Giá trị phần tử lớn nhất:', max(num_list))
    # YC6: Tìm vị trí phần tử nhỏ nhất của danh sách
min_item = min(num_list)            # Tìm giá trị phần tử nhỏ nhất
for i in range(len(num_list)):      # Cách duyệt 1: lấy cả index và value
    if num_list[i] == min_item:     # Kiểm tra phần tử thứ i = min_item
        min_index = i               # Lưu vị trí index của phần tử nhỏ nhất
print('Vị trí phần tử nhỏ nhất:', min_index)
        # Cách ngắn gọn (bonus):
min_index2 = num_list.index(min(num_list))
print('Vị trí phần tử nhỏ nhất:', min_index2)
    # YC7: Dùng hàm tính giá trị trung bình của các phần tử trong danh sách
    # Tính giá trị trung bình
avg_value = sum(num_list) / len(num_list)
print('Giá trị trung bình:', avg_value)     # Trước khi làm tròn
    # Làm tròn đến chữ số thập phân thứ 2
avg_value = round(avg_value, 2)
print('Giá trị trung bình:', avg_value)     # Sau khi làm tròn